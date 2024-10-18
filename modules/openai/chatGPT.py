from modules.openai.openai_client import get_openai_api_client
from utils.constants import SYSTEM_ROLE


class chatGPT():
    def __init__(self) -> None:
        self.client = get_openai_api_client()

    def make_request(self, input_text:str, current_code:str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": SYSTEM_ROLE
                },
                {
                    "role": "user", 
                    "content": f"I need you to make the specified changes:{input_text}\nApply this on the current code{current_code}"
                }
            ]
        )
        return completion.choices[0].message.content
    
    def generate_image(self, prompt: str) -> str:
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        return image_url

