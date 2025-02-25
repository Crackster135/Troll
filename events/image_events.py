import random
import time
import tkinter as tk
from PIL import Image, ImageTk
import os

directory = "events/media/images/"

images = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def display_image_in_window():
    img_index = random.randint(0, len(images) - 1)
    # Desired window size
    width, height = random.randint(400, 800), random.randint(400, 800)

    # Construct the absolute path to the image file
    #current_dir = os.path.dirname(os.path.abspath(__file__)) + '/media/images/'
    image_path = directory + images[img_index]

    # Create a window
    root = tk.Tk()

    # Open an image file
    img = Image.open(image_path)

    # Resize the image to the specified width and height
    img = img.resize((width, height), Image.Resampling.LANCZOS)

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

def display_multiple_images():
    for image in images:
        image = directory + image

        # Create a separate window for each image
        window = tk.Toplevel()

        # Open an image file
        img = Image.open(image)

        # Resize the image if necessary
        width = random.randint(400, 800)
        height = random.randint(400, 800)
        img = img.resize((width, height), Image.Resampling.LANCZOS)

        # Convert the image to a format Tkinter can use
        img_tk = ImageTk.PhotoImage(img)

        # Create a label to hold the image
        label = tk.Label(window, image=img_tk)
        label.image = img_tk  # Keep a reference to the image to prevent garbage collection
        label.pack()

        # Set the desired window size
        window.geometry(f"{width}x{height}+{random.randint(0, 2000)}+{random.randint(0, 2000)}")
    # Start the main Tkinter event loop
    tk.mainloop()
