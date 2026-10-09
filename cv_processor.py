import cv2
import sys
import os
import numpy as np

def process_image(task_type="grayscale"):
    input_filename = "input.jpg"
    output_filename = "output.jpg"

    # 1. Broad Verification Check
    if not os.path.exists(input_filename):
        print(f"Error: '{input_filename}' not found in the root workspace directory.")
        print("Please upload or save an image asset as 'input.jpg' first.")
        return

    # 2. Read the image asset matrices
    img = cv2.imread(input_filename)
    if img is None:
        print(f"Error: '{input_filename}' could not be decoded. Ensure it is a valid JPEG image.")
        return

    print(f"Loaded '{input_filename}' successfully. Resolution: {img.shape[1]}x{img.shape[0]}")
    task_type = task_type.lower().strip()

    # 3. Headless Processing Execution Matrix
    if task_type == "grayscale" or task_type == "gray":
        result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("Processing: Converted image array to 8-bit grayscale channels.")

    elif task_type == "edges" or task_type == "canny":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.Canny(gray, 100, 200)
        print("Processing: Executed dual-threshold Canny edge detection matrix.")

    elif task_type == "blur" or task_type == "gaussian":
        result = cv2.GaussianBlur(img, (15, 15), 0)
        print("Processing: Applied 15x15 pixel Gaussian kernel blur filter.")

    elif task_type == "invert":
        result = cv2.bitwise_not(img)
        print("Processing: Inverted all color channel bit values.")

    else:
        print(f"Error: Unknown task sequence type '{task_type}'.")
        print("Available arguments are: 'grayscale', 'edges', 'blur', 'invert'")
        return

    # 4. Write back to the workspace disk to trigger Arena's visual diff tracker
    success = cv2.imwrite(output_filename, result)
    if success:
        print(f"Success: Process matrix saved directly to '{output_filename}'.")
    else:
        print(f"Error: Workspace sandbox pipeline failed writing to '{output_filename}'.")

if __name__ == "__main__":
    # Parse incoming Arena AI terminal argument triggers safely
    chosen_task = "grayscale"
    if len(sys.argv) > 1:
        chosen_task = sys.argv[1]
        
    process_image(chosen_task)
