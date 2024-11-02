import pyautogui
import pytesseract
from PIL import Image
import time

# Set the Tesseract cmd path if it's not in your PATH environment variable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your tesseract path

# Allow some time to switch to the screen you want to capture
print("You have 5 seconds to switch to the screen you want to capture...")
time.sleep(5)

# Take a screenshot
screenshot = pyautogui.screenshot()

# Save the screenshot to a file (optional, just for verification)
screenshot.save("screenshot.png")

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(screenshot)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)