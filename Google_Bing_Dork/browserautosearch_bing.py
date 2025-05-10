from selenium import webdriver # Hace referencia al conjunto de drivers necesarios para la ejecución del navegador
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class BrowserAutoSearch:
    def __init__(self):
        self.browser = self._initialize_browser()

    def _initialize_browser(self):
        browsers = {
            "firefox" : {
                "service" : FirefoxService(GeckoDriverManager().install()),
                "options" : webdriver.FirefoxOptions(),
                "driver" : webdriver.Firefox
            },
            "chrome" : {
                "service" : ChromeService(ChromeDriverManager().install()),
                "options" : webdriver.ChromeOptions(),
                "driver" : webdriver.Chrome
            }
        }

        # Incializamos los navegadores
        for browser_name,browser_info in browsers.items():
            try:
                return browser_info["driver"](service=browser_info["service"],options=browser_info["options"])
            except Exception as e:
                print(f"Error al intentar inicializar el navegador {browser_name}: {e}")
        
        raise Exception("No se pudo inicial ningún navegador, ¿tiene instalador Firefox o Chrome?")
    
# Inicializa el webdriver Firefox

# Inicializa el Webdriver de Chrome
# service = Service(ChromeDriverManager().install())
# options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(service=service,options=options)

    def accept_cookies(self, button_selector):
        """
        Acepta el anuncio de cookies de un buscador.
        """
        try:
            accept_button = self.browser.find_element(By.ID, button_selector)
            accept_button.click()
        except Exception as e:
            print(f"Error al intentar aceptar las cookies del buscador: {e}")

    def search_bing(self,query):
        """
        Realiza una búsqueda en Bing.
        """
        
        # Abre Google
        self.browser.get("https://www.bing.com")

        # Esperamos unos segundos hasta que aparezca la opción de aceptar cookies.
        time.sleep(5)

        # Aceptamos las cookies que proporciona Google
        self.accept_cookies(button_selector="bnp_btn_accept")

        # Encuentra el cuadro de búsqueda y envia la cadena de texto
        time.sleep(3)
        search_box = self.browser.find_element(By.NAME, "q")
        search_box.send_keys(query + Keys.ENTER)

        # Esperamos a que la página cargue los resultados
        time.sleep(5)

    def bing_search_results(self):
        """
        Extrae los resultados en una consulta en Bing.
        """
        # Extraemos los enlaces y descripciones de los primeros resultados
        results = self.browser.find_elements(By.CLASS_NAME, "b_algo")
        custom_results = []
        for resultado in results:
            try:
                cresult = {}
                cresult["title"] = resultado.find_element(By.CSS_SELECTOR, "a").text
                cresult["link"] = resultado.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                
                if resultado.find_element(By.CLASS_NAME, "b_lineclamp2").text:
                    cresult["description"] = resultado.find_element(By.CLASS_NAME, "b_lineclamp2").text

                elif resultado.find_element(By.CLASS_NAME, "b_lineclamp3").text:
                    cresult["description"] = resultado.find_element(By.CLASS_NAME, "b_lineclamp3").text
                custom_results.append(cresult)
            except Exception as e:
                #print(f"Se ha producido una excepción a la hora de recolectar los resultados: {e}")
                continue
        return custom_results
    
    def quit(self):
        # Cerramos el navegador
        self.browser.quit()