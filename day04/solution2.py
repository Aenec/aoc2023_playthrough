con = [lines.rstrip()[8:].split() for lines in open('input.txt', 'r')]
cards = [1] * len(con)
for i, game in enumerate(con):
  idx = game.index('|')
  first = game[:idx]
  second = game[idx + 1:]
  wins = sum(1 for elem in first if elem in second)
  for j in range(1, wins+1):
    cards[i+j] += 1 * cards[i]
print(sum(cards))
  