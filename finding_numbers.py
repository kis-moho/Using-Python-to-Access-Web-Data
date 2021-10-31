import re
name = input("Enter file:")
if len(name) < 1:
    name = "finding_numbers.txt"
fh = open(name)

count = list()
for line in fh:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1 : continue
    for number in numbers :
        inum = int(number)
        count.append(inum)

print(sum(count))
