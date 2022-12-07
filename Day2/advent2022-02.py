import os
import sys

# Variables
lineBreakKey = '---'
removableCharacter = '\n'

listSet = []
pair = []
outcome = 0
resultList = []

# Read the file into a list

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'input.txt'))
file_lines = file.readlines()
content_list = [r.strip() for r in file_lines] 
file.close()

print('Creating list of pairs...')

# Make list of pairs
for line in (content_list):
    if lineBreakKey in line:
        if pair:
            pair.append(line)
            listSet.append(pair)
            pair = []
    else:
        pair.append(line)
        listSet.append(pair)

# Assign letters to number value

for letter in pair:
    match letter:
        case "A":
            letter = 1
        case "B":
            letter = 2
        case "C":
            letter = 3
        case "X":
            letter = 1
        case "Y":
            letter = 2
        case "Z":
            letter = 3

print(listSet)

# Remove any evidence of string-type

for pair in listSet:
    if '---' in pair:
        pair.remove('---')

# Subtract each pair, and store into output varibles

print('Subtracting each pair...')

# Convert string values to integers

int_list = [[int(x) for x in pair] for pair in listSet]

for pair in int_list:
     for vals in pair:
        total = sum(pair)
        resultList.append(total)

# Outcome of the round



# add everything together

finalResults = sum(resultList)

unique = list(dict.fromkeys(finalResults))

print('Most calories:' + str(unique))