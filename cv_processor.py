import os
import sys
import cv2

def process_image(task_type="grayscale"):
    input_filename = "input.jpg"
    output_filename = "output.jpg"

    if not os.path.exists(input_filename):
        print(f"Error: '{input_filename}' not found in the current directory.")
        return False

    img = cv2.imread(input_filename)
    if img is None:
        print(f"Error: Could not read '{input_filename}'.")
        return False

    task_type = task_type.lower().strip()

    if task_type in ("grayscale", "gray"):
        result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif task_type in ("edges", "canny"):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.Canny(gray, 100, 200)
    elif task_type in ("blur", "gaussian"):
        result = cv2.GaussianBlur(img, (15, 15), 0)
    elif task_type == "invert":
        result = cv2.bitwise_not(img)
    else:
        print(f"Error: Unknown task '{task_type}'.")
        print("Try: grayscale, edges, blur, or invert")
        return False

    ok = cv2.imwrite(output_filename, result)
    if not ok:
        print(f"Error: Failed to save '{output_filename}'.")
        return False

    print(f"Success: Saved processed image to '{output_filename}'.")
    return True

if __name__ == "__main__":
    task = "grayscale"
    if len(sys.argv) > 1:
        task = sys.argv[1]

    success = process_image(task)
    sys.exit(0 if success else 1)
