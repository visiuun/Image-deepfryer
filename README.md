![image](https://files.catbox.moe/9wd33v.jpg)

# Image Deep Fryer

This Python tool allows you to "deep fry" an image by applying extreme downscaling and upscaling to distort the image, followed by severe JPEG compression for that "artifacted" effect that gives it a truly low-quality look. Perfect for memes, social media posts, or just adding some extra absurdity to your images.

## Features

- Select an image file from your computer.
- Choose an output directory for saving the processed image.
- Enter a compression percentage (1-500) to control the intensity of the deep-frying effect.
- Supports JPEG and PNG images.
- Extremely low JPEG quality for maximum artifacting.

## Requirements

- Python 3.x
- `Pillow` library for image processing
- `tkinter` for file dialogs

You can install the required dependencies using:

```bash
pip install pillow
```

## How to Use

1. Clone or download this repository to your local machine.
2. Run the script `deepfry_image.py` (or whatever you name it) in your terminal or command prompt.
3. A file selection window will open, allowing you to choose the image you want to deep fry.
4. After selecting the image, choose an output directory where the modified image will be saved.
5. Enter a compression percentage between 1 and 500. The higher the number, the more extreme the "deep frying" effect.
6. The script will process the image, apply the "deep fry" effect, and save it in the selected output directory.

## Example

```bash
python "image fryer.py"
```

Upon running, you'll be asked to select an image file and specify the compression percentage. The program will then output a file with a highly compressed and artifacted version of the input image.

---
