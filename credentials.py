import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import os
import subprocess
import test2 as tm
import screenshot as ss
import canva as cs
import screenshot as ss
import screat as ld

# Now you can import inferenceModel.py
# Function to open the main page
def open_main_page():
    # Replace this with your code to open the main page
    print("Opening Main Page")

# Function to open the main UI
def open_main_ui():
    # Create the main window
    root = tk.Tk()
    root.title("CamBoard")
    root.configure(bg="#000000")

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set main UI size and position
    window_width = int(screen_width )
    window_height = int(screen_height)
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")



    # Function to open the AI whiteboard
    def open_whiteboard():
        # Replace this with your code to open the AI whiteboard
        print("Opening AI Whiteboard")
        try:
            cs.canva()
            print("Running canva.py in the background...")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run canva.py: {str(e)}")

    # Function to open the mouse controller
    def open_mouse_controller():
        # Replace this with your code to open the mouse controller
        print("Opening Mouse Controller")

        try:
            tm.mouse()
            print("Running test2.py in the background...")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run test2.py: {str(e)}")

    # Function to open the window to display screenshots
    def open_screenshots():
        print("Opening Screenshots")
        ss.display_screenshots()

    # Function to open the OCR detection and select an image
    def open_ocr_detection():
        # Replace this with your code to open OCR detection and select an image
        print("Opening OCR Detection")

    def load_app():
        print("Loading App")

        try:
            ld.screat()
            print("Running screat.py in the background...")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run screat.py: {str(e)}")

    # Function to quit the application
    def quit_app():
        root.destroy()

    # Create and style the buttons for the main UI
    btn_whiteboard = ttk.Button(root, text="Open AI Whiteboard", command=open_whiteboard, width=30)
    btn_mouse_controller = ttk.Button(root, text="Open Mouse Controller", command=open_mouse_controller, width=30)
    btn_screenshots = ttk.Button(root, text="Open Screenshots", command=open_screenshots, width=30)
    btn_ocr_detection = ttk.Button(root, text="Open OCR Detection", command=open_ocr_detection, width=30)
    btn_aaa_bbbb = ttk.Button(root, text="PDF READER", command=load_app, width=30)
    btn_quit = ttk.Button(root, text="Quit", command=quit_app, width=40)

    # Arrange buttons using grid
    btn_whiteboard.grid(row=0, column=0, padx=40, pady=20)
    btn_mouse_controller.grid(row=0, column=1, padx=40, pady=20)
    btn_screenshots.grid(row=0, column=2, padx=40, pady=20)
    btn_ocr_detection.grid(row=1, column=0, padx=40, pady=20)
    btn_aaa_bbbb.grid(row=1, column=1, padx=40, pady=20)
    btn_quit.grid(row=2, column=0, columnspan=3, padx=40, pady=40)

    # Run the main event loop for the main UI
    root.mainloop()


# Function to open the landing page
def open_landing_page():
    # Create the landing page window
    landing_page = tk.Tk()
    landing_page.title("Camboard - Landing Page")
    landing_page.configure(bg="#000000")

    # Function to open the main page when button is clicked
    def enter_camboard():
        landing_page.destroy()
        open_main_ui()

    # Create and style the label for "Camboard" title
    lbl_camboard = ttk.Label(landing_page, text="Camboard", font=("Arial", 36), background="#3E3232", foreground="white")
    lbl_camboard.pack(pady=100)

    # Create and style the button to enter the main page
    btn_enter = ttk.Button(landing_page, text="Enter Camboard", command=enter_camboard)
    btn_enter.pack(pady=20)

    # Set window size and position for the landing page
    window_width = 1800
    window_height = 1200
    screen_width = landing_page.winfo_screenwidth()
    screen_height = landing_page.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    landing_page.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Add the image to the landing page
    image_path = "/home/krishnadev/Downloads/cam.png"  # Path to your image file
    if os.path.exists(image_path):
        # Load the image
        image = Image.open(image_path)

        # Resize the image as needed
        image = image.resize((1900, 1000), Image.ANTIALIAS)

        # Create PhotoImage object from the image
        img = ImageTk.PhotoImage(image)

        # Create a label to display the image
        lbl_image = tk.Label(landing_page, image=img)
        lbl_image.image = img  # Keep a reference to the image to prevent garbage collection
        lbl_image.pack(pady=20)

    else:
        messagebox.showerror("Error", "Image file not found.")

    # Run the main event loop for the landing page
    landing_page.mainloop()
# Function to open the window displaying the list of files in Downloads
def open_downloads_list():
    downloads_window = tk.Tk()
    downloads_window.title("Downloads - Files List")

    # Get the list of files in the Downloads directory
    downloads_dir = "/home/krishnadev/Pictures/Screenshots"
    if os.path.isdir(downloads_dir):
        files = os.listdir(downloads_dir)

        # Create a label to display the list of files
        lbl_files = ttk.Label(downloads_window, text="Files in Downloads:")
        lbl_files.pack(pady=10)

        # Create a text widget to display the files
        txt_files = tk.Text(downloads_window, width=50, height=20)
        txt_files.pack()

        # Insert the list of files into the text widget
        for file in files:
            txt_files.insert(tk.END, file + "\n")

        txt_files.config(state=tk.DISABLED)  # Disable editing

    else:
        messagebox.showerror("Error", "Downloads directory not found.")

    downloads_window.mainloop()

# Call the function to open the landing page when the script is run
open_landing_page()
