import cv2, serial, servocontroller
import mediapipe as mp

ser = serial.Serial('COM4', 9600, timeout=.1)
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

    # only calls this when hand is on screen, will prioritize hand that has entered screen most recently
    if coords != None:
        wrist_loc = coords[0].landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP]
        # if hand is on the right half of the screen
        hand_x = 1 if wrist_loc.x > 1 else wrist_loc.x
        angle = round(180 * hand_x)
        servocontroller.write_angle(ser, angle, 9)

        hand_y = 1 if wrist_loc.y > 1 else wrist_loc.y
        angle = round(180 * hand_y)
        servocontroller.write_angle(ser, angle, 10)

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
