import collections

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Easter Egg: int32 2201010001

# convert between letters and numbers up to 26
def number_to_letter(i):
	return alphabet[i%26] # %26 does the wrap-around

def letter_to_number(l):
	return alphabet.find(l) # index in the alphabet

# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
	i = letter_to_number(l)
	if i == -1: # character not found in alphabet
		return "" # remove it, it's space or punctuation
	else:
		return number_to_letter(i + amount) # Caesar shift

# How to encode a full text
def caesar_shift(text, amount):
	shifted_text = ""
	for char in text.lower(): # also convert uppercase letters to lowercase
		shifted_text += caesar_shift_single_character(char, amount)
	return shifted_text

### MAIN PROGRAM ###

message = """
swodkdbkfovvobpbywkxkxdsaeovkxngrycksndgyfkcdkxndbexuvoccvoqcyp
"""

code = caesar_shift(message, 16)
print(code)

print(collections.Counter(code).most_common(1)[0])