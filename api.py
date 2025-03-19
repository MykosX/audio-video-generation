import os
import torch
from TTS.api import TTS
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip, VideoFileClip, concatenate_videoclips

class Utils:
    @staticmethod
    def ensure_folder_exists(folder):
        """Ensure a folder exists, create it if not."""
        os.makedirs(folder, exist_ok=True)

    @staticmethod
    def choose_language():
        """Prompt user to choose a language."""
        print("Choose language:\n1 - English\n2 - Romanian")
        choice = input("Enter choice (1 or 2): ")
        if choice == "2":
            return "ro", "tts_models/ro/cv/vits", "romanian_speaker"
        return "en", "tts_models/en/ljspeech/vits", "english_speaker"

class AudioGenerator:
    def __init__(self):
        self.lang, self.tts_model, self.speaker = Utils.choose_language()
        self.tts = TTS(model_name=self.tts_model, gpu=False)

    def generate_speech(self, text_filepath, speech_filepath, index):
        """Generate speech from a text file."""
        with open(text_filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        
        kwargs = {"text": text, "file_path": speech_filepath, "speed": 1.2, "energy": 1.1}
        #if self.lang != "ro":
        #    kwargs["speaker"] = self.speaker
        kwargs["speaker"] = None
        
        self.tts.tts_to_file(**kwargs)

class ImageProcessor:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to(device)

    def generate_image_from_text(self, text_filepath, image_filepath):
        """Generate an image from a text file."""
        with open(text_filepath, 'r', encoding='utf-8') as file:
            prompt = file.read().strip()
        
        image = self.pipe(prompt).images[0]
        image.save(image_filepath)

    def modify_existing_image(self, image_filepath, text_filepath, output_filepath):
        """Modify an existing image by overlaying text from a text file."""
        with open(text_filepath, 'r', encoding='utf-8') as file:
            text = file.read().strip()
        
        image = Image.open(image_filepath)
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((10, 10), text, fill="white", font=font)
        
        image.save(output_filepath)
        print(f"Modified image saved at {output_path}")

class VideoGenerator:
    def generate_video_from_image(self, image_filepath, speech_filepath, video_filepath, index, lang):
        """Create a video from an image with speech overlay."""
        img_clip = ImageClip(image_filepath).set_duration(5)
        audio_clip = AudioFileClip(speech_filepath)
        
        video = img_clip.set_audio(audio_clip)
        video.write_videofile(video_filepath, fps=60)
        print(f"Video saved as {video_filepath}")
    
    def combine_videos(self, video_folder, output_file):
        """Combine all video clips in a folder."""
        video_files = sorted([os.path.join(video_folder, f) for f in os.listdir(video_folder) if f.endswith('.mp4')])
        
        if not video_files:
            print("No videos found to merge.")
            return
        
        clips = [VideoFileClip(f) for f in video_files]
        final_clip = concatenate_videoclips(clips, method='compose')
        final_clip.write_videofile(output_file, fps=60, codec='libx264')
        print(f"Final video saved as {output_file}")
