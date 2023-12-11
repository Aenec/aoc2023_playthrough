import re

route = []
with open('input.txt', 'r') as file:
  for row in file:
    route.append(re.findall(r'\b[A-Za-z]{3}\b|\b[A-Za-z]+\b', row))

dir = route.pop(0)[0]
route.pop(0)

cur = 'AAA'
steps = 0
while cur != 'ZZZ':
  for i, v in enumerate(route):
    if cur == v[0]:
      cur = (v[1] if dir[steps % len(dir)] == 'L' else v[2])
      steps += 1
      break
print(steps)