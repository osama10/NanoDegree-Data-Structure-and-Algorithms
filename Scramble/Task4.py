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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def possible_telemarketers(call_records, text_records):
    unique_callers = set()

    for call in call_records:
        caller = call[0]
        unique_callers.add(caller)

    for call in call_records:
        receiver = call[1]

        if receiver in unique_callers:
            unique_callers.remove(receiver)

    for text in text_records:
        sender = text[0]
        receiver = text[1]

        if sender in unique_callers:
            unique_callers.remove(sender)

        if receiver in unique_callers:
            unique_callers.remove(receiver)

    telemarketers = sorted(caller for caller in unique_callers)

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print("{0}".format(telemarketer))


possible_telemarketers(calls, texts)
