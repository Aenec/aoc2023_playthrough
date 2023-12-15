con = open('input.txt', 'r').read().split(',')

boxes = [[] for _ in range(256)]
for v in con:
  cur = 0
  for char in v:
    if char == '=':
      t = v.split('=')
      found = False
      for i in range(len(boxes[cur])):
        if boxes[cur][i][0] == t[0]:
          found = True
          boxes[cur][i][1] = t[1]
          break
      if not found:
        boxes[cur].append(t)
      break
    elif char == '-':
      if boxes[cur]:
        for i, lens in enumerate(boxes[cur]):
          if lens[0] == v.split('-')[0]:
            boxes[cur].pop(i)
      break
    else:
      cur += ord(char)
      cur *= 17
      cur %= 256

res = 0
for i, box in enumerate(boxes):
  for j, lens in enumerate(box):
    res += ((i+1) * (j+1) * int(lens[1]))
print(res)


