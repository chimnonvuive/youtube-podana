# # Import the pytube library
from pytube import YouTube
import subprocess
import os

# Define a function to extract audio from a YouTube video
def extract_audio(link):
  # Create a YouTube object with the video link
  yt = YouTube(link)
  # Filter the streams to get only the audio ones
  audio_streams = yt.streams.filter(only_audio=True)
  # Choose the first audio stream (you can modify this to choose other criteria)
  audio_stream = audio_streams[0]
  # Download the audio stream to the current working directory
  audio_stream.download()
  # Return the file name of the downloaded audio
  return audio_stream.default_filename

# Test the function with an example video link
link = "https://www.youtube.com/watch?v=sdd4BST87ks"
file_name = extract_audio(link)
print(f"Audio file name: {file_name}")

file_path = os.path.dirname(os.path.realpath(file_name))
# # input_file = 'input.mp4'
# # output_file = 'output.wav'

command = "ffmpeg -i \"" + file_path + "\\" + file_name + "\" -ab 160k -ac  -ar 44100 -vn \"" \
            + file_path + "\\" + file_name.replace(".mp4",".wav") + "\""
 # ['ffmpeg', '-i', file_name,
 #           '-acodec', 'pcm_s16le', '-ar', '44100', file_name.replace(".mp4",".wav")]
subprocess.call(command, shell=True)