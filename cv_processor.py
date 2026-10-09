import cv2
import sys
import os
import numpy as np


def process_image(task_type="grayscale"):
    """
    Process an image with various filters and effects.
    
    Args:
        task_type (str): Type of processing to apply. Options: 'grayscale', 'edges', 'blur', 'invert'
    """
    input_filename = "input.jpg"
    output_filename = "output.jpg"

    # Check if input file exists
    if not os.path.exists(input_filename):
        print(f"Error: '{input_filename}' not found.")
        print("Please provide an 'input.jpg' file in the current directory.")
        return False

    # Load the image
    img = cv2.imread(input_filename)
    if img is None:
        print(f"Error: Could not read '{input_filename}'. Make sure it's a valid image file.")
        return False

    print(f"Loaded '{input_filename}' successfully. Resolution: {img.shape[1]}x{img.shape[0]}")
    task_type = task_type.lower().strip()

    # Apply the requested filter
    try:
        if task_type in ["grayscale", "gray"]:
            result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print("Applied grayscale conversion.")

        elif task_type in ["edges", "canny"]:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            result = cv2.Canny(gray, 100, 200)
            print("Applied Canny edge detection.")

        elif task_type in ["blur", "gaussian"]:
            result = cv2.GaussianBlur(img, (15, 15), 0)
            print("Applied Gaussian blur.")

        elif task_type == "invert":
            result = cv2.bitwise_not(img)
            print("Applied color inversion.")

        else:
            print(f"Error: Unknown task type '{task_type}'.")
            print("Available options: 'grayscale', 'edges', 'blur', 'invert'")
            return False

        # Save the result
        success = cv2.imwrite(output_filename, result)
        if success:
            print(f"Success: Saved processed image to '{output_filename}'.")
            return True
        else:
            print(f"Error: Failed to write '{output_filename}'.")
            return False

    except Exception as e:
        print(f"Error during image processing: {e}")
        return False


if __name__ == "__main__":
    # Get task type from command line argument, default to grayscale
    task = "grayscale"
    if len(sys.argv) > 1:
        task = sys.argv[1]
    
    success = process_image(task)
    sys.exit(0 if success else 1)
