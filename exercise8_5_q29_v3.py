# Cedric Anover, 8/09/2023
# Q29: Enter a line from your code above that reads a line from a file (recall opening a file is not reading the file)

file_name = 'mbox-short.txt'

def main():
    global file_name

    emails = [] # Set empty list for emails

    with open(file_name, 'r') as file:
        while True:
            line = file.readline() # Read one line at a time
            
            if "From " in line:
                # Clean the line
                line.rstrip()
                line = line[:-1] 

                line_word_ls = line.split() # Create List of 'Words'
                
                email = line_word_ls[1] # Extract the Email

                emails.append(email) # Append email to emails

            # Exit Criterion
            if not line:
                break
    
    # Print the Emails and the Count
    for email in emails:
        print(email)
    
    print("There were {} lines in the file with From as the first word".format(len(emails)))

if __name__ == "__main__":
    main()