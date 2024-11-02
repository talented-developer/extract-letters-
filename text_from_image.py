import os
from PIL import Image
import pytesseract

# Set the path to the tesseract executable if you are on Windows
# For example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Uncomment the line below and adjust the path accordingly if needed
# pytesseract.pytesseract.tesseract_cmd = r'your_path_to_tesseract.exe'

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Iterate through files in the current directory
for filename in os.listdir(current_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Add all desired image formats
        img_path = os.path.join(current_dir, filename)
        
        # Open the image
        img = Image.open(img_path)

        # Use pytesseract to do OCR on the image
        extracted_text = pytesseract.image_to_string(img)

        # Print the extracted text
        print(f"Extracted text from {filename}:\n{extracted_text}\n")