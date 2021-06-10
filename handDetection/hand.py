import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
Hands = mpHands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

preTime = 0
curTime = 0

while True:
    _, img = cap.read()
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = Hands.process(imRGB)

    if result.multi_hand_landmarks:
        for hand_lmks in result.multi_hand_landmarks:
            for id,lm in enumerate(hand_lmks.landmark):
                #print(id,lm)
                h,w,c=img.shape
                x=int(lm.x*w)
                y=int(lm.y*h)
                #print(id,x,y)

            draw.draw_landmarks(img,hand_lmks,mpHands.HAND_CONNECTIONS)

    curTime = time.time()
    if curTime == preTime:
        fps = 30
    else:
        fps = 1/(curTime-preTime)
    preTime = curTime
    cv2.putText(img, str(int(fps)), (25, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1, color=(255, 0, 0), thickness=2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
