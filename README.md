# ASCII Art Generator

This Python script converts images into ASCII art. It takes an image file as input and outputs a text-based representation of the image using ASCII characters.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Breakdown](#code-breakdown)
- [License](#license)

## Features

- Convert any image file to ASCII art
- Resize images to a specified width
- Convert images to grayscale
- Map pixel intensities to ASCII characters
- Interactive command-line interface

## Requirements

- Python 3.x
- Pillow (PIL Fork) library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Pillow library:

```bash
pip install Pillow
```

3. Download the `ascii_art_generator.py` script to your local machine.

## Usage

Run the script from the command line:

```bash
python ascii_art_generator.py
```

Follow the prompts to enter the path to an image file. The script will then convert the image to ASCII art and display it in the console.

Enter 'q' when prompted for a file path to quit the program.

## How It Works

The ASCII Art Generator works by following these steps:

1. Load the input image
2. Resize the image to a manageable width
3. Convert the image to grayscale
4. Map each pixel's intensity to an ASCII character
5. Display the resulting ASCII art in the console

## Code Breakdown

Let's break down the main components of the code:

### Imports and Constants

```python
import os
from PIL import Image

ASCII_CHARS = "@#$%?*+:,.-&"
```

This section imports the necessary modules and defines the ASCII characters used to represent different pixel intensities.

### Image Resizing

```python
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))
```

This function resizes the input image to a specified width while maintaining the aspect ratio. Resizing helps to create more manageable ASCII art output.

### Grayscale Conversion

```python
def grayify(image):
    return image.convert("L")
```

This function converts the image to grayscale, which simplifies the pixel intensity mapping process.

### Pixel to ASCII Conversion

```python
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_chars = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    return "".join(ascii_chars)
```

This function maps each pixel's intensity to an ASCII character. It divides the pixel value (0-255) by 25 to get an index (0-10) for the `ASCII_CHARS` list.

### ASCII Art Display

```python
def display_ascii_art(ascii_str, width):
    for i in range(0, len(ascii_str), width):
        print(ascii_str[i:i+width])
```

This function prints the ASCII art to the console, breaking it into lines based on the image width.

### Main Function

```python
def main():
    while True:
        path = input("Enter a valid pathname to an image (or 'q' to quit):\n")
        if path.lower() == "q":
            break
        if not os.path.isfile(path):
            print(f"{path} is an invalid pathname to an image.")
            continue
        try:
            image = Image.open(path)
            image = resize_image(image)
            image = grayify(image)
            ascii_str = pixels_to_ascii(image)
            image_width = image.width
            display_ascii_art(ascii_str, image_width)
        except Exception as e:
            print(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
```

The main function handles user input, file validation, and orchestrates the ASCII art generation process. It provides a loop for processing multiple images and includes error handling for invalid inputs or processing issues.
