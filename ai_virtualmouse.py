# All the imports go here
import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import os
import pyautogui
import time
def canva():
# Giving different arrays to handle colour points of different colour
    bpoints = [deque(maxlen=1024)]



    # These indexes will be used to mark the points in particular arrays of specific colour
    blue_index = 0
    green_index = 0
    save_directory = '/home/krishnadev/Pictures/'
    os.makedirs(save_directory, exist_ok=True)

    #The kernel to be used for dilation purpose
    kernel = np.ones((5,5),np.uint8)

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
    colorIndex = 0

    # Here is code for Canvas setup
    paintWindow = np.zeros((471,633,3)) + 255

    cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)


    # initialize mediapipe
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils


    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    ret = True
    while ret:
        # Read each frame from the webcam
        ret, frame = cap.read()

        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        # Get hand landmark prediction
        result = hands.process(framergb)

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # # print(id, lm)
                    # print(lm.x)
                    # print(lm.y)
                    lmx = int(lm.x * 640)
                    lmy = int(lm.y * 480)

                    landmarks.append([lmx, lmy])


                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
            fore_finger = (landmarks[8][0],landmarks[8][1])
            middle_finger = (landmarks[12][0], landmarks[12][1])
            ring_finger = (landmarks[16][0], landmarks[16][1])
            little_finger = (landmarks[20][0], landmarks[20][1])

            center = fore_finger
            thumb = (landmarks[4][0],landmarks[4][1])
            cv2.circle(frame, center, 3, (0,255,0),-1)
            print(center[1]-thumb[1])
            distance = np.sqrt((ring_finger[0] - little_finger[0]) ** 2 + (ring_finger[1] - little_finger[1]) ** 2)

            if distance > 40:  # Clear when fingers are close
                paintWindow = np.zeros((471,633,3)) + 255# Clear canvas
                bpoints = [deque(maxlen=1024)]  # Reset drawing points
                blue_index = 0



            elif (thumb[1]-center[1]<30):
                bpoints.append(deque(maxlen=512))
                blue_index += 1


            #elif center[1] <= 65:

                #if 160 <= center[0] <= 255:
                        #colorIndex = 0 # Blue

            else :

                bpoints[blue_index].appendleft(center)

        # Append the next deques when nothing is detected to avois messing up
        else:
            bpoints.append(deque(maxlen=512))
            blue_index += 1


        # Draw lines of all the colors on the canvas and frame
        points = [bpoints]
        # for j in range(len(points[0])):
        #         for k in range(1, len(points[0][j])):
        #             if points[0][j][k - 1] is None or points[0][j][k] is None:
        #                 continue
        #             cv2.line(paintWindow, points[0][j][k - 1], points[0][j][k], colors[0], 2)
        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is None or points[i][j][k] is None:
                        continue
                    cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

        cv2.imshow("Output", frame)
        cv2.imshow("Paint", paintWindow)
          # Save the screenshot to a file

        if cv2.waitKey(1) == ord('q'):
            break

    # release the webcam and destroy all active windows
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    canva()