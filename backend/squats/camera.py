import cv2
import numpy as np
import mediapipe as mp
import os
from imutils.video import VideoStream
import imutils
import pickle
import cv2,os,urllib.request
class VideoCamera_squats(object):
     
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    mpDraw = mp.solutions.drawing_utils
    counter = 0
    stage = None
    position=None
    #pickled_model = pickle.load(open('static/streamApp/bicecp_fyp_model.pkl', 'rb'))
    #image12=load_img("static/img/first.jpg")
    #print("pickled_model",pickled_model)
    
    # def get_count(self,count=counter):
    #     return self.counter
    # def set_count(self,count=counter):
    #     self.counter=self.counter+1
    #     return self.counter


  


    def __init__(self):
        #self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture('http://192.168.147.196:5000/video')
        #self.url = "http://192.168.147.196:5000/video"

    # def __del__(self):
    #     self.video.release()
    def get_frame(self,pose=pose,mpDraw=mpDraw,mpPose=mpPose,counter=counter,stage=stage):
        success, image = self.video.read()
        count1=1
        stage1=None
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
            right_ankle= [0.0, 0.0]
            right_knee =[0.0, 0.0]
            right_hip =[0.0, 0.0]
            position="no results found"
            angle=0
            #shoulder=0
            #elbow=0
            #wrist=0
        else: 
            landmarks = results.pose_landmarks.landmark



            right_ankle = [landmarks[mpPose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mpPose.PoseLandmark.RIGHT_ANKLE.value].y]
            right_knee = [landmarks[mpPose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mpPose.PoseLandmark.RIGHT_KNEE.value].y]
            right_hip = [landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].y]
            
            shoulder = [landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].y]
            
            print("right_ankle",right_ankle)
            print("right_knee",right_knee)
            print("right_hip",right_hip)
            # Calculate angle
            angle = calculate_angle(right_hip, right_knee, right_ankle)
            back_angle = calculate_angle(shoulder, right_hip, right_knee)
            print("angle",angle)
            print("back_angle",back_angle)
        
            
            if ( (int(angle) > 170) and (int(back_angle)>155)):
                self.stage = "up"
            if( (int(angle) < 155) and (self.stage =='up') and (int(back_angle)>155) ):
                self.stage="down"
                self.counter +=1
                print(self.counter )
                
            if ((int(back_angle)>155) or (int(angle) > 170)):
                position="right"
            else:
                position="wrong"


        frame = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        frame_flip=frame
        #frame_flip = cv2.flip(frame, 0)
        cv2.rectangle(frame_flip, (0,0), (225,73), (245,117,16), -1)
        # Visualize angle
        cv2.putText(frame_flip, str(angle),tuple(np.multiply(right_hip, [50, 250]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        

        cv2.putText(frame_flip, 'REPS', (15,12),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(frame_flip, str(self.counter),(10,60),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        

        cv2.putText(frame_flip, str(position), (135,40),cv2.FONT_HERSHEY_SIMPLEX, 2, (20,20,20), 2, cv2.LINE_AA)
        


        if angle==0:
            cv2.putText(frame_flip, 'not visiable to camera', (150,120),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (10,10,10), 1, cv2.LINE_AA)
       

       
   
        ret, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()


