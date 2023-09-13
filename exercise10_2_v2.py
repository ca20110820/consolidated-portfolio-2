"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 'From ' line 
by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

# Cedric Anover, 4/08/2023

file_name = 'mbox-short.txt'
hour_dist = tuple()

with open(file_name, 'r') as file:
    for line in file.readlines():
        if "From " in line:
            line_word_ls = line.split()
            hour = line_word_ls[5].split(":")[0]
            hour_dist += (hour,)

hour_count = {h: sum([1 for i in hour_dist if i == h]) for h in sorted(list(set(hour_dist)))}

for hour, count in hour_count.items():
    print(hour, count)
