# Audio and Video Generation Script

This Python script allows you to generate audio (speech) and video content from text and image files. It leverages **Coqui AI** for text-to-speech (TTS) and **MoviePy** for video generation. Users can choose whether to generate audio, video, or both from files stored in separate folders.

## Features

- **Expressive Text-to-Speech (TTS)**: Converts `.txt` files into speech (audio) files with improved intonation and liveliness.
- **Text-to-Video**: Generates videos by overlaying text on a screen, synchronized with the generated speech.
- **Image-to-Video**: Converts images into videos with the generated speech as background audio.
- **Automatic Video Merging**: Combines generated videos into a single final video with smooth transitions.

## Installation

### Prerequisites

- **Python 3.10 or higher** is required for this script.
- **Coqui TTS** for text-to-speech conversion.
- **MoviePy** for video creation.
- **eSpeak-NG** (or **eSpeak**) for phoneme processing in Coqui TTS.
- **ImageMagick** for advanced text rendering in MoviePy.

### Step 1: Clone the Repository

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MykosX/audio-video-generation.git
   cd audio-video-generation
   ```

### Step 2: Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:
   
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Step 3: Install Required Dependencies

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install eSpeak-NG for Coqui TTS:**
   - **Windows**:
     1. Download and install [eSpeak-NG](https://espeak-ng.org/download.html).
     2. Add its path (`C:\Program Files\eSpeak NG`) to **Environment Variables**:
        ```cmd
        setx PATH "%PATH%;C:\Program Files\eSpeak NG"
        ```
   - **Linux (Ubuntu/Debian):**
     ```bash
     sudo apt update
     sudo apt install espeak-ng
     ```
   - **MacOS:**
     ```bash
     brew install espeak
     ```

3. **Install ImageMagick for MoviePy (Required for Text Rendering):**
   - **Windows**:
     1. Download and install [ImageMagick](https://imagemagick.org/script/download.php).
     2. During installation, check the box **"Install legacy utilities (convert)"**.
     3. Add its path to **Environment Variables** if not done automatically.
   - **Linux (Ubuntu/Debian):**
     ```bash
     sudo apt update
     sudo apt install imagemagick
     ```
   - **MacOS:**
     ```bash
     brew install imagemagick
     ```

4. Verify installations:
   ```bash
   espeak-ng --version
   convert --version  # ImageMagick verification
   ```

### Step 4: Folder Structure

Ensure the following folder structure exists in your project:

```
audio-video-generation/
│
├── input/text/             # Folder containing text files for speech generation
├── input/text/             # Folder containing text files for video generation (text overlay)
├── input/image/            # Folder containing image files for image-to-video generation
│
├── output/speech/          # Output folder for speech (.wav files)
├── output/video/           # Output folder for video files (.mp4)
├── output/                 # Folder for final merged video
```

### Step 5: Running the Script

1. **Generate Expressive Audio:**
   ```bash
   python generate_audio.py
   ```

2. **Generate Videos:**
   ```bash
   python generate_video.py
   ```

3. **Merge Videos into a Final Video:**
   ```bash
   python combine_videos.py
   ```

### Output

- **Speech**: The generated speech files (in `.wav` format) will be saved in the `speech/` folder.
- **Video**: The generated video files (in `.mp4` format) will be saved in the `video/` folder.
- **Final Merged Video**: The final compiled video will be saved in `final_video/` as `final_video.mp4`.

## How the Script Works

### 1. Expressive Text-to-Speech
The script reads `.txt` files from `input/text/` and generates speech files (`.wav`) with improved intonation, adjusted speed, and energy for a livelier voice.

### 2. Text-to-Video
The script overlays text from `input/text/` on a video, synchronizing it with the generated speech audio.

### 3. Image-to-Video
The script generates videos from images in `input/image/`, syncing them with the corresponding speech audio.

### 4. Video Merging with Transitions
The generated videos are merged into a single final video with **1-second black screen transitions** between them for smooth playback.

## Dependencies

The script uses the following libraries:

- **Coqui TTS**: Text-to-speech conversion with expressive voice parameters.
- **MoviePy**: Video editing and generation.
- **eSpeak-NG**: Required for Coqui TTS phoneme processing.
- **ImageMagick**: Required for proper text rendering in MoviePy.
  
Install all dependencies via:
```bash
pip install -r requirements.txt
```

`requirements.txt` should include:
```
wheel
TTS
moviepy
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this repository, submit issues, or open pull requests. If you have improvements or bug fixes, feel free to contribute!
