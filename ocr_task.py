import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    Extracts text from an image using Tesseract OCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except FileNotFoundError:
        return "Error: Image not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    image_file = input("Enter the path to the image file: ")  # Get image path from user
    extracted_text = extract_text_from_image(image_file)
    print("\n--- Extracted Text ---")
    print(extracted_text)