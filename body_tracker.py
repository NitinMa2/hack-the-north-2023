import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
import math

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

  pose_landmarks_list = result.pose_landmarks

  if (len(pose_landmarks_list) == 0):
    return

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

def process_positional_data():
  global stored_positions

  actions = []
  node_speed_scaling = 100
  fast_speed_threshold = 5

  num_positions = len(stored_positions[0])
  
  # calc average speed of all nodes
  average_node_speed = 0
  for i in range(num_positions-1):
    delta_pos_list = [math.sqrt(
        (stored_positions[j][i-1].x - stored_positions[j][i].x)**2 + (stored_positions[j][i-1].y - stored_positions[j][i].y)**2
        ) for j in range(5)]
    average_node_speed += sum(delta_pos_list)/5
  average_node_speed /= num_positions-1
  average_node_speed *= node_speed_scaling

  print(average_node_speed)

  if(average_node_speed >= fast_speed_threshold):
    actions.append("fast")
  else:
    actions.append("slow")

  
  l_hand_over_shoulder_fc = 0
  l_hand_over_shoulder_max = 0

  r_hand_over_shoulder_fc = 0
  r_hand_over_shoulder_max = 0

  l_hand_past_head_fc = 0
  l_hand_past_head_max = 0

  r_hand_past_head_fc = 0
  r_hand_past_head_max = 0

  # get positions of key points
  for i in range(num_positions):
    head_pos = (stored_positions[0][i].x, stored_positions[0][i].y)
    l_shoulder_pos = (stored_positions[1][i].x, stored_positions[1][i].y)
    r_shoulder_pos = (stored_positions[2][i].x, stored_positions[2][i].y)
    l_hand_pos = (stored_positions[3][i].x, stored_positions[3][i].y)
    r_hand_pos = (stored_positions[4][i].x, stored_positions[4][i].y)
    
    # hands over shoulder level
    if l_hand_pos[1] <= l_shoulder_pos[1]:
      l_hand_over_shoulder_fc += 1
    else:
      l_hand_over_shoulder_max = max(l_hand_over_shoulder_max, l_hand_over_shoulder_fc)
      l_hand_over_shoulder_fc = 0

    if r_hand_pos[1] <= r_shoulder_pos[1]:
      r_hand_over_shoulder_fc += 1
    else:
      r_hand_over_shoulder_max = max(r_hand_over_shoulder_max, r_hand_over_shoulder_fc)
      r_hand_over_shoulder_fc = 0

    # hands past head vertical
    if l_hand_pos[0] >= head_pos[0]:
      l_hand_past_head_fc += 1
    else:
      l_hand_past_head_max = max(l_hand_past_head_max, l_hand_past_head_fc)
      l_hand_past_head_fc = 0

    if r_hand_pos[0] <= head_pos[0]:
      r_hand_past_head_fc += 1
    else:
      r_hand_past_head_max = max(r_hand_past_head_max, r_hand_past_head_fc)
      r_hand_past_head_fc = 0


  if(l_hand_over_shoulder_max >= 10):
    actions.append("left hand over shoulder")
  
  if(r_hand_over_shoulder_max >= 10):
    actions.append("right hand over shoulder")

  if(l_hand_past_head_max >= 10):
    actions.append("left hand past head")
  
  if(r_hand_past_head_max >= 10):
    actions.append("right hand past head")



  print(actions)


  plt.plot([i.x for i in stored_positions[0]], [i.y for i in stored_positions[0]])
  plt.plot([i.x for i in stored_positions[1]], [i.y for i in stored_positions[1]])
  plt.plot([i.x for i in stored_positions[2]], [i.y for i in stored_positions[2]])
  plt.plot([i.x for i in stored_positions[3]], [i.y for i in stored_positions[3]])
  plt.plot([i.x for i in stored_positions[4]], [i.y for i in stored_positions[4]])
  plt.show()

  return actions
  
