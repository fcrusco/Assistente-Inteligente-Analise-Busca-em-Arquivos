# 📄 Analista IA Local (RAG Offline)

Assistente virtual conversacional baseado na arquitetura **RAG (Retrieval-Augmented Generation)** que opera de forma 100% offline. 

O sistema indexa documentos locais e responde perguntas em tempo real com privacidade total dos dados, sem acesso à internet, mapeando e listando com precisão cirúrgica apenas os arquivos físicos de origem utilizados para compor a resposta.

---

## 💡 O que o sistema faz

* **Busca Local:** Consulta múltiplos diretórios simultaneamente.
* **Rastreabilidade de Fontes:** Identifica e exibe os arquivos exatos onde a informação foi encontrada.
* **Respostas Determinísticas:** Configurado para extrair fatos reais do contexto, respondendo *"Não encontrei essa informação nos arquivos indexados."* em vez de alucinar.

---

## 🚀 Tecnologias e Pacotes

* **Linguagem:** Python 3.12+ (com suporte a venv).
* **Interface:** Streamlit (Front-end reativo web).
* **Orquestração de IA:** LangChain via LCEL (Sintaxe declarativa moderna).
* **Modelos Locais:** Ollama + Llama 3 (8B) com `temperature=0.0`.
* **Vetorização e Banco:** HuggingFace (`all-MiniLM-L6-v2`) + FAISS-CPU (banco vetorial em memória).
* **Persistência:** PyYAML (gerenciamento do arquivo `config.yaml`).

---

## 💼 Casos de Uso e Aplicações no Mercado

Por operar de forma totalmente isolada (*air-gapped*), esta aplicação resolve dores críticas em setores que lidam com segredos comerciais ou dados sensíveis:

* **Escritórios de Advocacia e Jurídico:** Consulta rápida a pilhas de petições, jurisprudências e contratos confidenciais sem expor os dados dos clientes a APIs públicas.
* **Auditoria e Compliance:** Validação e cruzamento de normas internas, regulamentos setoriais e relatórios fiscais para checagem de conformidade de processos.
* **Suporte Técnico e Help Desk Corporativo:** Indexação de manuais de engenharia, logs de servidores e bases de conhecimento legadas para aceleração do atendimento de TI nível 2 e 3.
* **Setor de Saúde e Clínicas:** Análise assistida de prontuários anonimizados, estudos de caso e relatórios de exames médicos, mantendo a conformidade restrita com leis de privacidade (LGPD).

---

## 🏁 Instalação e Execução

### Passo 1: Clonar o Repositório
```bash
git clone 
cd chat
```

### Passo 2: Configurar o Modelo Local (Ollama)
Instale o Ollama via site oficial: [ollama.com](https://ollama.com/)  
Certifique-se de que o serviço está rodando e execute no terminal:
```bash
ollama pull llama3
```

### Passo 3: Configurar o Ambiente Virtual Python
```bash
python -m venv .venv
```

* **Ativar no Windows:**
```bash
.venv\Scripts\activate
```

* **Ativar no Linux/macOS:**
```bash
source .venv/bin/activate
```

### Passo 4: Instalar as Dependências
```bash
pip install streamlit langchain langchain-community ollama faiss-cpu sentence-transformers pyyaml
```

### Passo 5: Rodar a Aplicação
```bash
streamlit run app.py
```

---

## 🛠️ Como Utilizar

1. Acesse o endereço local `http://localhost:8501` no seu navegador.
2. Na barra lateral, cole os caminhos absolutos das pastas que contêm seus arquivos (um caminho por linha) e clique em **Atualizar e Indexar**.
3. Use o chat para fazer perguntas. As fontes utilizadas aparecerão estruturadas com o nome exato dos arquivos logo abaixo da resposta da IA.


---
## 🇺🇸 English
# 📄 Local AI Analyst (Offline RAG)

Conversational virtual assistant based on the **RAG (Retrieval-Augmented Generation)** architecture that operates 100% offline. 

The system indexes local documents and answers questions in real-time with total data privacy, without internet access. It maps and lists with surgical precision only the exact source files used to compose the response.

---

## 💡 What the system does

* **Local Search:** Queries multiple directories simultaneously.
* **Source Traceability:** Identifies and displays the exact files where the information was found.
* **Deterministic Responses:** Configured to extract real facts from the context, responding with *"I did not find this information in the indexed files"* instead of hallucinating.

---

## 🚀 Technologies and Packages

* **Language:** Python 3.12+ (with venv support).
* **Interface:** Streamlit (Reactive web front-end).
* **AI Orchestration:** LangChain via LCEL (Modern declarative syntax).
* **Local Models:** Ollama + Llama 3 (8B) with `temperature=0.0`.
* **Vectorization and DB:** HuggingFace (`all-MiniLM-L6-v2`) + FAISS-CPU (in-memory vector database).
* **Persistence:** PyYAML (management of the `config.yaml` file).

---

## 💼 Use Cases and Market Applications

By operating in a completely isolated environment (*air-gapped*), this application solves critical pain points in sectors that handle trade secrets or sensitive data:

* **Law Firms and Legal:** Quick searches through piles of petitions, case laws, and confidential contracts without exposing client data to public APIs.
* **Audit and Compliance:** Validation and cross-referencing of internal norms, sector regulations, and tax reports to check process compliance.
* **Tech Support and Corporate Help Desk:** Indexing engineering manuals, server logs, and legacy knowledge bases to accelerate Tier 2 and 3 IT support.
* **Healthcare and Clinics:** Assisted analysis of anonymized medical records, case studies, and medical exam reports, maintaining strict compliance with privacy laws.

---

## 🏁 Installation and Execution

### Step 1: Clone the Repository
```bash
git clone YOUR_REPOSITORY_URL  
cd chat
```

### Step 2: Configure the Local Model (Ollama)
Install Ollama via the official website: [ollama.com](https://ollama.com/)  
Make sure the service is running and execute in the terminal:
```bash
ollama pull llama3
```

### Step 3: Configure the Python Virtual Environment
```bash
python -m venv .venv
```

* **Activate on Windows:**
```bash
.venv\Scripts\activate
```

* **Activate on Linux/macOS:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install streamlit langchain langchain-community ollama faiss-cpu sentence-transformers pyyaml
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

---

## 🛠️ How to Use

1. Access the local address `http://localhost:8501` in your browser.
2. In the sidebar, paste the absolute paths of the folders containing your files (one path per line) and click **Update and Index**.
3. Use the chat to ask questions. The sources used will appear structured with the exact file names right below the AI's response.


---
## 🇪🇸 Español
# 📄 Analista IA Local (RAG Offline)

Asistente virtual conversacional basado en la arquitectura **RAG (Retrieval-Augmented Generation)** que opera de forma 100% offline. 

El sistema indexa documentos locales y responde preguntas en tiempo real con total privacidad de los datos, sin acceso a internet, mapeando y listando con precisión quirúrgica únicamente los archivos físicos de origen utilizados para redactar la respuesta.

---

## 💡 Qué hace el sistema

* **Búsqueda Local:** Consulta múltiples directorios simultáneamente.
* **Trazabilidad de Fuentes:** Identifica y muestra los archivos exactos donde se encontró la información.
* **Respuestas Deterministas:** Configurado para extraer hechos reales del contexto, respondiendo *"No encontré esta información en los archivos indexados"* en lugar de alucinar.

---

## 🚀 Tecnologías y Paquetes

* **Lenguaje:** Python 3.12+ (con soporte para venv).
* **Interfaz:** Streamlit (Front-end reactivo web).
* **Orquestación de IA:** LangChain vía LCEL (Sintaxis declarativa moderna).
* **Modelos Locales:** Ollama + Llama 3 (8B) con `temperature=0.0`.
* **Vectorización y BD:** HuggingFace (`all-MiniLM-L6-v2`) + FAISS-CPU (base de datos vectorial en memoria).
* **Persistencia:** PyYAML (gestión del archivo `config.yaml`).

---

## 💼 Casos de Uso y Aplicaciones de Mercado

Al operar de forma totalmente aislada (*air-gapped*), esta aplicación resuelve problemas críticos en sectores que manejan secretos comerciales o datos sensibles:

* **Bufetes de Abogados y Sector Jurídico:** Consulta rápida de expedientes, jurisprudencia y contratos confidenciales sin exponer los datos de los clientes a APIs públicas.
* **Auditoría y Cumplimiento (Compliance):** Validación y cruce de normativas internas, regulaciones sectoriales e informes fiscales para comprobar la conformidad de los procesos.
* **Soporte Técnico y Help Desk Corporativo:** Indexación de manuales de ingeniería, registros de servidores y bases de conocimiento heredadas para acelerar la atención de TI de nivel 2 y 3.
* **Sector Salud y Clínicas:** Análisis asistido de historiales médicos anonimizados, estudios de casos e informes de exámenes, manteniendo un estricto cumplimiento de las leyes de privacidad.

---

## 🏁 Instalación y Ejecución

### Paso 1: Clonar el Repositorio
```bash
git clone URL_DE_TU_REPOSITORIO  
cd chat
```

### Paso 2: Configurar el Modelo Local (Ollama)
Instala Ollama a través del sitio web oficial: [ollama.com](https://ollama.com/)  
Asegúrate de que el servicio se esté ejecutando y lanza en la terminal:
```bash
ollama pull llama3
```

### Paso 3: Configurar el Entorno Virtual de Python
```bash
python -m venv .venv
```

* **Activar en Windows:**
```bash
.venv\Scripts\activate
```

* **Activar en Linux/macOS:**
```bash
source .venv/bin/activate
```

### Paso 4: Instalar las Dependencias
```bash
pip install streamlit langchain langchain-community ollama faiss-cpu sentence-transformers pyyaml
```

### Paso 5: Ejecutar la Aplicación
```bash
streamlit run app.py
```

---

## 🛠️ Cómo Utilizar

1. Accede a la dirección local `http://localhost:8501` en tu navegador.
2. En la barra lateral, pega las rutas absolutas de las carpetas que contienen tus archivos (una ruta por línea) y haz clic en **Actualizar e Indexar**.
3. Usa el chat para hacer preguntas. Las fuentes utilizadas aparecerán estructuradas con el nombre exacto de los archivos justo debajo de la respuesta de la IA.
