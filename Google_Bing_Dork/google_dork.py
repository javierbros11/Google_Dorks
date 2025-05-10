# External Packages

from dotenv import load_dotenv,set_key
import os
import argparse
import sys
# Local files
from google_config import GoogleConfig
from browserautosearch_bing import BrowserAutoSearch
from ai_agent_google import IAAgent
from google_file_downloader import FileDownloader
from googlesearch import GoogleSearch
from results_parser import ResultsParser

# IA Config

def _openai_config(self):
        """
        Configura la API_KEY de OpenAI en el fichero .env
        """

        api_key = input("Introduce tu API_KEY de OpenAI: ")
        set_key(".env","OPENAI_API_KEY",api_key)

# Main Code

def main(query,configure_env, start_page, pages, lang,output_json,output_html,download,gen_dork,selenium):
    
    # Config setup

    configure = GoogleConfig(configure_env)
    API_KEY_GOOGLE, SEARCH_ENGINE_ID = configure.load_env()

    if gen_dork:
        print("Utilizando gpt4all y ejecutando la generación en local. Puede tardar unos minutos...")
        ia_agent = IAAgent()
        respuesta = ia_agent.generate_gdork(gen_dork)
        print(f"\nResultado:\n{respuesta}")
        sys.exit(1)

    if not query:
        print("Indica una consulta con el comando -q. Utiliza el comando -h para ver la ayuda")
        sys.exit(1)

    elif selenium:
        browser = BrowserAutoSearch()
        browser.search_bing(query=query)
        resultados = browser.bing_search_results()
        browser.quit()
    
    else:
        #API_KEY_GOOGLE,SEARCH_ENGINE_ID = load_env(configure_env=configure_env)
        busqueda = GoogleSearch(API_KEY_GOOGLE,SEARCH_ENGINE_ID)
        resultados = busqueda.search(query,start_page=start_page,pages = pages,lang=lang)
    
    rparser = ResultsParser(resultados)

    # Mostrar los resultados en linea de consola de comandos.

    rparser.mostrar_pantalla()

    if output_html:
        rparser.exportar_html(output_html)
    
    if output_json:
        rparser.exportar_json(output_json)

    # En cuanto a la descarga de ficheros PDF es posibles que algunas descargas fallen debido al uso de CDNs.
    if download:
        # Separar las extensiones de los archivos en una lista
        file_types = download.split(",")
        # Nos quedamos con las URLs de los resultados obtenidos
        urls = [resultado['link'] for resultado in resultados]
        descarga_ficheros = FileDownloader("Descargas_GoogleDorks")
        descarga_ficheros.filtra_descarga(urls,file_types)

if __name__ == "__main__":
    # Configuración de los argumentos del programa
    parser = argparse.ArgumentParser(description = "Esta herramienta permite realizar Hacking con buscadores de forma automática. En este caso emplearemos principalmente el buscador de Google Chrome/Bing.")
    parser.add_argument("-q","--query", type=str,
                        help="Este argumento especifica la consulta a realizar.\nEjemplo: '-q marca.com'")
    parser.add_argument("-c", "--configure", action="store_true",
                        help="Inicia el proceso de configuración del archivo .env.\nUtiliza esta opcion sin otros argumentos para configurar las claves.")
    parser.add_argument("--start-page", type=int, default=1,
                        help="Define la página de incio del buscador donde empezará a recibir resultados.")
    parser.add_argument("--pages",type=int,default=1,
                        help="Es el número de páginas en total que se desean consultar. Cada página consta de 10 resultados de búsqueda.")
    parser.add_argument("--lang",type=str,default="lang_es",
                        help="Código de idioma de cara a los resultados de búsqueda. Por defecto es 'lang-es' (español)")
    parser.add_argument("--json",type=str,
                        help="Exporta los resultados en formato JSON, indicando el nombre del archivo con su extensión .json. Se almacena en la misma ruta que el programa principal.")
    parser.add_argument("--html",type=str,
                        help="Exporta los resultados en formarto HTML indicando el nombre del archivo con su extensión .html. Se almacena en la misma ruta que el programa principal.")
    parser.add_argument("--download", type=str,
                        help="Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se desean descargar.\nEjemplo: --download 'pdf,sql,doc'")
    parser.add_argument("-gd","--generate-dork", type=str,
                        help="Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado de generar dicha consulta.\n" \
                        "Por ejemplo: --generate-dork 'Listado de usuarios y passwds en un fichero de texto.'")
    parser.add_argument("--selenium",action="store_true", default=False,
                        help="Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de realizar cualquier búsqueda.")
    args = parser.parse_args()
    
    main(query = args.query,configure_env=args.configure,start_page=args.start_page,pages=args.pages,
         lang=args.lang,output_json=args.json,output_html=args.html,download=args.download,
         gen_dork = args.generate_dork,selenium = args.selenium)