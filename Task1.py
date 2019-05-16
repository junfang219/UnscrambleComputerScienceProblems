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

phone_numbers_list = []

for item in texts:
    phone_numbers_list += item[0:len(item)-1]

for item in calls:
    phone_numbers_list += item[0:len(item)-2]

phone_numbers_set = set(phone_numbers_list)
num_unique_phones = len(phone_numbers_set)

print('There are {} different telephone numbers in the records.'.format(num_unique_phones))