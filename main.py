import easyocr
from symspellpy.symspellpy import SymSpell, Verbosity
import os

# OCR Reader
reader = easyocr.Reader(['en'])

# Load Image
image_path = 'sample.jpg'  # Change to your image filename
result = reader.readtext(image_path, detail=0)

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = "frequency.txt"

if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1):
    print("Dictionary file not found!")

# Spell Correction
corrected_text = []
for sentence in result:
    words = sentence.split()
    corrected = []
    for word in words:
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            corrected.append(suggestions[0].term)
        else:
            corrected.append(word)
    corrected_text.append(' '.join(corrected))

# Final Output
print("Original OCR Text:", result)
print("Corrected Text:", corrected_text)