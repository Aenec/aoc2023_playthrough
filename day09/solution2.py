con = [[int(val) for val in line.rstrip().split()] for line in open('input.txt', 'r')]

calc = []
res = 0
for i in range(len(con)):
  calc = con[i]
  left = [calc[0]]
  while True:
    temp = []
    for idx in range(len(calc)-1):
      temp.append(calc[idx+1] - calc[idx])
    left.append(temp[0])
    if all(v == 0 for v in temp):
      break
    calc = temp
    
  x = 0
  for j in range(len(left)-2, -1, -1):
    x = left[j] - x
  res += x
print(res)