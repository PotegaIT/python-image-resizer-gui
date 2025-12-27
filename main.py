import os
from tkinter import Tk, filedialog, Button, Label, Entry
from tkinter.ttk import Progressbar
from PIL import Image

# Function to resize an image (high quality)
def resize_image(input_path, width=200, height=200):
    try:
        with Image.open(input_path) as img:
            # Copy the image to avoid modifying the original
            img_copy = img.copy()
            
            # Proportional scaling with high-quality filter
            img_copy.thumbnail((width, height), resample=Image.LANCZOS)
            
            return img_copy
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return None

# Function to save an image with high quality
def save_image(img, output_path):
    ext = os.path.splitext(output_path)[1].lower()
    
    if ext in ['.jpg', '.jpeg']:
        img.save(output_path, quality=95, optimize=True)
    elif ext == '.png':
        img.save(output_path, compress_level=1, optimize=True)
    else:
        img.save(output_path)

# Function to process a folder of images
def process_folder(folder_path, width, height):
    output_folder = os.path.join(folder_path, "thumbnails")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    progress['maximum'] = len(files)
    progress_label.config(text=f"0/{len(files)}")

    for i, filename in enumerate(files, start=1):
        input_path = os.path.join(folder_path, filename)
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}_thumb{ext}")

        resized_img = resize_image(input_path, width, height)
        if resized_img:
            save_image(resized_img, output_path)

        progress['value'] = i
        progress_label.config(text=f"{i}/{len(files)}")
        root.update_idletasks()

# Function called when the folder selection button is clicked
def select_folder():
    folder_path = filedialog.askdirectory(title="Select a folder with images")
    if folder_path:
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            if width <= 0 or height <= 0:
                raise ValueError
        except ValueError:
            label.config(text="Error: Please enter valid numbers for width and height.")
            return
        
        label.config(text=f"Processing folder:\n{folder_path}")
        process_folder(folder_path, width, height)
        label.config(text=f"Done! Thumbnails are in the folder:\n{os.path.join(folder_path, 'thumbnails')}")

# Main window configuration
root = Tk()
root.title("Thumbnail Creator")
root.geometry("700x330")
root.resizable(False, False)

button = Button(root, text="Select a folder with images", command=select_folder)
button.pack(pady=10)

label = Label(root, text="No folder selected")
label.pack(pady=5)

width_label = Label(root, text="Width:")
width_label.pack()
width_entry = Entry(root)
width_entry.insert(0, "200")
width_entry.pack()

height_label = Label(root, text="Height:")
height_label.pack()
height_entry = Entry(root)
height_entry.insert(0, "200")
height_entry.pack()

progress = Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=10)

progress_label = Label(root, text="0/0")
progress_label.pack()

close_button = Button(root, text="Close", command=root.quit)
close_button.pack(pady=10)

root.mainloop()
