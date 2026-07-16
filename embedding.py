from dotenv import load_dotenv
import os
load_dotenv()
oa_api_key = os.getenv("OA_API_KEY")

class Embedding:
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Initialize the embedding model here (e.g., load a pre-trained model)

    def embed(self, text: str):
        # Implement the embedding logic here
        # For example, convert the text into a vector representation
        pass