import mediapipe as mp
import cv2
import time
import pyautogui as gui
gui.FAILSAFE=False

class handDetector():
    def __init__(self, mode=False, handNo=2, detectCon=0.5, trackingCon=0.5):

        self.mode = mode
        self.handNo = handNo
        self.detectCon = detectCon
        self.trackingCon = trackingCon

        self.mpHands = mp.solutions.hands
        self.Hands = self.mpHands.Hands(
            self.mode, self.handNo, self.detectCon, self.trackingCon)
        self.draw = mp.solutions.drawing_utils

    def detectHand(self, img, draw=True):

        imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.Hands.process(imRGB)

        if self.result.multi_hand_landmarks:
            for hand_lmks in self.result.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(
                        img, hand_lmks, self.mpHands.HAND_CONNECTIONS)
        return img

    def pos_hand_landmarks(self, img, handNo=0, position=False):

        landmarkList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                x = int(lm.x*w)
                y = int(lm.y*h)
                # print(id,x,y)
                landmarkList.append([x, y])
                if position:
                    landmarkList.append([lm.x,lm.y])
        return landmarkList

    def gap(self, a, b):
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

    def action(self, l):
        pass


def main():
    w_scr,h_scr=1920,1080
    cap = cv2.VideoCapture(0)
    cap.set(3, 1920)
    cap.set(4, 1080)
    preTime = 0
    curTime = 0
    detector = handDetector(handNo=1, detectCon=0.5,trackingCon=0.5)
    temp=0
    fpp=0
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        h_img,w_img,_=img.shape
        h_img,w_img=h_img*2/3,w_img*2/3
        if success:
            img = detector.detectHand(img)
            lmkList = detector.pos_hand_landmarks(img)
            # if len(lmkList) != 0 and temp==0:
            #     gui.moveTo(lmkList[8][0]*w_scr/w_img*2,lmkList[8][1]*h_scr/h_img*2)
            #     temp=temp+1
            # elif temp==1:
            #     temp=0
            # else :
            #     temp=temp+1
            if len(lmkList) != 0:
                cv2.circle(img, (lmkList[0][0],lmkList[0][1]), 20, (255,0,0),thickness=-1)
                cv2.circle(img, (lmkList[4][0],lmkList[4][1]), 15, (255,255,0),thickness=-1)
                cv2.circle(img, (lmkList[8][0],lmkList[8][1]), 15, (0,255,0),thickness=-1)
                cv2.circle(img, (lmkList[12][0],lmkList[12][1]), 15, (0,0,255),thickness=-1)
                cv2.circle(img, (lmkList[16][0],lmkList[16][1]), 15, (255,51,153),thickness=-1)
                cv2.circle(img, (lmkList[20][0],lmkList[20][1]), 15, (96,96,0),thickness=-1)

        

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


if __name__ == "__main__":
    main()
