import os
from api import AudioGenerator, ImageProcessor, VideoGenerator, Utils

class Generator:
    def __init__(self):
        self.audio_gen = AudioGenerator()
        self.image_proc = ImageProcessor()
        self.video_gen = VideoGenerator()
        
        # Input directories
        self.text_input = "input/text"
        self.image_input = "input/image"
        
        # Output directories
        self.speech_output = "output/speech"
        self.image_output = "output/image"
        self.video_output = "output/video"
        self.merged_video_filepath = "output/final.mp4"
    
    def process_audio(self):
        """Make sure output folder exists."""
        Utils.ensure_folder_exists(self.speech_output)
        
        text_files = sorted([f for f in os.listdir(self.text_input) if f.endswith('.txt')])
        
        for i, text_file in enumerate(text_files):
            text_filepath = os.path.join(self.text_input, text_file)
            speech_filepath = os.path.join(self.speech_output, os.path.splitext(text_file)[0] + ".wav")
            
            self.audio_gen.generate_speech(
                text_filepath, speech_filepath, i
            )
            print(f"Generated {self.audio_gen.lang.upper()} audio for {text_file} using {self.audio_gen.speaker}: {speech_filepath}")
    
    def process_images(self):
        """Make sure output folder exists."""
        Utils.ensure_folder_exists(self.image_output)
        
        text_files = sorted([f for f in os.listdir(self.text_input) if f.endswith('.txt')])
        
        for i, text_file in enumerate(text_files):
            text_filepath = os.path.join(self.text_input, text_file)
            image_filepath = os.path.join(self.image_output, os.path.splitext(text_file)[0] + ".png")
            
            self.image_proc.generate_image_from_text(
                text_filepath, image_filepath
            )
            print(f"Generated image from text file: {text_file} to {image_filepath}")
    
    def process_videos(self):
        """Make sure output folder exists."""
        Utils.ensure_folder_exists(self.speech_output)
        Utils.ensure_folder_exists(self.video_output)
        
        text_files = sorted([f for f in os.listdir(self.text_input) if f.endswith('.txt')])
        image_files = sorted([f for f in os.listdir(self.image_input) if f.endswith(('.png', '.jpg', '.jpeg'))])
        
        for i, (text_file, image_file) in enumerate(zip(text_files, image_files)):
            text_filepath = os.path.join(self.text_input, text_file)
            speech_filepath = os.path.join(self.speech_output, os.path.splitext(text_file)[0] + ".wav")
            
            self.audio_gen.generate_speech(
                text_filepath, speech_filepath, i
            )
            print(f"Generated audio for {text_file}")
            
            image_filepath = os.path.join(self.image_input, image_file)
            video_filepath = os.path.join(self.video_output, os.path.splitext(text_file)[0] + ".mp4")
            
            self.video_gen.generate_video_from_image(
                image_filepath, speech_filepath, video_filepath, i, self.audio_gen.lang
            )
            print(f"Generated video from {image_file}")
    
    def merge_videos(self):
        self.video_gen.combine_videos(self.video_output, self.merged_video_filepath)

def main():
    generator = Generator()
    
    print("Choose operations (bitwise):")
    print("1 - Audio Processing")
    print("2 - Image Processing")
    print("4 - Video Processing")
    choice = int(input("Enter your choice (sum for multiple): "))
    
    if choice & 1:
        generator.process_audio()
    if choice & 2:
        generator.process_images()
    if choice & 4:
        generator.process_videos()
        generator.merge_videos()
    
if __name__ == "__main__":
    main()
