# External Packages

from dotenv import load_dotenv, set_key
import os
import sys

class GoogleConfig:
    """
    Realiza la configuración del archivo .env.
    """

    def __init__(self,configure_env):
        """
        Inicializa los atributos de instancia.
        Args:
            configure_env(bool): Indica si se quiere configurar las APIs.
        """
        self.configure = configure_env
    
    def _env_config(self):
        """
        Se encarga de configurar el archivo .env con los valores proporcionados.
        """
        api_key = input("Introduce tu API_KEY de Google: ")
        engine_id = input("Introduce el id del buscador personalizado de Google: ")

        set_key(".env","API_KEY_GOOGLE",api_key)
        set_key(".env","SEARCH_ENGINE_ID",engine_id)


    def load_env(self):
        # Comprobamos si existe el fichero .env
        env_exists = os.path.exists(".env")

        if not env_exists or self.configure:
            self._env_config()
            print("Archivo .env configurado satisfactoriamente.")
            print("Por favor, realiza de nuevo la consulta.")
            sys.exit(1)
            
        else:
            print("El archivo .env ya estaba creado.\n Cargando las APIs de entorno...")
        # Cargamos las variables en el entorno
        load_dotenv()

        # Leer las variables del entorno en nuestro programa (API -> 100 peticiones/dia ID -> Engine_ID)
        API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
        SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

        print("APIs de entorno cargadas satisfactoriamente :)")
        return (API_KEY_GOOGLE,SEARCH_ENGINE_ID)