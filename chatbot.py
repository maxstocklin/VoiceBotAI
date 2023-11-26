
from openai import OpenAI
import os
import sys

from dotenv import load_dotenv
from speech_to_text import STT_convertor
from text_to_speech import TTS_convertor

load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def main():
	if len(sys.argv) != 2:
		print("Usage: python test.py <filename>")
		sys.exit(1)

	filename = sys.argv[1]
	print(f"Processing file: {filename}")
	print('Step 1: Speech to Text')
	transcription = STT_convertor(filename)
	print(transcription)

	print('Step 2: Chatbot')
	client = OpenAI(
	api_key=OPENAI_API_KEY,
	)

	completion = client.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=[
		{"role": "system", "content": "You are an Assistant named Stan and you are acting friendly. Tell them a joke if nothing is specified."},
		{"role": "user", "content": f"{transcription}"}
	],
	max_tokens=3000,
	temperature=0.7,  # Adjust for creativity
	stop=["\n"],  # Stops on a new line
	frequency_penalty=0.5,  # Adjust to reduce repetition
	presence_penalty=0.5  # Adjust to encourage diversity
	)

	chatbot_response = completion.choices[0].message.content
	print(chatbot_response)

	print('Step 3: Text to Speech')
	TTS_convertor(chatbot_response, "output_weather.mp3")
if __name__ == "__main__":
	main()
