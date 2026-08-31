# 🤖 Criador Multi-Agente de Posts com a API do Google Gemini

> **Projeto de Estudos em Inteligência Artificial, Engenharia de Prompt e Sistemas Multi-Agente.**  
> Este repositório demonstra a construção de um pipeline de 4 agentes especializados que trabalham de forma colaborativa para pesquisar, planejar, redigir e revisar posts para redes sociais (Instagram) focados em tecnologia.

---

## 📌 Sobre o Projeto

O objetivo deste projeto é explorar o poder dos modelos **Gemini** e do ecossistema da **Google GenAI SDK** para solucionar um problema real: a criação automatizada de conteúdo relevante e atualizado para redes sociais.

A solução utiliza **Google Search Grounding** para que o primeiro agente acesse dados em tempo real na web, garantindo que os posts sejam baseados em novidades e notícias recentes.

---

## 🏗️ Arquitetura do Sistema Multi-Agente

O fluxo de trabalho é dividido em 4 etapas sequenciais, onde a saída de cada agente serve como contexto para o próximo:

```
                  [ Tópico do Usuário ]
                            │
                            ▼
     ┌─────────────────────────────────────────────┐
     │ 1. Agente Buscador (Search Grounding)       │
     │    Pesquisa notícias recentes no Google     │
     └──────────────────────┬──────────────────────┘
                            │
                            ▼
     ┌─────────────────────────────────────────────┐
     │ 2. Agente Planejador                        │
     │    Estrutura o roteiro (Hook, Pontos, CTA)  │
     └──────────────────────┬──────────────────────┘
                            │
                            ▼
     ┌─────────────────────────────────────────────┐
     │ 3. Agente Redator                           │
     │    Escreve o rascunho (Emojis + Hashtags)   │
     └──────────────────────┬──────────────────────┘
                            │
                            ▼
     ┌─────────────────────────────────────────────┐
     │ 4. Agente Revisor                           │
     │    Refina tom de voz, gramática e estilo    │
     └──────────────────────┬──────────────────────┘
                            │
                            ▼
              [ 📲 Post Final de Instagram ]
```

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **[Google GenAI SDK (`google-genai`)](https://github.com/googleapis/python-genai)**: SDK oficial da Google para acesso aos modelos Gemini.
- **Gemini 2.5 Flash / Gemini Pro**: Modelos de linguagem para geração e raciocínio.
- **Google Search Grounding**: Ferramenta nativa do Gemini para busca web.
- **Python-Dotenv**: Gerenciamento seguro de chaves de API.
- **Jupyter Notebook**: Ambiente para experimentação e estudos.

---

## 📂 Estrutura do Repositório

```text
AI_Multi_Agent_Post_Creator/
│
├── README.md                            # Documentação principal do projeto
├── requirements.txt                    # Dependências do projeto
├── .env.example                        # Modelo para variáveis de ambiente
├── .gitignore                          # Arquivos ignorados pelo Git
│
├── notebooks/                          # Notebooks Jupyter para estudos e testes
│   └── 01_estudo_agentes_gemini.ipynb   # Notebook completo e comentado
│
└── src/                                # Código-fonte modular do projeto
    ├── __init__.py
    ├── agents.py                       # Definição e lógica dos 4 agentes
    └── main.py                         # Interface interativa de terminal
```

---

## 💻 Como Executar o Projeto

### Pré-requisitos

- Python 3.10 ou superior instalado.
- Uma chave de API gratuita do Google Gemini (obtenha no [Google AI Studio](https://aistudio.google.com/)).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/AI_Multi_Agent_Post_Creator.git
   cd AI_Multi_Agent_Post_Creator
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   # No Windows:
   python -m venv venv
   .\venv\Scripts\activate

   # No Linux/Mac:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure sua Chave de API:**
   - Copie o arquivo `.env.example` para `.env`:
     ```bash
     cp .env.example .env
     ```
   - Abra o arquivo `.env` e substitua pelo seu token da API:
     ```env
     GOOGLE_API_KEY=sua_chave_aqui
     ```

5. **Execute a aplicação via Terminal:**
   ```bash
   python src/main.py
   ```

6. **Ou explore pelo Jupyter Notebook:**
   ```bash
   jupyter notebook notebooks/01_estudo_agentes_gemini.ipynb
   ```

---

## 🧠 Aprendizados e Conclusões

Neste projeto de estudos, foi possível compreender e aplicar:
1. **Engenharia de Prompt Específica**: Definição de papéis (personas) e contextos delimitados para obter respostas mais precisas de cada agente.
2. **Grounding (Ancoragem de Dados)**: Uso da busca do Google para mitigar alucinações de modelos de IA sobre fatos recentes.
3. **Arquitetura Encadeada**: Como quebrar uma tarefa complexa (criar um post) em sub-tarefas menores executadas por agentes especialistas.

---

## 📜 Licença

Este projeto é de código aberto sob a licença [MIT](LICENSE). Sinta-se à vontade para utilizar, modificar e contribuir!
