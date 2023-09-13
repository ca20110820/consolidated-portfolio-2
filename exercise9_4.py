# Cedric Anover, 4/08/2023
#
# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

file_name = "mbox-short.txt"
email_dict = {} # Dict: Email -> Count

with open(file_name, 'r') as file:
    for line in file.readlines():
        if "From " in line:
            line_word_ls = line.split()
            
            email = line_word_ls[1] # Extract Email
            
            if email in email_dict.keys(): # If email already in email_dict
                email_dict[email] += 1
            else: # If email not in email_dict
                email_dict[email] = 1

### Extract most prolific committer
commiter_email = None
commiter_count = None

for email, count in email_dict.items():
    if (commiter_email == None) or (commiter_count == None):
        commiter_email = email
        commiter_count = count
    else:
        # Check if New Prolific Commiter
        if count > commiter_count:
            commiter_email = email
            commiter_count = count

print(commiter_email, commiter_count)