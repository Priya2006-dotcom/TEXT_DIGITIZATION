from symspellpy.symspellpy import SymSpell, Verbosity
import tempfile
import os

# Create SymSpell object
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Create a temporary dictionary file
temp_dict = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
temp_dict.write("apple 1000\nis 9000\ngood 8000\nto 8500\nhealth 7500\n")
temp_dict.close()

# Load that dictionary
sym_spell.load_dictionary(temp_dict.name, term_index=0, count_index=1)

# Run the spell check
input_term = "aplpes is godo to haetlh"
suggestions = sym_spell.lookup_compound(input_term, max_edit_distance=2)

if suggestions:
    print("Corrected:", suggestions[0].term)
else:
    print("No suggestions found.")
