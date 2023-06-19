from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    try:
        # Sending a request to the ChatGPT API
        response = openai.ChatCompletion.create(
            engine="gpt-3.5-turbo",  # Specify the model
            prompt=prompt,           # Input text
            temperature=0.7,         # Controls randomness: Higher values (closer to 1) make output more random, lower values make it more focused
            max_tokens=50            # Limit the length of the output text
        )
        
        # Extracting the text from the response
        return response.choices[0].text

    except Exception as e:
        error_str = f"An error occurred: {e}"
        # print(error_str)
        return error_str
