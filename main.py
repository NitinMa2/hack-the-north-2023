import os
import mediapipe as mp
import cv2
import body_tracker
import lyrics
import text_to_speech
from audio_manipulation.auto_tune import *
from audio_manipulation.combine_audio import *
 

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# ------ do pose tracking -------
model_path = './models/pose_landmarker_heavy.task'

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=body_tracker.image_process_callback)

cap_cam = cv2.VideoCapture(0)
cap_cam.set(cv2.CAP_PROP_POS_MSEC, 0)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

with PoseLandmarker.create_from_options(options) as landmarker:

  for i in range(820):
    ret, frame = cap_cam.read()

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    landmarker.detect_async(mp_image, int(cap_cam.get(cv2.CAP_PROP_POS_MSEC)))

    annotated_image = body_tracker.draw_landmarks_on_image(frame, body_tracker.latest_result)
    out.write(frame)
    # cv2.imshow('frame', annotated_image)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  out.release()
  cv2.destroyWindow('frame')

  print(">>>>>>>>>>>>>>>>>>>>>>")
  print("Generating your song...")
  print('<<<<<<<<<<<<<<<<<<<<<<')

  #retrieve body position parameters for lyrics generation
  actions = body_tracker.process_positional_data()

  #generate lyrics
  song = lyrics.lyrics_generation(actions)

  #convert lyrics to speech
  text_to_speech.text_to_speech(song, play_sound=False)

  # Call the autotune function and save the result
  pitch_corrected_y, sr, filepath = get_autotune_result("text_to_speech_output.mp3", "scale", "C:min")
  save_autotune_result(pitch_corrected_y, sr, filepath, "_autotuned")

  # Combine soundtrack with lyrics audio
  x = combine_audio("text_to_speech_output_autotuned.mp3", "./audio_manipulation/guitar_soundtrack.mp3")

  # Combine video with audio
  movie_plus_audio("output.mp4", x)

  # play the final video
  os.startfile("final_video.mp4")
