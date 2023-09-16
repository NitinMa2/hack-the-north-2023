from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip

sound1 = AudioFileClip("mixkit-retro-game-emergency-alarm-1000.wav")
sound2 = AudioFileClip("mixkit-crickets-and-insects-in-the-wild-ambience-39.wav")

mixed = CompositeAudioClip([sound1, sound2.set_start(2)])
mixed.write_audiofile("mixed-output.mp3", fps =16000)
