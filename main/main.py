import cv2, serial, servocontroller
import mediapipe as mp
from time import sleep

ser = serial.Serial('COM4', 9600, timeout=.1)
cam = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

def angle_change(ser : serial.Serial, hand_location : list):
    hand_x = 1 if hand_location.x > 1 else hand_location.x
    hand_y = 1 if hand_location.y > 1 else hand_location.y
    #hand_z = abs(hand_location.z)

    normalized_location = {
        hand_x : 9, 
        hand_y : 10 
        #hand_z : 11
        }

    for key in normalized_location:
        angle = round(180 * key)
        motor = normalized_location[key]
        servocontroller.write(ser, angle, motor)

def findHandPos(capture, color : cv2.cvtColor):
    imgColor = cv2.cvtColor(capture, color)
    processed = hands.process(imgColor)
    result = processed.multi_hand_landmarks
    return result

def main():
    while True:
        ret, frame = cam.read()
        # flips orientation of frame horizontally
        frame = cv2.flip(frame, 1)
        coords = findHandPos(frame, cv2.COLOR_BGR2RGB)

        # only calls this when hand is on screen, will prioritize hand that has entered screen most recently
        if coords != None:
            landmark_loc = coords[0].landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP]
            angle_change(ser, landmark_loc)

            #hand_z = abs(wrist_loc.z)
            #angle = round(180 * (10 * hand_z))
            #print(f"rounded: {angle}, raw: {hand_z}")
            #servocontroller.write_angle(ser, angle, 11)

        # if camera cannot be captured
        if not ret:
            print("no frame capture")
            break
        
        # showing camera & q force exit
        cv2.imshow('cam', frame)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
    main()
