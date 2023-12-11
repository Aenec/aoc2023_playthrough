import sys

con = [line.strip() for line in open('input.txt', 'r')]
seeds = [int(num) for num in con[0].split() if num.isdigit()]

alma = []
chapter = []
for line in con[3:]:
  if line == '':
    alma.append(chapter)
    chapter = []
  elif line[0].isdigit():
    chapter.append([int(num) for num in line.split()])
alma.append(chapter)

minLocation = sys.maxsize
for seed in seeds:
  for chap in alma:
    diff = -1
    for row in chap:
      if seed in range(row[1], row[1] + row[2]):
        diff = seed - row[1]
        break
    if diff != -1:
      seed = row[0] + diff
  if seed < minLocation:
    minLocation = seed

print(minLocation)
      
