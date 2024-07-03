import numpy as np
import re

pattern = re.compile(r'\d+')
letter2Number = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def workflowPrep(content:list) -> list:
  workflow = dict()
  for line in content:
    name, content = line.split('{')
    content = content.rstrip('}')
    rules = content.split(',')
    workflow[name] = []
    for rule in rules:
      if len(rule) > 3:
        workflow[name].append([rule[0], rule[1], int(pattern.search(rule)[0]), rule[rule.find(':')+1:]])
      else:
        workflow[name].append(rule)
  return workflow

def count(range, name):
  if name == "R": #dead end
    return 0
  elif name == "A": #accepted end
    product = 1
    for low, high in range.values():
      product *= high - low + 1
    return product
  
  #else next step
  total = 0
  print(name)
  rules = workflow[name][:len(workflow[name])-1]
  fallback = workflow[name][len(workflow[name])-1]
  for letter, operator, target, next in rules:
    low, high = range[letter]
    within = (low, min(target - 1, high)) if operator == "<" else (max(target + 1, low), high)
    outside = (max(target, low), high) if operator == "<" else (low, min(target, high))
    if within[0] <= within[1]:
      copy = dict(range)
      copy[letter] = within
      total += count(copy, next)
    if outside[0] <= outside[1]:
      range = dict(range)
      range[letter] = outside
    else:
      break
  else:
    total += count(range, fallback)          
  return total

data = np.array([line.rstrip() for line in open('input.txt', 'r')])
splitIndex = np.where((data == '') | (data == '\n'))[0][0]
workflow = workflowPrep(data[:splitIndex])
result = count({key: (1, 4000) for key in "xmas"}, 'in')
print(result)