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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_fixed_line_code(num):
    index = 1
    code = ""
    while num[index] != ')':
        code += num[index]
        index += 1
    return code


def get_code(call_records):
    unique_code = set()

    for call in call_records:
        if call[0][0] == '(' and call[0][1:4] == '080':
            receiver = call[1]

            if receiver[0] == '1':
                unique_code.add('140')
            elif receiver[0] == '(':
                unique_code.add(get_fixed_line_code(receiver))
            else:
                unique_code.add(receiver[:4])

    codes_list = sorted([code for code in unique_code])

    print("The numbers called by people in Bangalore have codes:")

    for code in codes_list:
        print(code)


get_code(calls)


def get_percentage(call_records):
    bangalore_called = 0
    bangalore_receive = 0

    for call in call_records:
        caller = call[0]
        receiver = call[1]

        if caller[0] == '(' and get_fixed_line_code(caller) == '080':
            bangalore_called += 1

            if receiver[0] == '(' and get_fixed_line_code(receiver) == '080':
                bangalore_receive += 1

    percentage = round(bangalore_receive * 100 / bangalore_called, 2)

    print("{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


get_percentage(calls)
