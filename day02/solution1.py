d = {'red': 12, 'green': 13, 'blue': 14}
res = 0
gameNumber = 0
with open('input.txt', 'r') as file:
  for line in file:
    b = False
    addLength = 0
    gameNumber += 1
    i = line.find(':')+2
    while i < len(line):
      k = i
      num = ''
      while line[k].isdigit():
        num += line[k]
        k += 1
        if len(num) > 1:
          i += 1
      for key, value in d.items():
        if line[i+2:i+2+len(key)] == key:
          if int(num) > value:
            b = True
            break
          addLength = len(key) + 4
          break
      if b:
        i += 1
        break
      i += addLength
    if not b:
      res += gameNumber
print(res)