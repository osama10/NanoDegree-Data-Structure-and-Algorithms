"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def number_spent_max_time(calls):
    number_time_frequency = dict()
    max_time_number_tuple = (calls[0][0], int(calls[0][3]))

    for call in calls:

        num1 = call[0]
        num2 = call[1]
        seconds = int(call[3])

        if num1 in number_time_frequency:
            number_time_frequency[num1] += seconds
        else:
            number_time_frequency[num1] = seconds

        if num2 in number_time_frequency:
            number_time_frequency[num2] += seconds
        else:
            number_time_frequency[num2] = seconds

        if int(max_time_number_tuple[1]) < int(number_time_frequency[num1]):
            max_time_number_tuple = (num1, number_time_frequency[num1])

        if int(max_time_number_tuple[1]) < int(number_time_frequency[num2]):
            max_time_number_tuple = (num2, number_time_frequency[num2])

    return max_time_number_tuple


result = number_spent_max_time(calls)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(result[0], result[1]))



