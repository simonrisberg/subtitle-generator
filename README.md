# Subtitle generator

This is a simple subtitle generator written in Python. It can handle generating subtitles for multiple file formats such as .mp4, .flv and .mkv

# Dependencies

## MoviePy

Used for stripping the audio from the video file

## OpenAI Whisper

Model used for transcribing the audio file into text with timestamps

## srt

Used for populating the .srt file with the newly extracted text and timestamps

# Install Prerequisites

Ensure that Python version 3.7 or older is installed. If not please [download Python](https://www.python.org/downloads/) and install it.

#### Install Required Libraries:

Run the following commands in your terminal or command prompt to install the necessary Python libraries:

`pip install moviepy whisper-openai srt`

#### Install FFmpeg:

`Moviepy` relies on FFmpeg to process video and audio files. Install FFmpeg using the instructions for your operating system:

##### Windows:

1. Download FFmpeg from [here](https://ffmpeg.org/download.html)
2. Extract the downloaded archive and add the `bin` folder to your system's PATH

##### MacOS:

`brew install ffmpeg`

##### Linux:

```
sudo apt update
sudo apt install ffmpeg
```

#### Verify installation:

`ffmpeg -version`

# Usage

1. Save the script in the folder where the video files are located
2. In your terminal, run `python generate_subtitles.py`
3. The script will automatically scan the folder for .mkv, .mp4 and .flv files and generate .srt file for each of them with the same name
