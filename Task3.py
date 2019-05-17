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

# Part A
Bangalore_calls_list = []

# find all Bangalore calls
for item in calls:
    if item[0][0:5] == '(080)':
        if item[1][0] == '7' or item[1][0] == '8' or item[1][0] =='9':
            Bangalore_calls_list.append(item[1][0:4])
        elif item[1][0] == '(':
            end_code = item[1].index(')')
            code = item[1][1:end_code]
            Bangalore_calls_list.append(code)
        else:
            Bangalore_calls_list.append(item[1][:3])


# remove duplicates by using set and sorted
Bangalore_unique_calls = sorted(set(Bangalore_calls_list))

# make the codes one line at a time
Bangalore_calls_string = ''
for item in Bangalore_unique_calls:
    Bangalore_calls_string += '{}\n'.format(item)

print("The numbers called by people in Bangalore have codes:\n" + Bangalore_calls_string)

# Part B
Bangalore_calls_answer_list = []
# calls from Bangalore to Bangalore
for item in calls:
    if item[0][0:5] == '(080)':
        if item[1][0:5] == '(080)':
            Bangalore_calls_answer_list.append(item)

# percentage of calls from Bangalore are to Bangalore
percentage_B_to_B = round(len(Bangalore_calls_answer_list) / len(Bangalore_calls_list) * 100, 2)
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percentage_B_to_B))