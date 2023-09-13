# Cedric Anover, 4/08/2023
#
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

file_name = "mbox-short.txt"

counter = 0
total = 0

with open(file_name, 'r') as file:
    for line in file.readlines():  # List[str]

        # Check if line does not have pattern 'X-DSPAM-Confidence'
        if not line.startswith("X-DSPAM-Confidence:"):
            continue  # Skip to the next iteration

        line = line.replace(' ', '')  # Remove the whitespaces

        idx = line.find(':')  # Use the colon as a reference point for the index

        # Extract the number and Convert the number string to Float
        number = float(line[idx + 1:])  # Left-inclusive, so add 1

        # Update counter and total
        counter += 1
        total += number

print("Average spam confidence:", total / counter)