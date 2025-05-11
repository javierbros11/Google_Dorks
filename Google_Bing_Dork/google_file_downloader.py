# Packages

import os
import requests

# Class

class FileDownloader:
    """
    Se trata de una clase que permite la descarga de ficheros de aquellos resultados obtenidos anteriormente durante
    una búsqueda con un dork.
    """
    def __init__(self, directorio_destino):
        """
        Constructor de la clase. Realiza la inicialización de las instancias.

        Args:
            ruta_destino(str): Ruta dentro del equipo local donde se almacenará los diferentes ficheros que descarguemos.
        """
        self.directorio = directorio_destino
        self.crear_directorio()

    def crear_directorio(self):
        """
        En el caso de que no exista la ruta de destino proporcionada, este método se encarga de crearla.
        """
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)

    def downloader(self, url):
        """
        Permite la descarga del fichero correspondiente asociada a la URL aportada.

        Args:
            url(str): Contiene la URL donde se almacena el fichero a descargar.
        """
        try:
            respuesta = requests.get(url)
            nombre_archivo = url.split("/")[-1] # Obtenemos el nombre del fichero extrayéndolo de la URL
            ruta_completa = os.path.join(self.directorio, nombre_archivo)
            # Guardamos el archivo en disco

            with open(ruta_completa, "wb") as archivo:
                archivo.write(respuesta.content)
            print(f"Archivo {nombre_archivo} almacenado en {ruta_completa}.")
        except Exception as e:
            print(f"Se ha producido un error al descargar {nombre_archivo}: {e}")

    def filtra_descarga(self, urls, formato_archivos = ["all"]):
        """
        Este métido realiza el filtrado de descarga de ficheros en función del formato que se quiera descargar.

        Args:
            urls(list): Lista que contiene el conjunto de URLs donde residen los ficheros que queremos descargar.
            filetype(list): Lista donde se almacena los tipos de ficheros que queremos almacenar.
        """
        if formato_archivos == ["all"]:
            for url in urls:
                self.downloader(url)
        else:
            for url in urls:
                if any(url.endswith(f".{tipo}") for tipo in formato_archivos): # Recorre todos los tipos de archivos que queremos y comprueba si una url termina con esa extensión del archivo.
                    self.downloader(url)
