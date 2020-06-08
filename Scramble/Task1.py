"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def print_total_numbers(calls, texts):
    unique_number = set()

    for call in calls:
        unique_number.add(call[0])
        unique_number.add(call[1])

    for text in texts:
        unique_number.add(text[0])
        unique_number.add(text[1])
    return len(unique_number)

print("There are {0} different telephone numbers in the records".format(print_total_numbers(calls, texts)))
