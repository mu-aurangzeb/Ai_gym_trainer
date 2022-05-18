from gc import get_count
from itertools import count
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
    stage = None
    
    def get_count(self,count=counter):
        return self.counter
    def set_count(self,count=counter):
        self.counter=self.counter+1
        return self.counter

    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self,pose=pose,mpDraw=mpDraw,mpPose=mpPose,counter=counter,stage=stage):
        success, image = self.video.read()
        count1=1
        stage1=None
    
        # ret, frame = self.cap.read()
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        #count=counter
        # landmarks = results.pose_landmarks.landmark
        image.flags.writeable = True
        landmarks = results.pose_landmarks.landmark


        def calculate_angle(a,b,c):
            a = np.array(a) # First
            b = np.array(b) # Mid
            c = np.array(c) # End
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
            if angle >180.0:
                angle = 360-angle
            return angle 
        
       
        
    

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
        shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].y]

        #print(calculate_angle(shoulder, elbow, wrist))
        anglee=calculate_angle(shoulder, elbow, wrist)
        print(anglee)


        if (int(anglee) > 155):
            print("down",self.stage)
            self.stage = "down"
        if ((int(anglee) < 30) and (self.stage =='down')):
            self.stage="up"
            self.counter+=1
            print("up",self.stage)

            print("Countttttt", self.counter)


        frame = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        frame_flip = cv2.flip(frame, 1)
        cv2.rectangle(frame_flip, (0,0), (225,73), (245,117,16), -1)
        # Visualize angle
        cv2.putText(frame_flip, str(calculate_angle(shoulder, elbow, wrist)), 
                           tuple(np.multiply(elbow, [50, 250]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
        


        


        cv2.putText(frame_flip, 'REPS', (15,12),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(frame_flip, str(self.counter), 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
       

       
   
        ret, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()