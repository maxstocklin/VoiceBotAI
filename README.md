# VoiceBotAI

This program provides a unique way to interact with a chatbot using voice commands. It integrates IBM Watson's Speech to Text and Text to Speech services with OpenAI's powerful GPT-3 model, allowing users to have a conversational experience entirely through voice.

Features

Speech to Text: Converts spoken language into text using IBM Watson's Speech to Text API.
ChatGPT Interaction: Processes the transcribed text through OpenAI's GPT-3 model to generate relevant responses.
Text to Speech: Converts the chatbot's text responses back into speech using IBM Watson's Text to Speech API.
Prerequisites

Before you start using this chatbot, you need to set up a few things:

An IBM Cloud account with Watson Speech to Text and Text to Speech services.
An OpenAI account with access to the GPT-3 API.
Python 3.x installed on your system.
Make sure you have the necessary API keys and have installed the required Python packages (ibm-watson, openai, etc.).

Installation

Clone this repository or download the source code.
Install the required dependencies:
sh
Copy code
pip install -r requirements.txt
Set your IBM and OpenAI API keys as environment variables:
sh
Copy code
export STT_API_KEY='your-ibm-speech-to-text-key'
export TTS_API_KEY='your-ibm-text-to-speech-key'
export OPENAI_API_KEY='your-openai-key'
Usage

To use the chatbot, run the script with the path to your audio file (e.g., .mp3):

sh
Copy code
python chatbot.py <soundfile_path>
Replace <soundfile_path> with the path to your audio file.

How It Works

Speech to Text: The program takes a sound file as input and uses IBM's Speech to Text API to transcribe the audio into text.
ChatGPT Interaction: The transcribed text is sent to OpenAI's ChatGPT, which generates a response.
Text to Speech: Finally, the chatbot's response is converted back into speech using IBM's Text to Speech API, completing the voice interaction loop.
Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make changes, and submit a pull request.

License

