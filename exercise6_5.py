# Cedric Anover, 3/08/2023

# Note: do not use any part of the number to extract the number!

text = "X-DSPAM-Confidence:    0.8475"

# Remove whitespaces
text = text.replace(" ", "")

# Extract the number using the colon
idx = text.find(":")

# Need to add 1 because python lists and strings are left-inclusive
number = float(text[idx+1:])

print(number)