from gpt4all import GPT4All
import os
from openai import OpenAI
from dotenv import load_dotenv

class GPT4ALLGenerator():
    def __init__(self,model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"):
        self.model = GPT4All(model_name, device = "cpu")

    def generate(self,prompt):
        return self.model.generate(prompt)
    
class OPENAIGenerator:
    def __init__(self,model_name = "gpt-4"):
        self.model_name = model_name
        self.client = OpenAI()

    def generate(self,prompt):
        client= OpenAI(
        api_key= os.getenv("OPENAI_API_KEY")
        )

        chat_completion = client.chat.completions.create(
        messages = {
            "role": "user",
            "content": "Cual es la capital de Francia?"
        },
        model = "gpt-4",
        )
        return chat_completion.choices[0].message.content
    
class IAAgent:

    def __init__(self, generator):
        self.generator = generator
    def generate_gdork(self,description):
        # Construimos el prompt
        prompt = self._build_prompt(description)
        try:
            output = self.generator.generate(prompt)
            return output
        except Exception as e:
            print(f"Error al generar el Google Dork: {e}")
    def _build_prompt(self,description):
        return f"""
        {description}
        """

if __name__ == "__main__":
    description = "Lista de usuarios y contraseñas"
    ia_agent = IAAgent()
    ia_agent.generate_gdork(description)


