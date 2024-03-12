import os
from PIL import Image

# Mapping of pixel intensity to ASCII characters
ASCII_CHARS = "@#$%?*+:,.-&"

# Resize the image to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

# Convert the image to grayscale
def grayify(image):
    return image.convert("L")

# Convert pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_chars = [ASCII_CHARS[pixel // 25] for pixel in pixels]
    return "".join(ascii_chars)

# Display the ASCII art
def display_ascii_art(ascii_str, width):
    for i in range(0, len(ascii_str), width):
        print(ascii_str[i:i+width])

def main():
    # Request user input for image path
    while True:
        path = input("Enter a valid pathname to an image (or 'q' to quit):\n")
        if path.lower() == "q":
            break

        # Check if file exists
        if not os.path.isfile(path):
            print(f"{path} is an invalid pathname to an image.")
            continue

        try:
            # Open and process the image
            image = Image.open(path)
            image = resize_image(image)
            image = grayify(image)
            ascii_str = pixels_to_ascii(image)
            image_width = image.width

            # Display the ASCII art
            display_ascii_art(ascii_str, image_width)

        except Exception as e:
            print(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
