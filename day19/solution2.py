# import numpy as np
# import re

# pattern = re.compile(r'\d+')
# letter2Number = {'x': 0, 'm': 1, 'a': 2, 's': 3}

# def workflowPrep(line:str) -> list: #[name, s<1982:R, ...]
#   name, content = line.split('{')
#   content = content.rstrip('}')
#   rules = [name]
#   for s in content.split(','):
#     newRule = []
#     delimiter = s.find(':')
#     if delimiter == -1:
#       newRule.append(s)
#     else:
#       newRule.append(s[0])
#       newRule.append(s[1])
#       newRule.append(int(s[2:delimiter]))
#       newRule.append(s[delimiter+1:])
#     rules.append(newRule)
#   return rules

# def findJob(name:str) -> int:
#   for item in workflows:
#     if item[0] == name:
#       return item
#   return None

# def traverseTree(job:list, prevValue:int):
#   lastConditionValue = -1
#   currentValue = 0
#   for i in job[1:]:
#     if len(i) > 1:
#       #1.Case: next workflow has recursion or ends here accepted 
#       if i[3] != 'R':
#         valueInRange = (i[2]-1) if i[1] == '<' else 4000 - (i[2]+1)
#         valueInRange = valueInRange if lastConditionValue == -1 else valueInRange * lastConditionValue
#         referenceValue = prevValue * valueInRange if prevValue > 0 else 1 * valueInRange
#         if i[3] != 'A':
#           recursiveValue = traverseTree(findJob(i[3]), referenceValue)
#           currentValue += recursiveValue if referenceValue != recursiveValue else referenceValue
#         else:
#           currentValue += referenceValue
      
#       #2.Case: opposite of condition, so safe for next iteration
#       valueOutOfRange = (i[2]-1) if i[1] == '>' else 4000 - (i[2]+1)
#       lastConditionValue = 1 * valueOutOfRange if lastConditionValue == -1 else lastConditionValue * valueOutOfRange
#     else:
#       if i[0] == 'R': continue
#       tempValue = prevValue * lastConditionValue 
#       if i[0] == 'A':
#         currentValue += tempValue
#       else:
#         recursiveValue = traverseTree(findJob(i[0]), tempValue)
#         currentValue = recursiveValue if recursiveValue != tempValue else currentValue 
#   return currentValue


# workflows = []
# for line in open('input_test.txt', 'r'):
#   if line == '\n':
#     break
#   workflows.append(workflowPrep(line.rstrip()))

# start = findJob('in')
# print(traverseTree(start, 0))

import itertools

# Define the workflows as a dictionary of conditions
workflows = {
    "px": [("a", "<", 2006, "qkq"), ("m", ">", 2090, "A"), ("default", "rfg")],
    "pv": [("a", ">", 1716, "R"), ("default", "A")],
    "lnx": [("m", ">", 1548, "A"), ("default", "A")],
    "rfg": [("s", "<", 537, "gd"), ("x", ">", 2440, "R"), ("default", "A")],
    "qs": [("s", ">", 3448, "A"), ("default", "lnx")],
    "qkq": [("x", "<", 1416, "A"), ("default", "crn")],
    "crn": [("x", ">", 2662, "A"), ("default", "R")],
    "in": [("s", "<", 1351, "px"), ("default", "qqz")],
    "qqz": [("s", ">", 2770, "qs"), ("m", "<", 1801, "hdj"), ("default", "R")],
    "gd": [("a", ">", 3333, "R"), ("default", "R")],
    "hdj": [("m", ">", 838, "A"), ("default", "pv")],
}

def evaluate_condition(value, operator, threshold):
    if operator == "<":
        return value < threshold
    elif operator == ">":
        return value > threshold

def get_next_workflow(x, m, a, s, current_workflow):
    for (rating, operator, threshold, next_workflow) in workflows[current_workflow]:
        if rating == "default" or evaluate_condition(locals()[rating], operator, threshold):
            return next_workflow
    return None

def is_accepted(x, m, a, s):
    current_workflow = "in"
    while current_workflow not in ("A", "R"):
        current_workflow = get_next_workflow(x, m, a, s, current_workflow)
    return current_workflow == "A"

# Generate all possible combinations
count = 0
for x, m, a, s in itertools.product(range(1, 4001), repeat=4):
    if is_accepted(x, m, a, s):
        count += 1

print(count)