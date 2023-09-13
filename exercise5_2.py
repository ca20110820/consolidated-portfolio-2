# Cedric Anover, 3/08/2023

# Set largest and smallest
largest = smallest = None

while True:
    # Prompt the user to enter a number
    number = input("Enter a number: ")

    try:
        number = int(number) # Convert to Integer

        # Check if no changes were made with largest & smallest variables
        if largest is None and smallest is None:
            # Update. This is only executed once.
            largest = smallest = number

        # Check and Update the largest & smallest variables
        largest = number if number > largest else largest
        smallest = number if number < smallest else smallest
    except:
        if number == 'done': # Case 1:  User entered 'done', we get out of the loop.
            print("Maximum is", largest)
            print("Minimum is", smallest)
            break
        else: # Case 2: User Entered non-integer value.
            print("Invalid input")