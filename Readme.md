# Análise de Documentos Anti-Fraude com Azure AI

Este projeto foi desenvolvido como parte do **Bootcamp DIO - Certificação IA-102**, focado em aplicar serviços cognitivos da Microsoft Azure para resolver problemas reais de verificação de identidade e prevenção de fraudes.

## Objetivo

O sistema automatiza a extração de dados de documentos (RG, CNH, Passaportes ou faturas) utilizando OCR avançado e IA generativa para identificar inconsistências que possam indicar fraudes documentais.

## Funcionalidades

* **Extração Inteligente:** Uso do modelo `prebuilt-document` para leitura de dados estruturados e não estruturados.
* **Integração Azure:** Conexão nativa com o **Azure AI Document Intelligence** (Form Recognizer).
* **Validação Automática:** Identificação de campos críticos e pontuação de confiança ($Confidence Score$) por campo.
* **Suporte Multiformato:** Processamento de arquivos PDF, PNG e JPEG.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Cloud:** Microsoft Azure
* **Serviço de IA:** Azure AI Document Intelligence
* **Bibliotecas:** `azure-ai-formrecognizer`, `azure-core`, `python-dotenv`

## Pré-requisitos

Antes de começar, você precisará de:

1. Uma conta ativa no **Azure Portal**.
2. Um recurso do **Document Intelligence** criado (nível gratuito F0 é suficiente).
3. Python instalado na sua máquina.

## Configuração e Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/projeto-anti-fraude-azure.git
cd projeto-anti-fraude-azure


2. **Instale as dependências:**
```bash
pip install azure-ai-formrecognizer azure-core python-dotenv


3. **Configure as variáveis de ambiente:**
Crie um arquivo `.env` na raiz do projeto com suas credenciais:
```env
AZURE_ENDPOINT="https://seu-recurso.cognitiveservices.azure.com/"
AZURE_KEY="sua_chave_aqui"


## Como Rodar

1. Coloque o documento que deseja analisar na pasta raiz do projeto.
2. Altere o nome do arquivo no script `analise_documentos_facil.py`.
3. Execute o comando:
```bash
python analise_documentos_facil.py


## Lógica Anti-Fraude (MVP)

A aplicação avalia a validade do documento baseada em:

* **Nível de Confiança:** Se a IA retornar uma confiança menor que **0.8 (80%)**, o documento é marcado para revisão humana.
* **Presença de Campos Chave:** Verifica se campos obrigatórios como CPF ou Data de Nascimento foram detectados com clareza.

==X==

### TEXTOS Relevantes Para entender do assunto:
**https://www.dio.me/articles/desvendando-o-azure-ai-um-guia-tecnico-para-iniciantes-e-estudantes-6bbbd56ea00b
**https://www.nuvei.com/br/postagens/real-time-fraud-detection-strategies-for-2026-boost-approvals-now
**https://learn.microsoft.com/pt-br/azure/ai-services/content-understanding/document/analyzer-improvement
**https://learn.microsoft.com/pt-br/azure/foundry-classic/openai/how-to/risks-safety-monitor?view=foundry-classic
