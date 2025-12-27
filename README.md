# 🖼️ Thumbnail Creator – High Quality Image Resizer in Python

✨ **Quickly create sharp, high-quality thumbnails** from your images with a simple Python script and GUI!  

Perfect for bloggers, content creators, or anyone who needs to process many images at once.  

---

## 🚀 Features

- Resize images **proportionally** with a **high-quality LANCZOS filter**  
- Save thumbnails in **JPEG** or **PNG** with optimized quality  
- **Tkinter GUI** – easy to select folders and set dimensions  
- **Progress bar** for tracking multiple images  
- Original images are **never modified**  
- Automatically creates a `thumbnails` folder for output  

---

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/PotegaIT/python-image-resizer-gui.git
```

2. Navigate to the project folder:

```bash
cd python-image-resizer-gui
```

3. Install dependencies:

```bash
pip install pillow
```

Tkinter is included with standard Python installations.

## 🎯 Usage

---

1. Run the script:
```bash
python main.py
```
2. Use the GUI to select your folder of images
3. Set **Width** and **Height** for your thumbnails
4. Click **Select folder** to start processing
5. Find the resized images in the `sample_images/thumbnails` folder

---

## 🖼️ Sample Images

The `sample_images` folder contains demo images for testing purposes.
You can replace them with your own photos.

---

## 💡 Notes

- JPEG images: `quality=95`, optimized for size
- PNG images: `compress_level=1` to preserve details
- Supported formats: `.jpg`, `.jpeg`, `.png`

---

## 🤝 Contributing

Contributions are welcome!
Ideas for **batch renaming, additional filters, or GUI improvements** are encouraged.

---

## 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

---

## 👤 Author

**Greg – PotegaIT**  
- YouTube: [PotegaIT](https://www.youtube.com/@PotegaIT)  
- GitHub: [PotegaIT](https://github.com/PotegaIT) 
