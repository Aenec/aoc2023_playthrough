con = [int(line.split(':')[1].replace(' ', '')) for line in open('input.txt', 'r')]

smaller = 0
for j in range(1, con[0]):
  if (j * (con[0] - j)) <= con[1]:
    smaller += 1
  else:
    break
print(con[0] - (2 * smaller) - 1)