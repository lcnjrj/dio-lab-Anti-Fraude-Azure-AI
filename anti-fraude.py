import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError

# Carrega variáveis de um arquivo .env
load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")

def analisar_fraude_identidade(caminho_arquivo):
    if not AZURE_ENDPOINT or not AZURE_KEY:
        raise ValueError("Configurações do Azure não encontradas no ambiente.")

    client = DocumentAnalysisClient(AZURE_ENDPOINT, AzureKeyCredential(AZURE_KEY))

    try:
        with open(caminho_arquivo, "rb") as f:
            # Usando o modelo especializado em documentos de identidade
            poller = client.begin_analyze_document("prebuilt-idDocument", document=f)
            result = poller.result()

        for id_document in result.documents:
            print(f"--- Documento Detectado: {id_document.doc_type} ---")
            
            # Exemplo de lógica anti-fraude: Validar campos críticos
            fields = id_document.fields
            nome = fields.get("FirstName")
            sobrenome = fields.get("LastName")
            doc_number = fields.get("DocumentNumber")
            
            if nome and sobrenome:
                print(f"Nome Extraído: {nome.value} {sobrenome.value} (Confiança: {nome.confidence:.2%})")
            
            # Alerta de baixa confiança (Possível fraude ou imagem ruim)
            if nome and nome.confidence < 0.8:
                print("[ALERTA] Baixa confiança na extração. Verificação manual necessária.")

    except AzureError as e:
        print(f"Erro na API do Azure: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    analisar_fraude_identidade("cnh_teste.jpg")
