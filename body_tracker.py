import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

latest_result = None
stored_positions = [[] for i in range(5)] # head, L shoulder, R shoulder, L hand, R hand

# Create a pose landmarker instance with the live stream mode:
def print_result(result: PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global latest_result
    latest_result = result
    print('pose landmarker result: {}'.format(result))  

def draw_landmarks_on_image(rgb_image, detection_result):
  if detection_result == None:
     return rgb_image
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image

def image_process_callback(result: PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
  global latest_result, stored_positions
  latest_result = result
  print("process data")

  pose_landmarks_list = result.pose_landmarks

  print("process data")

  # head
  stored_positions[0].append(pose_landmarks_list[0][0])

  # L shoulder
  stored_positions[1].append(pose_landmarks_list[0][11])

  # R shoulder
  stored_positions[2].append(pose_landmarks_list[0][12])

  # L hand
  stored_positions[3].append(pose_landmarks_list[0][15])

  # R hand
  stored_positions[4].append(pose_landmarks_list[0][16])

  print("processed data")

def process_positional_data():
  global stored_positions

  plt.plot([i.x for i in stored_positions[0]], [i.y for i in stored_positions[0]])
  plt.show()
  
