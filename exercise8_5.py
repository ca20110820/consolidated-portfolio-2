"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

# Cedric Anover, 4/08/2023

file_name = 'mbox-short.txt'

counter = 0

with open(file_name, 'r') as file:
    for line in file.readlines():
        if ("From" in line) and not ("From:" in line):
            line_word_ls = line.split()
            
            # Print the email from index 1
            email = line_word_ls[1]
            print(email)

            counter += 1

print("There were {} lines in the file with From as the first word".format(counter))