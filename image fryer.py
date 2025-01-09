import os
from tkinter import Tk, filedialog
from PIL import Image

def deepfry_image(input_path, output_dir, compression):
    try:
        # Generate output file name
        file_name, file_ext = os.path.splitext(os.path.basename(input_path))
        output_path = os.path.join(output_dir, f"{file_name}-compressed{file_ext}")

        # Open the image and apply extreme downscaling and upscaling
        with Image.open(input_path) as img:
            img = img.convert("RGB")  # Ensure compatibility with JPEG
            
            # Calculate extreme resizing factor
            if compression < 5:
                compression = 5
            scale_factor = int(compression / 5)  # Higher compression = smaller scale
            new_size = (max(1, img.width // scale_factor), max(1, img.height // scale_factor))
            
            # Resize down, then resize back up for maximum artifacting
            img = img.resize(new_size, Image.NEAREST)  # Downscale
            img = img.resize((img.width * scale_factor, img.height * scale_factor), Image.NEAREST)  # Upscale

            # Save with extreme JPEG compression
            img.save(output_path, "JPEG", quality=1)  # Force extremely low quality for deep frying
        print(f"Image deep-fried successfully: {output_path}")
    except Exception as e:
        print(f"Error compressing image: {e}")

def main():
    # Tkinter setup
    root = Tk()
    root.withdraw()  # Hide the root window

    # File selection
    input_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    if not input_path:
        print("No file selected. Exiting.")
        return

    # Output directory selection
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        print("No output directory selected. Exiting.")
        return

    try:
        compression = int(input("Enter compression percentage (1-500): ").strip())
        if compression < 1 or compression > 500:
            print("Invalid compression value. Must be between 1 and 500.")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 500.")
        return

    # File extension
    file_extension = os.path.splitext(input_path)[1].lower()

    if file_extension in [".jpg", ".jpeg", ".png"]:
        deepfry_image(input_path, output_dir, compression)
    else:
        print("Unsupported file format. Please provide a valid image file.")

if __name__ == "__main__":
    main()