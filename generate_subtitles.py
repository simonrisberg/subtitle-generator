import os
from moviepy import VideoFileClip
import whisper
import srt
from datetime import timedelta

def extract_audio(video_path, audio_path):
    """Extract audio from a video file."""
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()

def transcribe_audio(audio_path):
    """Transcribe audio to text using OpenAI's Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["segments"]

def create_srt(segments, output_path):
    """Generate an SRT file from transcribed segments."""
    if os.path.isdir(output_path):
        raise ValueError(f"The output path '{output_path}' is a directory. Please provide a valid .srt file path.")
    
    srt_subs = []
    for i, segment in enumerate(segments):
        start = timedelta(seconds=segment["start"])
        end = timedelta(seconds=segment["end"])
        content = segment["text"]
        srt_subs.append(srt.Subtitle(index=i+1, start=start, end=end, content=content))
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(srt_subs))

def process_video(video_path):
    """Process a single video file to generate subtitles."""
    audio_path = "temp_audio.wav"
    output_srt_path = os.path.splitext(video_path)[0] + ".srt"
    
    # Check if the corresponding .srt file already exists
    if os.path.exists(output_srt_path):
        print(f"Skipping {video_path} as {output_srt_path} already exists.")
        return
    
    try:
        # Step 1: Extract audio
        print(f"Processing {video_path}...")
        extract_audio(video_path, audio_path)

        # Step 2: Transcribe audio
        print("Transcribing audio...")
        segments = transcribe_audio(audio_path)

        # Step 3: Generate SRT
        print(f"Generating subtitles for {video_path}...")
        create_srt(segments, output_srt_path)
        print(f"Subtitles saved to {output_srt_path}")
    finally:
        # Clean up temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

def main():
    # Get the current directory
    current_folder = os.getcwd()
    print(f"Scanning folder: {current_folder}")

    # Find all .flv, .mp4, and .mkv files in the folder
    supported_extensions = (".flv", ".mp4", ".mkv")
    video_files = [f for f in os.listdir(current_folder) if f.endswith(supported_extensions)]
    
    if not video_files:
        print("No supported video files (.flv, .mp4, .mkv) found in the current folder.")
        return

    print(f"Found {len(video_files)} supported video file(s):")
    for f in video_files:
        print(f" - {f}")

    # Process each video file
    for video_file in video_files:
        try:
            process_video(video_file)
        except Exception as e:
            print(f"Error processing {video_file}: {e}")

if __name__ == "__main__":
    main()
