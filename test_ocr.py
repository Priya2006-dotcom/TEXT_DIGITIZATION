import cv2
import easyocr

# Step 1: Set image path
image_path = r"ocr image/ocr image.JPG"
print("Reading image from:", image_path)

# Step 2: Load the image
image = cv2.imread(image_path)
if image is None:
    print("Failed to load image! Please check the path.")
    exit()

# Step 3: Initialize OCR reader
reader = easyocr.Reader(['en'])

# Step 4: Perform OCR
results = reader.readtext(image)

# Step 5: Print OCR results
if not results:
    print("No text found!")
else:
    for (bbox, text, prob) in results:
        print(f"{text} (Confidence: {prob:.2f})")