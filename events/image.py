import tkinter as tk
from PIL import Image, ImageTk
import os

def display_image_in_window():
    # Create a window
    root = tk.Tk()

    width = 500
    height = 500
    
    # Example call
    # Construct the absolute path to the image file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "src/arabic1.jpg")

    # Open an image file
    img = Image.open(image_path)

    # Convert the image to a format Tkinter can use
    img_tk = ImageTk.PhotoImage(img)

    # Create a label to hold the image
    label = tk.Label(root, image=img_tk)
    label.image = img_tk  # Keep a reference to the image to prevent garbage collection
    label.pack()

    # Set the desired window size
    root.geometry(f"{width}x{height}")

    # Start the GUI event loop
    root.mainloop()


    # Desired window size
    width, height = 800, 600

    # Display the image in the window
    display_image_in_window(image_path, width, height)
