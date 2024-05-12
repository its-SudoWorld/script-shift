#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <image_file>"
    exit 1
fi

# Check if tesseract is installed
if ! command -v jp2a &> /dev/null; then
    echo "required package is not installed, installing jp2a."
    apt install jp2a
fi

# Perform OCR on the image file
jp2a "$1"

