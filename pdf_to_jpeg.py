#!/usr/bin/env python3
"""
convert_to_jpeg.py
Universal converter: PDF (1 page / multiple pages), PNG, JPG → JPEG
Usage:
    python convert_to_jpeg.py --file "/path/to/input"
"""

import os
import argparse
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_jpeg(pdf_path):
    folder = os.path.dirname(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    if len(images) == 1:
        # 1 page → save in same location
        output_file = os.path.join(folder, f"{base_name}.jpeg")
        images[0].save(output_file, "JPEG")
        print(f"Saved: {output_file}")
    else:
        # Multiple pages → save in subfolder
        output_folder = os.path.join(folder, "sawiro")
        os.makedirs(output_folder, exist_ok=True)
        for i, img in enumerate(images, start=1):
            output_file = os.path.join(output_folder, f"page_{i}.jpeg")
            img.save(output_file, "JPEG")
            print(f"Saved: {output_file}")

def image_to_jpeg(img_path):
    folder = os.path.dirname(img_path)
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    output_file = os.path.join(folder, f"{base_name}.jpeg")

    img = Image.open(img_path)
    img = img.convert("RGB")  # ensure compatibility
    img.save(output_file, "JPEG")
    print(f"Saved: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Universal converter: PDF, PNG, JPG → JPEG")
    parser.add_argument("--file", required=True, help="Path to the input file")
    args = parser.parse_args()

    ext = os.path.splitext(args.file)[1].lower()

    if ext == ".pdf":
        pdf_to_jpeg(args.file)
    elif ext in [".png", ".jpg", ".jpeg"]:
        image_to_jpeg(args.file)
    else:
        print("Unsupported file type. Only PDF, PNG, JPG are supported.")

if __name__ == "__main__":
    main()
