import os
from moviepy.editor import *
from TTS.api import TTS

# Folder paths
text_to_video_folder = 'input/text/'
image_to_video_folder = 'input/image/'
speech_folder = 'output/speech/'
video_folder = 'output/video/'

# Make sure output folder exists
os.makedirs(video_folder, exist_ok=True)

# Function to generate video from text
def generate_video_from_text(text_file, speech_filepath, i):
    with open(text_file, 'r', encoding='utf-8') as file:
        video_text = file.read()

    video_filename = f"video_{i+1}_text.mp4"
    video_filepath = os.path.join(video_folder, video_filename)

    # Create video from text (using text as overlay)
    txt_clip = TextClip(video_text, fontsize=70, color='white').set_duration(5)
    audio_clip = AudioFileClip(speech_filepath)

    video = txt_clip.set_audio(audio_clip)
    video.write_videofile(video_filepath, fps=24)

# Function to generate video from image
def generate_video_from_image(image_file, speech_filepath, i):
    image_filepath = os.path.join(image_to_video_folder, image_file)
    img_clip = ImageClip(image_filepath).set_duration(5)  # 5 seconds per image

    video_filename = f"video_{i+1}_image.mp4"
    video_filepath = os.path.join(video_folder, video_filename)

    audio_clip = AudioFileClip(speech_filepath)

    video = img_clip.set_audio(audio_clip)
    video.write_videofile(video_filepath, fps=60)

# Main function to process the video generation
def generate_video():
    text_to_video_files = [f for f in os.listdir(text_to_video_folder) if f.endswith('.txt')]
    image_files = [f for f in os.listdir(image_to_video_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    speech_files = sorted([f for f in os.listdir(speech_folder) if f.endswith('.wav')])

    for i, speech_file in enumerate(speech_files):
        speech_filepath = os.path.join(speech_folder, speech_file)

        # Generate video from text if available
        #if i < len(text_to_video_files):
        #    generate_video_from_text(os.path.join(text_to_video_folder, text_to_video_files[i]), speech_filepath, i)

        # Generate video from image if available
        if i < len(image_files):
            generate_video_from_image(image_files[i], speech_filepath, i)

if __name__ == "__main__":
    generate_video()
