import os
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_azure_client():
    """Inicializa o cliente Azure de forma segura."""
    endpoint = os.getenv("AZURE_ENDPOINT")
    key = os.getenv("AZURE_KEY")
    
    if not endpoint or not key:
        raise ValueError("ERRO: AZURE_ENDPOINT ou AZURE_KEY não configurados no arquivo .env")
        
    return DocumentAnalysisClient(
        endpoint=endpoint, 
        credential=AzureKeyCredential(key)
    )

def analisar_documento(caminho_arquivo):
    client = get_azure_client()
    
    try:
        with open(caminho_arquivo, "rb") as f:
            # Iniciando análise com modelo pré-treinado
            poller = client.begin_analyze_document("prebuilt-document", document=f)
            resultado = poller.result()
            
        print(f"\n--- Análise Concluída: {caminho_arquivo} ---")
        for i, pagina in enumerate(resultado.pages):
            print(f"Lendo página {i+1}...")
            for linha in pagina.lines:
                print(f" > {linha.content}")
                
        return resultado

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro durante a análise: {e}")

if __name__ == "__main__":
    # Nome do seu arquivo de teste
    arquivo = "exemplo.pdf" 
    analisar_documento(arquivo)
