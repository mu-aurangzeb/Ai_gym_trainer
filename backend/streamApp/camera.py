import cv2
import numpy as np
import mediapipe as mp

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def __del__(self):
        self.cap.release()
    def get_frame(self):
        mpPose = mp.solutions.pose
        pose = mpPose.Pose()
        mpDraw = mp.solutions.drawing_utils

        ret, frame = self.cap.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame=imgRGB
        results = pose.process(imgRGB)
        print(results.pose_landmarks)

        if results.pose_landmarks:
            mpDraw.draw_landmarks(image=imgRGB, landmark_list=results.pose_landmarks,
                                  connections=mpPose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mpDraw.DrawingSpec(color=(255,255,255),
                                                                               thickness=3, circle_radius=3),
                                  connection_drawing_spec=mpDraw.DrawingSpec(color=(49,125,237),
                                                                               thickness=2, circle_radius=2))




        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame_flip = cv2.flip(frame, 1)
        ret, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()