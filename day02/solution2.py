res = 0
with open('input.txt', 'r') as file:
  for line in file:
    addLength = 0
    i = line.find(':')+2
    d = {'red': 0, 'green': 0, 'blue': 0}
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
            d[key] = int(num) 
          addLength = len(key) + 4
          break
      i += addLength
    temp = 1
    for val in d.values():
      temp *= val
    res += temp
print(res)