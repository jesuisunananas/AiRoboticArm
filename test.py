import cv2, pyautogui
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
    ret, frame = cam.read()
    # flips orientation of frame horizontally
    frame = cv2.flip(frame, 1)
    coords = findHandPos(frame, cv2.COLOR_BGR2RGB)
    
    print(coords)
    # only calls this when hand is on screen, will prioritize hand that has entered screen most recently
    if coords != None:
        # if hand is on the right half of the screen
        xcoord = coords[0].landmark[mpHands.HandLandmark.WRIST].x
        ycoord = coords[0].landmark[mpHands.HandLandmark.WRIST].y
        pyautogui.moveTo(1920*xcoord, 1080*ycoord)
        if xcoord > 0.5:
            print('hello')
        else:
            print('goodbye')  

    # if camera cannot be captured
    if not ret:
        print("no frame capture")
        break
    
    # showing camera & q force exit
    cv2.imshow('cam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
