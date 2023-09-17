from gtts import gTTS
import os
import playsound
import uuid

def text_to_speech(text, output_dir='.', language='en', play_sound=False):
    """
    Convert text to speech and save it as an mp3 file.

    Parameters:
    - text (str): The text to be converted.
    - output_dir (str): The directory where the MP3 file will be saved.
    - language (str): The language in which you want to convert.
    - play_sound (bool): Whether or not to play the sound after generating it.

    Returns:
    str: The path of the generated MP3 file.
    """
    # Create a unique filename
    filename = "text_to_speech_output.mp3"
    file_path = os.path.join(output_dir, filename)

    # Convert text to speech
    tts_engine = gTTS(text=text, lang=language, slow=False)
    tts_engine.save(file_path)

    # Optionally play the sound
    if play_sound:
        playsound.playsound(file_path)

    return file_path