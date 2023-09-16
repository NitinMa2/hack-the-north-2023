import mediapipe as mp
import cv2
import body_tracker

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = './models/pose_landmarker_heavy.task'

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=body_tracker.print_result)

cap_cam = cv2.VideoCapture(0)
cap_cam.set(cv2.CAP_PROP_POS_MSEC, 0)

with PoseLandmarker.create_from_options(options) as landmarker:

  while True:
    ret, frame = cap_cam.read()

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    landmarker.detect_async(mp_image, int(cap_cam.get(cv2.CAP_PROP_POS_MSEC)))

    annotated_image = body_tracker.draw_landmarks_on_image(frame, body_tracker.latest_result)

    cv2.imshow('frame', annotated_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
  cv2.destroyWindow('frame')