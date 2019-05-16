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

telemarketers = []

# get a list of numbers calling out, a list of numbers answering calls,
# a list of numbers sent out texts, and a list of numbers receiving text
callout_numbers = [number[0] for number in calls]
answer_numbers = [number[1] for number in calls]
textsent_numbers = [number[0] for number in texts]
textreceive_numbers = [number[1] for number in texts]

# combine answer_numbers, textsent_numbers, textreceive_numbers as a set
other_three_set = set(answer_numbers + textsent_numbers + textreceive_numbers)

# loop through the callout_numbers and find the elements that are not in the combined set.
for num in callout_numbers:
    if num not in other_three_set:
        telemarketers.append(num)


# remove duplicates and sort the list
telemarketers_set = sorted(set(telemarketers))

# make the numbers printing one line at a time
telemarketers_string = ''

for num in telemarketers:
    telemarketers_string += '{}\n'.format(num)

print('These numbers could be telemarketers:\n' + telemarketers_string)