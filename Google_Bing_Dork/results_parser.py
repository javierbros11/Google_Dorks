# Packages

import json
from rich.console import Console
from rich.table import Table

# Class
class ResultsParser:

    def __init__(self, results):
        """
        Inicializa los atributos de instancia.
        
        Args:
            results(dict): Conjunto de resultados de búsqueda obtenidas en función de las páginas exploradas.
        """

        self.results = results
    
    def exportar_html(self, ruta_salida):
        """
        Permite exportar los resultados obtenidos en un archivo .html.

        Args:
            ruta_salida(str): Corresponde a la ruta donde se almacenará el archivo .html.
        """
        
        with open("html_template_google_dorks.html", "r", encoding="utf-8") as f:
            plantilla = f.read()

        elementos_html = ''
        for indice, resultado in enumerate(self.results, start=1):
            elemento = f'<div class="resultado">' \
                f'<div class="indice"> Resultado {indice}</div>' \
                f'<h5>{resultado["title"]}</h5>' \
                f'<p>{resultado["description"]}</p>' \
                f'<a href="{resultado["link"]}" target="_blank">{resultado["link"]}</a>' \
                f'</div>'
            elementos_html += elemento
        informe_html = plantilla.replace("{{ resultados }}", elementos_html)
        with open(ruta_salida, 'w', encoding="utf-8") as f:
            f.write(informe_html)
        print(f"Resultados exportados a HTML. Fichero creado: {ruta_salida}")
    
    def exportar_json(self,ruta_salida):
        """
        Permite exportar los resultados obtenidos en un archivo .json.

        Args:
            ruta_salida(str): Corresponde a la ruta donde se almacenará el archivo .json.
        """
        
        with open(ruta_salida, "w", encoding="utf-8") as f:
            json.dump(self.results, f ,ensure_ascii=False, indent=4) # <- 4 espacios de identación al inicio del doc
        print(f"Resultados exportados a JSON. Fichero creado: {ruta_salida}")
    
    def mostrar_pantalla(self):
        """
            Muestra por linea de comandos los resultados obtenidos tras realizar la consultas.
        """
        
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim")
        table.add_column("Titulo", width=50)
        table.add_column("Descripcion")
        table.add_column("Enlace")

        for indice,resultado in enumerate(self.results, start=1):
            table.add_row(str(indice), resultado["title"], resultado["description"], resultado["link"])
            table.add_row("","","","")

        console.print(table)
