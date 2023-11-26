import os
from dotenv import load_dotenv
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Load .env file
load_dotenv('.env')

TTS_API_KEY = os.getenv('TTS_API_KEY')
TTS_URL = os.getenv('TTS_URL')

authenticator = IAMAuthenticator(TTS_API_KEY)
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url(TTS_URL)

def TTS_convertor(text, output_audio_file):
    with open(output_audio_file, 'wb') as audio_file:
        response = text_to_speech.synthesize(
            text,
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'
        ).get_result()
        audio_file.write(response.content)
