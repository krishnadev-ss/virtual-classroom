import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def display_screenshots():
    screenshots_folder = "/home/krishnadev/Pictures/Screenshots"

    # Check if the folder exists
    if os.path.isdir(screenshots_folder):
        # Create a new window for displaying screenshots
        screenshots_window = tk.Toplevel()
        screenshots_window.title("Screenshots")

        # Get the list of files in the screenshots folder
        files = os.listdir(screenshots_folder)

        # Create a label for the window
        lbl_title = ttk.Label(screenshots_window, text="List of Screenshots", font=("Arial", 16))
        lbl_title.pack(pady=10)

        # Create a listbox to display the files
        listbox_files = tk.Listbox(screenshots_window, width=50, height=20)
        listbox_files.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Insert the list of files into the listbox
        for file in files:
            listbox_files.insert(tk.END, file)

        # Function to open the selected screenshot
        def open_selected_screenshot():
            selected_index = listbox_files.curselection()
            if selected_index:
                selected_file = listbox_files.get(selected_index[0])
                file_path = os.path.join(screenshots_folder, selected_file)
                try:
                    # Use subprocess.Popen to open the file
                    subprocess.Popen(["xdg-open", file_path])
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to open the screenshot: {str(e)}")
            else:
                messagebox.showinfo("Info", "Please select a screenshot to open.")

        # Create a button to open the selected screenshot
        btn_open = ttk.Button(screenshots_window, text="Open Selected Screenshot", command=open_selected_screenshot)
        btn_open.pack(pady=10)

        # Function to close the screenshots window
        def close_window():
            screenshots_window.destroy()

        # Create a button to close the window
        btn_close = ttk.Button(screenshots_window, text="Close", command=close_window)
        btn_close.pack(pady=10)

        # Run the screenshots window
        screenshots_window.mainloop()
    else:
        messagebox.showerror("Error", "Screenshots folder not found.")

# Call the function when the script is run directly
if __name__ == "__main__":
    display_screenshots()
