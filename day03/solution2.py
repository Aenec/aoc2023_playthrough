import re

def canAccessPos(i, k, rowLen, colLen):
  return 0 <= i < rowLen and 0 <= k < colLen

pos = [-1, 0, 1]
def findNumbersAroundStar(con, i, k):
  digits = []
  visited = {(i, k)}
  for p1 in pos:
    for p2 in pos:
      ni = i + p1
      nk = k + p2
      if (ni != i or nk != k) and (ni, nk) not in visited and canAccessPos(ni, nk, len(con), len(con[0])):
        if con[ni][nk].isdigit():
          while con[ni][nk].isdigit():
            nk -= 1
          nk += 1
          number = ''
          while canAccessPos(ni, nk, len(con), len(con[0])) and con[ni][nk].isdigit():
            number += con[ni][nk]
            nk += 1
            visited.add((ni, nk))
          if number != '':
            digits.append(number)
        else:
          visited.add((ni, nk))
  return digits if len(digits) == 2 else []


con = [line.strip() for line in open('input.txt', 'r')]
res = 0
n = []
for i in range(len(con)):
  stars = [m.start() for m in re.finditer('\*', con[i])]
  for star in stars:
    n = findNumbersAroundStar(con, i, star)
    res += (int(n[0]) * int(n[1])) if len(n) == 2 else 0
print(res)

    