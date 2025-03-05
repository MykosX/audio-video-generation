import os
from TTS.api import TTS

# Initialize Coqui AI with a more expressive model
tts = TTS(model_name="tts_models/en/ljspeech/vits", gpu=False)

# Folder paths
text_to_speech_folder = 'input/text/'
speech_folder = 'output/speech/'

# Make sure output folder exists
os.makedirs(speech_folder, exist_ok=True)

# Function to generate speech from text with adjusted parameters
def generate_speech(text_file, i):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    speech_filename = f"speech_{i+1}.wav"
    speech_filepath = os.path.join(speech_folder, speech_filename)
    
    # Generate speech with modifications
    tts.tts_to_file(text=text, file_path=speech_filepath, speed=1.2, energy=1.1)
    return speech_filepath

# Main function to process the text-to-speech files
def generate_audio():
    text_to_speech_files = [f for f in os.listdir(text_to_speech_folder) if f.endswith('.txt')]

    for i, text_file in enumerate(text_to_speech_files):
        speech_filepath = generate_speech(os.path.join(text_to_speech_folder, text_file), i)
        print(f"Generated expressive audio for {text_file}: {speech_filepath}")

if __name__ == "__main__":
    generate_audio()
