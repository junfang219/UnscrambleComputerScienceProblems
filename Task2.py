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

records = {}
record_longest_duration = []
# for people who call out
for item in calls:
    if item[0] not in records:
        records[item[0]] = int(item[3])
    else:
        records[item[0]] += int(item[3])

# increment people who answer
for item in calls:
    if item[1] not in records:
        records[item[1]] = int(item[3])
    else:
        records[item[1]] += int(item[3])

longest_duration = max(records.values())

record_longest_duration = [num for num, duration in records.items() if duration == longest_duration]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(record_longest_duration, longest_duration))