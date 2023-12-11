con = [[int(value) for value in line.split(':')[1].split()] for line in open('input.txt', 'r')] 

res = 1 # bc theres at least one win
for i in range(len(con[0])):
  wins = 0
  for j in range(1, con[0][i]):
    if (j * (con[0][i] - j)) > con[1][i]:
      wins += 1
  res *= wins

print(res)
