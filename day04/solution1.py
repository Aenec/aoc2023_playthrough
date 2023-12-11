res = 0
con = [line.rstrip()[8:].split() for line in open('input.txt', 'r')]
for game in con:
  idx = game.index('|')
  first = game[:idx]
  second = game[idx + 1:]
  wins = sum(1 for elem in first if elem in second)
  if wins == 1:
    res += 1
  elif wins > 1:
    res += 1 * (2 ** (wins-1))

print(res)