import os
import sys

# Variables
key = '---'
listSet = []
group = []
total = 0
resultList = []
removableCharacter = '\n'

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'dataList.txt'))
file_lines = file.readlines()
content_list = [r.strip() for r in file_lines]
file.close()

print('Creating list of lists...')
# make list of lists
for line in (content_list):
    if key in line:
        if group:
            group.append(line)
            listSet.append(group)
            group = []
    else:
        group.append(line)
        listSet.append(group)

# add together each list individually, and store into output varibles

print('Adding each group individually...')

for group in listSet:
    if '---' in group:
        group.remove('---')

int_list = [[int(x) for x in group] for group in listSet]

for group in int_list:
     for cals in group:
        total = sum(group)
        resultList.append(total)

# sort output variables for the highest one

results_sorted = sorted(resultList)

unique = list(dict.fromkeys(results_sorted))

print('Most calories:' + str(unique))

top_three = []

val1 = unique.pop()
val2 = unique.pop()
val3 = unique.pop()
top_three.append(val1)
top_three.append(val2)
top_three.append(val3)


top_three_total = sum(top_three)

print('Most calories between the top three elves: ' + str(top_three_total))