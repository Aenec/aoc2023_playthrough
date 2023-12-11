import re
import math

routes = []
with open('input.txt', 'r') as file:
  for row in file:
    routes.append(re.findall(r'\b[A-Za-z]{3}\b|\b[A-Za-z]+\b', row))

dir = routes.pop(0)[0]
routes.pop(0)
loops = []

for v in [v[0] for v in routes if 'A' == v[0][2]]:
  loop = []
  steps = 0
  beginLoop = None
  while 1:
    while steps == 0 or not v[2] == 'Z':
      for i in range(len(routes)):
        if routes[i][0] == v:
          v = routes[i][1 if dir[steps % len(dir)] == 'L' else 2] 
          break
      steps += 1
    loop.append(steps)
    if beginLoop is None:
      beginLoop = v
      steps = 0
    elif v == beginLoop:
      break
  loops.append(loop)

print(math.lcm(*[l[0] for l in loops]))