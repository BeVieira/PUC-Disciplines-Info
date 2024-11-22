from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium import webdriver
import time

# Instala automaticamente o ChromeDriver correspondente à versão do Chrome instalada
chromedriver_autoinstaller.install()

# Lista com os códigos das disciplinas
disciplinas = [
    "ADM1019", "INF1009", "INF1010", "INF1011", "INF1012", "INF1014", "INF1015", "INF1018",
    "INF1022", "INF1027", "INF1028", "INF1029", "INF1032", "INF1034", "INF1036", "INF1038",
    "INF1039", "INF1040", "INF1041", "INF1301", "INF1304", "INF1316", "INF1350", "INF1377",
    "INF1383", "INF1403", "INF1408", "INF1410", "INF1608", "INF1629", "INF1631", "INF1636",
    "INF1640", "INF1721", "INF1761", "INF1771", "INF2218", "JUR1809", "LET1920"
]

# Função para capturar e salvar a ementa de cada disciplina
def capturar_ementas(disciplinas):
    # Inicializa o WebDriver
    driver = webdriver.Chrome()

    # Cria e abre o arquivo de texto para salvar as ementas
    with open("ementas.txt", "w", encoding="utf-8") as file:
        for codigo_disciplina in disciplinas:
            url = f'https://www.puc-rio.br/ferramentas/ementas/ementa.aspx?cd={codigo_disciplina}'
            driver.get(url)
            
            try:
                # Aguarda até que o elemento com o conteúdo da ementa esteja presente
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "divContent"))
                )
                ementa_texto = element.text
                # Escreve a ementa no arquivo
                file.write(f"Ementa da disciplina {codigo_disciplina}:\n")
                file.write(ementa_texto + "\n\n")
                print(f"Ementa da disciplina {codigo_disciplina} salva com sucesso.")
                
                time.sleep(1)  # Pequena pausa entre cada requisição para evitar sobrecarregar o servidor
                
            except Exception as e:
                print(f"Erro ao encontrar a ementa para a disciplina {codigo_disciplina}. Erro: {e}")
                file.write(f"Ementa da disciplina {codigo_disciplina} não encontrada. Erro: {e}\n\n")

    # Fecha o navegador após a execução
    driver.quit()

# Executa a função
capturar_ementas(disciplinas)
