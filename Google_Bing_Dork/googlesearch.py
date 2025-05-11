# Packages

import requests

# Class

class GoogleSearch:

    def __init__(self, api_key,engine_id):
        """
        Inicializa una nueva instancia de Google Search.

        Esta clase permite realizar peticiones automátizadas a la API de Google.

        Args:
            api_key(str): Clave API de Google.
            engine_id(str): Identificador del motor de búsqueda personalizado de Google.
        """

        self.api_key = api_key
        self.engine_id = engine_id

    def search(self,query, start_page = 1, pages = 1,lang = "lang_es"):
        """
        Realiza una búsqueda en Google utilizando su API.
        
        Args:
            query(str): Google Dork a realizar.
            start_page(int)(default = 1): Página de comienzo
            pages(int)(default = 1): Número de páginas que quiere obtener
            lang(str): Establece el lenguaje de la búsqueda.
        """

        final_results = []
        results_per_page = 10 # Google muestra por defecto 10 resultados por página.
        for page in range(pages):
            # Calculamos el resultado de comienzo de cada página.
            start_index = (start_page - 1) * results_per_page + 1 + (page * results_per_page) # Total de resultados en función de las páginas en total, cada página consta de 10 resultados.
            url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.engine_id}&q={query}&start={start_index}&lr={lang}"
            response = requests.get(url)
            # Comprobamos si la respuesta es correcta
            if response.status_code == 200:
                data = response.json()
                results = data.get("items")
                cresults = self.custom_results(results)
                final_results.extend(cresults)
            else:
                print(f"Error obtenido al consultar la página: {page}: HTTP {response.status_code}")
                break # Rompemos la iteración actual.
        return final_results
    
    def custom_results(self, results):
        """
        Filtra los resultados de la consulta.

        Args:
            response(dict): Resultados de cada una de las consultas realizadas anteriormente en el método search.
        """
        
        custom_results = []

        for i in results:
            cresult = {}
            cresult["title"] = i.get("title")
            cresult["description"] = i.get("snippet")
            cresult["link"] = i.get("link")
            custom_results.append(cresult)
        return custom_results
