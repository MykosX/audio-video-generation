import os
from moviepy.editor import *

# Folder paths
video_folder = 'output/video/'
output_folder = 'output/'
# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)
output_video = os.path.join(output_folder, 'final_video.mp4')

# Get all generated video files
video_files = [os.path.join(video_folder, f) for f in os.listdir(video_folder) if f.endswith('.mp4')]
video_files.sort()  # Ensure a consistent order

if not video_files:
    print("No videos found to merge.")
else:
    # Load video clips
    clips = [VideoFileClip(f) for f in video_files]
    
    # Concatenate clips
    final_clip = concatenate_videoclips(clips, method='compose')
    
    # Write the final video
    final_clip.write_videofile(output_video, fps=60, codec='libx264')
    
    print(f"Final video saved as {output_video}")
