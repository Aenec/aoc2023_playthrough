con = open('input.txt', 'r').read().split(',')

res = 0
for v in con:
  cur = 0
  for char in v:
    cur += ord(char)
    cur *= 17
    cur %= 256
  res += cur
print(res)
