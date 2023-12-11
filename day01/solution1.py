res = 0
with open('input.txt', 'r') as file:
  for line in file:
    first = 0
    last = 0
    for char in line:
      if char.isdigit():
        first = char
        break
    for char in reversed(line):
      if char.isdigit():
        last = char
        break
    res += int(first + last)

print(res)