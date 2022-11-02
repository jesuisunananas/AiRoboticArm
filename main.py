import cv2, time
import mediapipe as mp

cam = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

def findHandPos(capture, color : cv2.cvtColor):
    imgColor = cv2.cvtColor(capture, color)
    processed = hands.process(imgColor)
    result = processed.multi_hand_landmarks
    return result

main = True
while main:
    time.sleep(1)
    ret, frame = cam.read()
    print(findHandPos(frame, cv2.COLOR_BGR2RGB)) 
    

    if not ret:
        print("no frame capture")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
