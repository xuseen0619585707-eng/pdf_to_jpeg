#!/usr/bin/env python3
"""
pdf_to_jpeg.py
Convert each page of a PDF into separate JPEG images.
Usage:
    python pdf_to_jpeg.py --pdf "path/to/input.pdf" --output "path/to/output/folder"
"""

import os
import argparse
from pdf2image import convert_from_path

def pdf_to_jpeg(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)
    
    # Save each page as JPEG
    for i, img in enumerate(images, start=1):
        output_file = os.path.join(output_folder, f"page_{i}.jpeg")
        img.save(output_file, 'JPEG')
        print(f"Saved {output_file}")
    
    print("Done! All pages converted to JPEG.")

def main():
    parser = argparse.ArgumentParser(description="Convert PDF pages to JPEG images.")
    parser.add_argument('--pdf', required=True, help="Path to the input PDF file.")
    parser.add_argument('--output', required=True, help="Folder to save JPEG images.")
    args = parser.parse_args()
    
    pdf_to_jpeg(args.pdf, args.output)

if __name__ == "__main__":
    main()
