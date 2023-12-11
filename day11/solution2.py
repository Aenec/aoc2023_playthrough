uni = open('input.txt', 'r').read().splitlines()

emptyRows = [i for i, row in enumerate(uni) if all([element == '.' for element in row])]
emptyCols = [j for j in range(len(uni[0])) if all(uni[i][j] == '.' for i in range(len(uni)))]
c = []
for i in range(len(uni)):
  c.extend([(i, j) for j in range(len(uni[i])) if uni[i][j] == '#'])

res = 0
for i, v in enumerate(c):
  for v2 in c[:i]:
    iMax = max(v[0], v2[0])
    iMin = min(v[0], v2[0])
    jMax = max(v[1], v2[1])
    jMin = min(v[1], v2[1])
    res += sum(1000000 if k in emptyRows else 1 for k in range(iMin, iMax))
    res += sum(1000000 if k in emptyCols else 1 for k in range(jMin, jMax))
print(res)