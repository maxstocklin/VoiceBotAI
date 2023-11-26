from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv('.env')

STT_API_KEY = os.getenv('STT_API_KEY')
STT_URL = os.getenv('STT_URL')

authenticator = IAMAuthenticator(STT_API_KEY)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(STT_URL)

def STT_convertor(recording_file):
	with open(recording_file, 'rb') as audio_file:
		audio = audio_file.read()

	response = speech_to_text.recognize(
		audio=audio,
		content_type='audio/mp3'
	).get_result()

	transcription = response['results'][0]['alternatives'][0]['transcript']
