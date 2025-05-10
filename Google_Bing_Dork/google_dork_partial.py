import requests



API_KEY_GOOGLE = "AIzaSyD2XwQqyvYY6T5Mwg6arEN_e5dkDSW08Sc" # La API KEY de búsqueda de google enlazada a la cuenta gmail
SEARCH_ENGINE_ID = "526897637584648aa" # ID del motor de búsqueda de google enlazada a la cuenta gmail
query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)' # consulta Google Dork a realizar.
page = 1 # Número de la página que quiero acceder
language = "lang_es" # Lang del idioma que queremos que aparezcan las páginas.

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY_GOOGLE}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={language}"


data = requests.get(url).json() # Obtiene la data en forma de diccionario (json).
# requests.get() -> devuelve el resultado de la consulta, .json() -> permite devolverlo como JSON (necesario para usar la API de google)
results = data.get("items")

for i in results:
    print("----- Nuevo resultado -----")
    print(i.get("title"))
    print(i.get("snippet"))
    print(i.get("link"))
    print("---------------------------")