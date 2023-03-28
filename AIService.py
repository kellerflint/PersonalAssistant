import openai
from Config import OPENAI_API_KEY

class AIService:
    def __init__(self):
        pass

    def getAIResponse(self, inputText):
        print(f"Getting AI response on: {inputText}.")
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": inputText}
            ]
        )
        if response.choices:
            return response.choices[0].message.content.strip()
        else:
            return None

