def hasSymbol(con, i, k):
  for p1 in pos:
    for p2 in pos:
      new_i = i + p1
      new_k = k + p2
      if 0 <= new_i < len(con) and 0 <= new_k < len(con[0]):
        if not con[new_i][new_k].isdigit() and con[new_i][new_k] != '.':
          return True
  return False  


res = 0
num = ''
pos = [0, 1, -1]
add = False
con = [line.rstrip() for line in open('input.txt', 'r')]
for i in range(len(con)):
  for k in range(len(con[0])):
    if not con[i][k].isdigit():
      if len(num) == 0:
        continue
      if add:
        res += int(num)
      num = ''
      add = False
    else:
      num += con[i][k]
      if not add:
        add = hasSymbol(con, i, k)
if add:
  res += int(num)
print(res)