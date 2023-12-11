import sys

def compareRanges(r1, r2):
  cr = None
  ucr = set()

  if r1.start >= r2.start and r1.stop <= r2.stop:
    cr = r1
  else:
    if r1.start <= r2.start:
      if r1.stop <= r2.stop:
        if r1.stop < r2.start:
          ucr.add(r1)
        else:
          cr = range(r2.start, r1.stop)
          ucr.add(range(r1.start, r2.start))
      else:
        cr = r2
        ucr.add(range(r1.start, r2.start))
        ucr.add(range(r2.stop, r1.stop))
    else:
      if r1.start > r2.stop:
        ucr.add(r1)
      else:
        cr = range(r1.start, r2.stop)
        ucr.add(range(r2.stop, r1.stop))

  return cr, ucr

def getOutput(cr, range2, range3):
  start = range3.start + (cr.start - range2.start)
  end = start + (cr.stop - cr.start)
  return range(start, end)

con = [line.strip() for line in open('input.txt', 'r')]
seeds = [int(num) for num in con[0].split() if num.isdigit()]
minLocation = sys.maxsize

alma = []
chapter = []
for line in con[3:]:
  if line == '':
    alma.append(chapter)
    chapter = []
  elif line[0].isdigit():
    chapter.append([int(num) for num in line.split()])
alma.append(chapter)

for i in range(0, len(seeds), 2):
  newInput = {range(seeds[i], seeds[i] + seeds[i+1])}
  for chap in alma:
    ucr = list(newInput)
    newInput = set()
    for entry in chap:
      ucrTemp = []
      r2 = range(entry[1], entry[1] + entry[2])
      while ucr:
        r1 = ucr.pop()
        ncr, nucr = compareRanges(r1, r2)
        if ncr:
          newInput.add(getOutput(ncr, r2, range(entry[0], entry[0] + entry[2])))
        ucrTemp.extend(nucr)
      ucr = ucrTemp
    newInput.update(ucr) #no coverage found

  minTemp = min(newInput, key=lambda x: x.start).start
  if minTemp < minLocation:
    minLocation = minTemp
print(minLocation)