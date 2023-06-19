from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    try:
        # Sending a request to the ChatGPT API
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}],
            temperature = 0.7,
            max_tokens=193
        )
        
        # Extracting the text from the response
        return response['choices'][0]['message']['content']

    except Exception as e:
        error_str = f"An error occurred: {e}"
        # print(error_str)
        return error_str
