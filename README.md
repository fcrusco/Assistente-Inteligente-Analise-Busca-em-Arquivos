📄 Analista IA Local (RAG Offline)
Assistente virtual conversacional baseado na arquitetura RAG (Retrieval-Augmented Generation) que opera de forma 100% offline. 
O sistema indexa documentos locais e responde perguntas em tempo real com privacidade total dos dados, sem acesso a internet, mapeando e listando com precisão cirúrgica apenas os arquivos físicos de origem utilizados para compor a resposta.

💡 O que o sistema faz
Busca Local: Consulta múltiplos diretórios simultaneamente.
Rastreabilidade de Fontes: Identifica e exibe os arquivos exatos onde a informação foi encontrada.
Respostas Determinísticas: Configurado para extrair fatos reais do contexto, respondendo "Não encontrei essa informação nos arquivos indexados." em vez de alucinar.

🚀 Tecnologias e Pacotes
Linguagem: Python 3.12+ (com suporte a venv).
Interface: Streamlit (Front-end reativo web).
Orquestração de IA: LangChain via LCEL (Sintaxe declarativa moderna).
Modelos Locais: Ollama + Llama 3 (8B) com temperature=0.0.
Vetorização e Banco: HuggingFace (all-MiniLM-L6-v2) + FAISS-CPU (banco vetorial em memória).
Persistência: PyYAML (gerenciamento do arquivo config.yaml).

💼 Casos de Uso e Aplicações no Mercado
Por operar de forma totalmente isolada (air-gapped), esta aplicação resolve dores críticas em setores que lidam com segredos comerciais ou dados sensíveis:
Escritórios de Advocacia e Jurídico: Consulta rápida a pilhas de petições, jurisprudências e contratos confidenciais sem expor os dados dos clientes a APIs públicas.
Auditoria e Compliance: Validação e cruzamento de normas internas, regulamentos setoriais e relatórios fiscais para checagem de conformidade de processos.
Suporte Técnico e Help Desk Corporativo: Indexação de manuais de engenharia, logs de servidores e bases de conhecimento legadas para aceleração do atendimento de TI nível 2 e 3.
Setor de Saúde e Clínicas: Análise assistida de prontuários anonimizados, estudos de caso e relatórios de exames médicos, mantendo a conformidade restrita com leis de privacidade (LGPD).

🏁 Instalação e Execução
Passo 1: Clonar o Repositório

Passo 2: Configurar o Modelo Local (Ollama)
Instale o Ollama via site oficial: ollama.com
Certifique-se de que o serviço está rodando e execute no terminal:
ollama pull llama3

Passo 3: Configurar o Ambiente Virtual Python
python -m venv .venv
Ativar no Windows: .venv\Scripts\activate
Ativar no Linux/macOS: source .venv/bin/activate

Passo 4: Instalar as Dependências
pip install streamlit langchain langchain-community ollama faiss-cpu sentence-transformers pyyaml

Passo 5: Rodar a Aplicação
streamlit run app.py

🛠️ Como Utilizar
Acesse o endereço local http://localhost:8501 no seu navegador.
Na barra lateral, cole os caminhos absolutos das pastas que contêm seus arquivos (um caminho por linha) e clique em Atualizar e Indexar.
Use o chat para fazer perguntas. As fontes utilizadas aparecerão estruturadas logo abaixo da resposta da IA.
