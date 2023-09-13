"""
8.4 Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see 
if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

# Cedric Anover, 4/08/2023

# file_name = input("Enter file name: ")
file_name = "romeo.txt"

word_ls = []  # List[str]

with open(file_name, 'r') as file:
    for line in file.readlines():  # line:str
        line_word_ls = line.split()  # List[str]

        for word in line_word_ls:
            # Check if word is not in word_ls
            if word not in word_ls:
                # Append if not in word_ls
                word_ls.append(word)

print(sorted(word_ls))