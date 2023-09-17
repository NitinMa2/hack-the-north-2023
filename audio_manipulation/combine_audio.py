from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip


def combine_audio(sound_file_1, sound_file_2):
    sound1 = AudioFileClip(sound_file_1)
    sound2 = AudioFileClip(sound_file_2)

    return CompositeAudioClip([sound1, sound2.set_start(0)])


def save_combined_audio(composite_audio_clip, destination_file):
    composite_audio_clip.write_audiofile(destination_file, fps =16000)
