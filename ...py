def findposition(self, img, handNo=0, draw =True):
        
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)
            
            return lmList




lmList = detector.findposition(img)
        if len(lmList) !=0:
            print(lmList[4])
        