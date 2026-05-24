import streamlit as st
import yaml
import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- CONFIGURAÇÕES DE ARQUIVO ---
CONFIG_FILE = "config.yaml"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f) or {"caminhos": []}
    return {"caminhos": []}

def save_config(caminhos):
    with open(CONFIG_FILE, "w") as f:
        yaml.dump({"caminhos": caminhos}, f)

# --- LÓGICA DE IA (RAG COM LCEL) ---
@st.cache_resource
def processar_arquivos(caminhos):
    documentos = []
    for path in caminhos:
        if os.path.exists(path):
            loader = DirectoryLoader(
                path, 
                glob="**/*.txt", 
                loader_cls=TextLoader, 
                loader_kwargs={"encoding": "utf-8"},
                silent_errors=True
            )
            documentos.extend(loader.load())
    
    if not documentos:
        return None

    # Fatiamento preciso para indexação sem ruídos
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       
        chunk_overlap=50     
    )
    documentos_fatiados = text_splitter.split_documents(documentos)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documentos_fatiados, embeddings)
    return vectorstore

# --- INTERFACE STREAMLIT ---
st.set_page_config(page_title="Analista IA Local", layout="wide")
st.title("📄 Assistente Inteligente - Análise/Busca em Arquivos")

# Sidebar - Configuração de Caminhos
with st.sidebar:
    st.header("⚙️ Configurações")
    config = load_config()
    caminhos_text = st.text_area("Caminhos dos Diretórios (um por linha):", 
                                 value="\n".join(config["caminhos"]))
    
    if st.button("Atualizar e Indexar"):
        novos_caminhos = [c.strip() for c in caminhos_text.split("\n") if c.strip()]
        save_config(novos_caminhos)
        st.session_state.vectorstore = processar_arquivos(novos_caminhos)
        st.success("Arquivos indexados com sucesso!")

# Inicialização do Cérebro
if "vectorstore" not in st.session_state:
    config = load_config()
    if config["caminhos"]:
        st.session_state.vectorstore = processar_arquivos(config["caminhos"])

# Interface de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Sobre qual informação dos arquivos deseja o relatório?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processamento da Resposta
    if "vectorstore" in st.session_state and st.session_state.vectorstore:
        with st.chat_message("assistant"):
            llm = Ollama(model="llama3", temperature=0.0) # Deterministico
            
            # Prompt focado puramente em responder de forma direta
            template = """Você é um analista de dados focado em responder perguntas estritamente com base nos textos fornecidos.
            Sempre responda em Português do Brasil de forma direta.
            Se a resposta exata para a pergunta não estiver presente nos trechos de contexto abaixo, responda estritamente: "Não encontrei essa informação nos arquivos indexados."

            Contexto:
            {context}

            Pergunta: {question}
            Resposta:"""

            PROMPT = PromptTemplate(
                template=template, input_variables=["context", "question"]
            )

            # Função auxiliar para formatar os documentos textualmente
            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            # k=5 para garantir captura de múltiplos arquivos contendo o mesmo fato
            retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 5})
            
            # Construção da Chain usando a sintaxe LCEL
            rag_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | PROMPT
                | llm
                | StrOutputParser()
            )
            
            with st.spinner("Consultando arquivos locais..."):
                # 1. Recupera os documentos brutos do FAISS
                docs_recuperados = retriever.invoke(prompt)
                
                # 2. Executa a inteligência artificial para obter a resposta textual limpa
                resposta_texto = rag_chain.invoke(prompt).strip()
            
            # --- VALIDAÇÃO DE FONTES HÍBRIDA E MULTI-ARQUIVO ---
            if "Não encontrei essa informação" in resposta_texto:
                resposta_final = resposta_texto
            else:
                arquivos_validos = set()
                resposta_minuscula = resposta_texto.lower()
                
                # ALTERAÇÃO CRÍTICA: Remove o nome comum repetido que causava falsos positivos generalizados
                nome_comum = "fabio crusco da silva"
                resposta_higienizada = resposta_minuscula.replace(nome_comum, "")
                
                # Limpa pontuações residuais
                texto_limpo = resposta_higienizada.replace(".", "").replace(",", "").replace(":", "").strip()
                palavras = [p for p in texto_limpo.split() if len(p) > 2] # ignora conectores pequenos
                
                # Monta n-grams sequenciais com o conteúdo purificado da resposta
                tamanho_segmento = min(3, len(palavras))
                segmentos_resposta = []
                if tamanho_segmento >= 2:
                    for i in range(len(palavras) - tamanho_segmento + 1):
                        segmentos_resposta.append(" ".join(palavras[i:i+tamanho_segmento]))
                else:
                    segmentos_resposta = [texto_limpo] if texto_limpo else []

                for doc in docs_recuperados:
                    nome_arq = os.path.basename(doc.metadata.get("source", ""))
                    conteudo_chunk = doc.page_content.lower()
                    
                    # Se houver segmentos reais de fatos (ex: "iniciado em 2026") dentro do arquivo
                    if segmentos_resposta and any(segmento in conteudo_chunk for segmento in segmentos_resposta if len(segmento) > 8):
                        if nome_arq:
                            arquivos_validos.add(nome_arq)
                
                # Exibição do resultado consolidado com suporte a múltiplas fontes
                if arquivos_validos:
                    arquivos_ordenados = sorted(list(arquivos_validos))
                    fontes_str = "\n\n**📌 Informação encontrada no(s) arquivo(s):**\n" + "\n".join([f"- `{arq}`" for arq in arquivos_ordenados])
                    resposta_final = f"{resposta_texto}{fontes_str}"
                else:
                    # Fallback de segurança: se a filtragem for estrita demais, traz apenas o k=1 mais relevante do vetor
                    nome_fallback = os.path.basename(docs_recuperados[0].metadata.get("source", ""))
                    resposta_final = f"{resposta_texto}\n\n**📌 Informação encontrada no arquivo:**\n- `{nome_fallback}`"

            st.markdown(resposta_final)
            st.session_state.messages.append({"role": "assistant", "content": resposta_final})
    else:
        st.error("Por favor, configure e indexe os caminhos de arquivos na barra lateral.")