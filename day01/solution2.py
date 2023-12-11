d = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
  'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
  'nine': '9'}
res = 0

with open('input.txt', 'r') as file:
  for line in file:
    first = 0
    last = 0

    i = 0
    while i < len(line):
      number = '' 
      # Check for spelled-out numbers
      for word, digit in d.items():
        if line[i:i+len(word)] == word:
          number += digit
          i += 2 #overlap of spelled numbers only at the last char 
          break
      
      # Check for digits
      if not number.isdigit():
        if line[i].isdigit():
          number = line[i]
          i += 1

      # Set position 
      if number.isdigit():
        if first == 0:
          first = number
        last = number
      else:
        i += 1
    res += int(first + last)

print(res)