# Import necessary libraries
import spacy
from transformers import pipeline

# Load pre-trained spaCy model for tokenization and sentence structure analysis
nlp = spacy.load('en_core_web_sm')

# Function for tokenization and analyzing text
def tokenize_text(ocr_text):
    doc = nlp(ocr_text)
    tokens = [(token.text, token.pos_) for token in doc]
    return tokens

# Example OCR result from EasyOCR
ocr_text = "I has a apple and a pen."

# Step 1: Tokenizing the text
tokens = tokenize_text(ocr_text)
print("Tokens and their Parts of Speech:")
for token in tokens:
    print(f"{token[0]} -> {token[1]}")

# Step 2: Use BERT for contextual corrections
fill_mask = pipeline("fill-mask", model="bert-base-uncased")

# Replace the word you want to correct with [MASK]
# Example: let's try to fix "a apple" (which is grammatically incorrect)
text_with_mask = "I has [MASK] apple and a pen."

# Get predictions from BERT
predictions = fill_mask(text_with_mask)

# Step 3: Display the top predictions for the masked word
print("\nPredictions for the masked word:")
for prediction in predictions:
    print(f"Prediction: {prediction['sequence']}, Score: {prediction['score']:.4f}")
