import cv2
import numpy as np
import mediapipe as mp
import os
from imutils.video import VideoStream
import imutils
import pickle
import cv2,os,urllib.request

class VideoCamera_butterfly(object):
     
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    mpDraw = mp.solutions.drawing_utils
    counter = 0
    stage = None
    position=None


    def __init__(self):
        #self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture('http://192.168.147.196:5000/video')
        #self.url = "http://192.168.147.196:5000/video"

    # def __del__(self):
    #     self.video.release()
    def get_frame(self,pose=pose,mpDraw=mpDraw,mpPose=mpPose,counter=counter,stage=stage):
        success, image = self.video.read()
       
        image= cv2.flip(image, 0)
        
    
        # ret, frame = self.cap.read()
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #imgRGB=cv2.flip(imgRGB, 0)
        results = pose.process(imgRGB)
        #count=counter
        #landmarkss = results.pose_landmarks.landmark
        image.flags.writeable = True
        #landmarks = results.pose_landmarks.landmark
        


        def calculate_angle(a,b,c):
            a = np.array(a) # First
            b = np.array(b) # Mid
            c = np.array(c) # End
            radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = float(np.abs(radians*180.0/np.pi))
            if (float(angle) > 180.0):
                angle = 360-angle
            return angle 
        
        

        mpDraw.draw_landmarks(imgRGB, results.pose_landmarks, mpPose.POSE_CONNECTIONS,
                                mpDraw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mpDraw.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )
        if not results.pose_landmarks:
            no_results_found="no results found"
            print("no results found")
            right_shoulder_angle=0
            left_shoulder_angle=0
            position="no results found"
            angle=0
            #shoulder=0
            #elbow=0
            #wrist=0
        else: 
            landmarks = results.pose_landmarks.landmark

            right_shoulder = [landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_elbow = [landmarks[mpPose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mpPose.PoseLandmark.RIGHT_ELBOW.value].y]
            right_hip = [landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].y]
    
            
            left_shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]
            left_hip = [landmarks[mpPose.PoseLandmark.LEFT_HIP.value].x,landmarks[mpPose.PoseLandmark.LEFT_HIP.value].y]
           
        
            right_shoulder_angle=calculate_angle(right_elbow,right_shoulder, right_hip)
            left_shoulder_angle=calculate_angle(left_elbow,left_shoulder , left_hip)
            
            right_elbow_angle=calculate_angle(right_shoulder, right_elbow, right_hip)
            left_elboe_angle=calculate_angle(left_shoulder, left_elbow, left_hip)


            if ( ((int(right_shoulder_angle)>65) and (int(right_shoulder_angle)<85)) and ((int(left_shoulder_angle)>65) and (int(left_shoulder_angle)<85)) ):
                #cv2.putText(imgRGB, 'shoulders is Right', (65,12),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                position="Shoulders are right"
            else:
                #cv2.putText(imgRGB, 'shoulders is  Wrong', (65,12),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50,60,260), 1, cv2.LINE_AA)
                position="shoulders are Wrong"

            



        frame = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        #frame_flip=frame
        frame_flip = cv2.flip(frame, 0)
        cv2.rectangle(frame_flip, (0,0), (225,73), (245,117,16), -1)      

        cv2.putText(frame_flip, str(position), (30,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (60,60,20), 2, cv2.LINE_AA)
        


        if right_shoulder_angle==0:
            cv2.putText(frame_flip, 'not visiable to camera', (150,120),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (10,10,10), 1, cv2.LINE_AA)
       

       
   
        ret, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()


