from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url = 'https://openrouter.ai/api/v1',
    api_key = OPENAI_API_KEY,
)

def main(input_text):

    data_schema = {
        "id": "str",
        "name": "str",
        "email": "str",
        "age": "int",
        "gender": "str",
        "location": "str",
        "segment": "str",
        "acquisition_channel": "str",
        "sign_up_date": "str",
        "last_interaction": "str",
        "products_purchased": "list",
        "month_of_purchase": "str",
    }
    
    try:
        completion = client.chat.completions.create(
            model = "deepseek/deepseek-r1:free",
            messages = [
                {
                    "role": "system", "Content": f"You are a provider of random dummy marketing data in json file following the given format: {data_schema}.",
                },
                {
                    "role": "user", "content": "Generate json dummy marketing data for super-mart",
                }
            ],
            extra_headers = {
                "HTTP-Referer": "https://openrouter.ai", # any valid referer
                "X-Title": "OpenRouter Example", # any valid title
            }
        )

        print(completion.choices[0].message.content)

    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    input_text = input("Enter your text: ")
    main(input_text)