from dotenv import load_dotenv
import custom_openai
import os

load_dotenv()

custom_openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
	response = custom_openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		prompt=prompt,
		temperature=1,
		max_tokens=100	
	)
	response_dict = response.get("choise")
	if response_dict and len(response_dict) > 0:
		prompt_response = response_dict[0]["text"]
	return prompt_response