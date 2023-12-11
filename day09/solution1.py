con = [[int(val) for val in line.rstrip().split()] for line in open('input.txt', 'r')]

calc = []
res = 0
for i in range(len(con)):
  calc = con[i]
  while True:
    temp = []
    res += calc[len(calc)-1]
    for idx in range(len(calc)-1):
      temp.append(calc[idx+1] - calc[idx])
    if all(v == 0 for v in temp):
      break
    calc = temp
print(res)