import cv2
import numpy as np
import mediapipe as mp
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
class VideoCamera(object):
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    mpDraw = mp.solutions.drawing_utils
    counter = 0 

    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self,pose=pose,mpDraw=mpDraw,mpPose=mpPose,counter=counter):
        success, image = self.video.read()

        # ret, frame = self.cap.read()
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        print(results.pose_landmarks)
        count=counter
        
        

        # if results.pose_landmarks:
        #     mpDraw.draw_landmarks(image=imgRGB, landmark_list=results.pose_landmarks,
        #                           connections=mpPose.POSE_CONNECTIONS,
        #                           landmark_drawing_spec=mpDraw.DrawingSpec(color=(255,255,255),
        #                                                                        thickness=3, circle_radius=3),
        #                           connection_drawing_spec=mpDraw.DrawingSpec(color=(49,125,237),
        #                                                                        thickness=2, circle_radius=2))
        mpDraw.draw_landmarks(imgRGB, results.pose_landmarks, mpPose.POSE_CONNECTIONS,
                                mpDraw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mpDraw.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )


        frame = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        frame_flip = cv2.flip(frame, 1)
        cv2.rectangle(frame_flip, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(frame_flip, 'REPS', (15,12),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(frame_flip, str(count), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        ret, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()