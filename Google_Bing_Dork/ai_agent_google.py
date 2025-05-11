from gpt4all import GPT4All

class IAAgent:

    """
    Esta clase permite generar mediante el uso de IA (GPT4All) una respuesta teniendo en cuenta la descripción del usuario sobre un Google Dork.
    """

    def __init__(self, model = "orca-mini-3b-gguf2-q4_0.gguf"):
        """
        Función constructora, inicializa los atributos de instancia.

        Args:
            model(str): Consta del módelo de IA elegido por el usuario. Por defecto, orca-mini-3b-gguf2-q4_0.gguf.
        """

        self.model = GPT4All(model, device = "cpu")

    def generate_gdork(self,description):
        """
        Método encargado de lanzar el prompt y recoger el resultado otorgado por GPT4All.

        Args:
            description(str): Descripción otorgada por el usuario a la hora de querer generar un Google Dork.
        """

        # Construimos el prompt
        
        prompt = self._build_prompt(description)
        
        try:
            output = self.model.generate(prompt)
        except Exception as e:
            print(f"Error al generar el Google Dork: {e}")
        
        return output

    def _build_prompt(self,description):
        """
        Método encargado de adjuntar una descripción a la IA en base a una introducción previa.

        Args:
            description(str): Descripción otorgada por el usuario a la hora de querer generar un Google Dork.
        """
        
        return f"""

        Genera un Google Dork específico basado en la descripción del usuario. Un Google Dork utiliza operadores avanzados en motores de búsqueda para encontrar información específica que es difícil de encontrar mediante una búsqueda normal. Tu tarea es convertir la descripción del usuario en un Google Dork preciso. A continuación, se presentan algunos ejemplos de cómo deberías formular los Google Dorks basándote en diferentes descripciones:



        Descripción: Documentos PDF relacionados con la seguridad informática publicados en el último año.

        Google Dork: filetype:pdf "seguridad informática" after:2023-01-01



        Descripción: Presentaciones de Powerpoint sobre cambio climático disponibles en sitios .edu.

        Google Dork: site:.edu filetype:ppt "cambio climático"



        Descripción: Listas de correos electrónicos en archivos de texto dentro de dominios gubernamentales.

        Google Dork: site:.gov filetype:txt "email" | "correo electrónico"



        Ahora, basado en la siguiente descripción proporcionada por el usuario, genera el Google Dork correspondiente:



        Descripción: {description}

        """
