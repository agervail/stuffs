from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

numbers = []
for n in onlyfiles:
    numbers.append(int(n[3:8]))

for i in range(len(numbers)-1):
    if numbers[i+1] - numbers[i] != 1:
        print numbers[i]
