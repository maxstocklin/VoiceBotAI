# VoiceBotAI

# Voice-Interactive Chatbot

This program integrates IBM Watson's Speech to Text and Text to Speech services with OpenAI's GPT-3.5 model, providing a seamless voice-interactive chatbot experience.

## Features

- **Speech to Text:** Converts voice to text using IBM Watson's API.
- **ChatGPT Interaction:** Processes the text with OpenAI's GPT-3 to generate responses.
- **Text to Speech:** Converts the chatbot's text responses back into voice using IBM Watson's API.

## Prerequisites

- IBM Cloud account with Watson Speech to Text and Text to Speech services.
- OpenAI account with GPT-3 API access.
- Python 3.x.

Ensure you have the API keys for IBM Watson and OpenAI, and install the required Python packages.

## Installation

1. Clone or download this repository.
2. Edit Bash Profile:
   ```bash
   vim ~/.bash_profile
   ```
    or
   ```
   vim ~/.zshrc 
   ```
3. Set your API keys as environment variables:
   ```bash
    export STT_API_KEY='your-ibm-speech-to-text-key'
    export TTS_API_KEY='your-ibm-text-to-speech-key'
    export OPENAI_API_KEY='your-openai-key'
   ```
##Usage

Run the script with the path to your audio file:

   ```bash
    python chatbot.py <soundfile_path>
   ```
Replace <soundfile_path> with your audio file's path.


##How It Works
###Step 1: Speech to Text
Transcribes audio to text using IBM's API.
###Step 2: ChatGPT Interaction
Sends text to ChatGPT for response.
###Step 3: Text to Speech
Converts response to speech using IBM's API.

