# main_pipeline.py

# Member 1: OCR Reading from test_ocr.py
from test_ocr import extract_text_from_image

# Member 2: Spelling Correction
from spellcorr import correct_spelling

# Member 3: Contextual Correction
from context_correction import apply_contextual_correction


def main():
    # Step 1: OCR
    image_path = "sample.jpg"  # ✅ Update this if image name/path changes
    print(f"\nReading image from: {image_path}")
    
    ocr_text = extract_text_from_image(image_path)
    print("\n--- OCR Extracted Text ---")
    print(ocr_text)

    # Step 2: Spelling Correction
    corrected_text = correct_spelling(ocr_text)
    print("\n--- After Spelling Correction ---")
    print(corrected_text)

    # Step 3: Contextual Correction using BERT
    final_text = apply_contextual_correction(corrected_text)
    print("\n--- Final Contextually Corrected Text ---")
    print(final_text)


if __name__ == "__main__":
    main()

