import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
import test2 as tm
import screenshot as ss

# Function to open the main page
def open_main_page():
    # Replace this with your code to open the main page
    print("Opening Main Page")

# Function to open the main UI
def open_main_ui():
    # Create the main window
    root = tk.Tk()
    root.title("CamBoard")
    root.configure(bg="blue")

    window_width = 1800
    window_height = 1200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Function to open the AI whiteboard
    def open_whiteboard():
        # Replace this with your code to open the AI whiteboard
        print("Opening AI Whiteboard")

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
        ss.display_screenshots()

    # Function to open the OCR detection and select an image
    def open_ocr_detection():
        # Replace this with your code to open OCR detection and select an image
        print("Opening OCR Detection")

    # Create and style the buttons for the main UI
    btn_whiteboard = ttk.Button(root, text="Open AI Whiteboard", command=open_whiteboard)
    btn_whiteboard.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    btn_mouse_controller = ttk.Button(root, text="Open Mouse Controller", command=open_mouse_controller)
    btn_mouse_controller.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    btn_screenshots = ttk.Button(root, text="Open Screenshots", command=open_screenshots)
    btn_screenshots.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    btn_ocr_detection = ttk.Button(root, text="Open OCR Detection", command=open_ocr_detection)
    btn_ocr_detection.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    # Function to quit the application
    def quit_app():
        root.destroy()

    # Button to quit the application
    btn_quit = ttk.Button(root, text="Quit", command=quit_app)
    btn_quit.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    # Run the main event loop for the main UI
    root.mainloop()

# Function to open the landing page
def open_landing_page():
    # Create the landing page window
    landing_page = tk.Tk()
    landing_page.title("Camboard - Landing Page")
    landing_page.configure(bg="blue")

    # Function to open the main page when button is clicked
    def enter_camboard():
        landing_page.destroy()
        open_main_ui()

    # Create and style the label for "Camboard" title
    lbl_camboard = ttk.Label(landing_page, text="Camboard", font=("Arial", 36), background="blue", foreground="white")
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
