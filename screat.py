from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np
from pdf2image import convert_from_path
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def screat():
    root = Tk()


    root.withdraw()  # Hide the main window
    pdf_file_path = askopenfilename(initialdir="/home/krishnadev/Downloads", title="Select PDF File",
                                    filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    root.destroy()  # Close the Tkinter window

    if not pdf_file_path:
        print("No PDF file selected.")
        quit()
    # Parameters
    width, height = 1280, 720
    gestureThreshold = 300

    images = convert_from_path(pdf_file_path)
    output_folder = "/home/krishnadev/Downloads/new/"
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(output_folder +  str(i + 1) + '.jpg', 'JPEG')

    folderPath = "/home/krishnadev/Downloads/new/"

    # Camera Setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Hand Detector
    detectorHand = HandDetector(detectionCon=0.8, maxHands=1)

    # Variables
    imgList = []
    delay = 30
    buttonPressed = False
    counter = 0
    drawMode = False
    imgNumber = 0
    delayCounter = 0
    annotations = [[]]
    annotationNumber = -1
    annotationStart = False
    hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image

    # Get list of presentation images
    # Sort the filenames based on numeric values
    pathImages = sorted(os.listdir(folderPath), key=lambda x: int(x.split('.')[0]))

    print(pathImages)

    while True:
        # Get image frame
        success, img = cap.read()
        img = cv2.flip(img, 1)
        pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
        imgCurrent = cv2.imread(pathFullImage)

        # Find the hand and its landmarks
        hands, img = detectorHand.findHands(img)  # with draw
        # Draw Gesture Threshold line
        cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

        if hands and buttonPressed is False:  # If hand is detected

            hand = hands[0]
            cx, cy = hand["center"]
            lmList = hand["lmList"]  # List of 21 Landmark points
            fingers = detectorHand.fingersUp(hand)  # List of which fingers are up

            # Constrain values for easier drawing
            xVal = int(np.interp(lmList[8][0], [0, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [0, height], [0, height]))  # Include entire height
            indexFinger = xVal, yVal

            if cy <= gestureThreshold:  # If hand is at the height of the face
                if fingers == [1, 0, 0, 0, 0]:
                    print("Left")
                    buttonPressed = True
                    if imgNumber > 0:
                        imgNumber -= 1
                        annotations = [[]]
                        annotationNumber = -1
                        annotationStart = False
                if fingers == [0, 0, 0, 0, 1]:
                    print("Right")
                    buttonPressed = True
                    if imgNumber < len(pathImages) - 1:
                        imgNumber += 1
                        annotations = [[]]
                        annotationNumber = -1
                        annotationStart = False

            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)

            if fingers == [0, 1, 0, 0, 0]:
                if annotationStart is False:
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                print(annotationNumber)
                annotations[annotationNumber].append(indexFinger)
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)


            else:
                annotationStart = False

            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True

        else:
            annotationStart = False

        if buttonPressed:
            counter += 1
            if counter > delay:
                counter = 0
                buttonPressed = False

        for i, annotation in enumerate(annotations):
            for j in range(len(annotation)):
                if j != 0:
                    cv2.line(imgCurrent, annotation[j - 1], annotation[j], (0, 0, 200), 12)

        # Resize the image to fit within the screen
        screen_width = 1280  # Define your desired screen width
        screen_height = 720  # Define your desired screen height

        aspect_ratio = screen_width / screen_height
        imgCurrent_height, imgCurrent_width, _ = imgCurrent.shape
        imgCurrent_aspect_ratio = imgCurrent_width / imgCurrent_height

        if imgCurrent_aspect_ratio > aspect_ratio:
            # Image is wider, fit to width
            new_width = screen_width
            new_height = int(screen_width / imgCurrent_aspect_ratio)
        else:
            # Image is taller or square, fit to height
            new_height = screen_height
            new_width = int(screen_height * imgCurrent_aspect_ratio)

        # Resize the image
        imgCurrent_resized = cv2.resize(imgCurrent, (new_width, new_height))

        # Place the resized image on the right side of a blank screen
        blank_screen = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
        blank_screen[0:new_height, 0:new_width] = imgCurrent_resized

        # Display the image
        cv2.imshow("Slides", blank_screen)

        #cv2.imshow("Slides", imgCurrent)
        cv2.imshow("Image", img)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

if __name__ == "__main__":
    screat()