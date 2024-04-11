from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np
from pdf2image import convert_from_path
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import datetime

def save_image(img, folderPath, imgNumber, pathImages):
    """Saves the current image with annotations to the specified folder.

    Args:
        img: The image to be saved (including annotations).
        folderPath: The path to the folder where the image will be saved.
        imgNumber: The index of the current image in the presentation.
        pathImages: The list of image filenames in the presentation.

    Returns:
        None
    """

    # Generate unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_path = os.path.join(folderPath, pathImages[imgNumber])  # Full path of the image

    try:
        # Save the current image (overwriting the existing file)
        cv2.imwrite(full_path, img)
        print(f"Image overwritten successfully: {full_path}")
    except Exception as e:
        print(f"Error overwriting image: {e}")
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
    gestureThreshold = 500

    images = convert_from_path(pdf_file_path)
    output_folder = "/home/krishnadev/Downloads/new/"
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(output_folder +  str(i + 1) + '.jpg', 'JPEG')

    folderPath = "/home/krishnadev/Downloads/new/"
    #folderPath = "/home/krishnadev/Pictures"

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
    annotations = []  # List of lists to store annotations for each gesture
    annotationNumber = -1
    annotationStart = False
    hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image

    # Get list of presentation images
    pathImages = sorted(os.listdir(folderPath), key=lambda x: int(x.split('.')[0]))
    print(pathImages)
    prev_x, prev_y = None, None

    while True:
        # Get image frame
        success, img = cap.read()
        img = cv2.flip(img, 1)
        pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
        imgCurrent = cv2.imread(pathFullImage, cv2.IMREAD_UNCHANGED)  # Read as-is for aspect ratio preservation
        new_width = 1280  # Define your desired screen width
        new_height = int(imgCurrent.shape[0] * (new_width / imgCurrent.shape[1]))  # Maintain aspect ratio
        imgCurrent = cv2.resize(imgCurrent, (new_width, new_height))

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
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
            indexFinger = (cx, cy)

            if cy <= gestureThreshold:  # If hand is at the height of the face
                if fingers == [1, 0, 0, 0, 0]:
                    print("Left")
                    buttonPressed = True
                    if imgNumber > 0:
                        imgNumber -= 1
                        annotations = [[]]
                        annotationNumber = -1
                        annotationStart = False  # Reset annotation for new gesture
                if fingers == [0, 0, 0, 0, 1]:
                    print("Right")
                    buttonPressed = True
                    if imgNumber < len(pathImages) - 1:
                        imgNumber += 1
                        annotations = [[]]
                        annotationNumber = -1
                        annotationStart = False  # Reset annotation for new gesture

            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(imgCurrent, (cx, cy), 10, (0, 0, 255), cv2.FILLED)



            if fingers == [0, 1, 0, 0, 0]:
                if annotationStart is False:
                    annotationStart = True
                    annotations.append([])  # Create a new list for each gesture
                    annotationNumber += 1
                print(annotationNumber)
                annotations[annotationNumber].append(indexFinger)
                cv2.circle(imgCurrent, indexFinger, 10, (0, 0, 255), cv2.FILLED)

            else:
                annotationStart = False

            if fingers == [1, 1, 1, 1, 1]:  # Clear screen when all fingers are up
                annotations = [[]]
                annotationNumber = -1
                annotationStart = False
                buttonPressed = True

            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    annotations.pop()  # Remove the last list for the current gesture
                    annotationNumber -= 1
                    buttonPressed = True

        else:
            annotationStart = False

        if buttonPressed:
            counter += 1
            if counter > delay:
                counter = 0
                buttonPressed = False

        # Draw lines for smooth drawing
        for gesture in annotations:
            if len(gesture) > 1:
                for i in range(len(gesture) - 1):
                    cv2.line(imgCurrent, gesture[i], gesture[i + 1], (0, 0, 200), 10)

        imgSmall = cv2.resize(img, (ws, hs))
        h, w, _ = imgCurrent.shape
        imgCurrent[0:hs, w - ws: w] = imgSmall

        cv2.imshow("Slides", imgCurrent)
        cv2.imshow("Image", img)

        key = cv2.waitKey(1)
        if key == ord('s'):
            save_image(imgCurrent, folderPath, imgNumber, pathImages)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    screat()
