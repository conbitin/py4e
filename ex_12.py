import re 

FILE = 'regex_sum_1341864.txt'
handle = open(FILE)
sum = 0
for line in handle:
    result = re.findall('[0-9]+', line)
    if len(result) < 1: continue
    for number in result:
        sum = sum + int(number)
print(sum)