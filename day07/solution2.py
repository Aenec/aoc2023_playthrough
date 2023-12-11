game = [line.strip().split() for line in open('input.txt', 'r')]
rank = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

table = []
rating = []
for i, player in enumerate(game):
  ht = {}
  #create stochastic table of cards
  joker = 0
  for card in player[0]:
    if card == 'J':
      joker += 1
    else:
      if card in ht:
        ht[card] += 1
      else:
        ht[card] = 1

  # ranking hand
  # adding joker to highest number is always better
  sht = sorted(ht.values(), reverse=True)
  if len(sht) > 0:
    sht[0] += joker
  else:
    sht.append(joker)

  for j, v in enumerate(rank):
    if sht == v:
      game[i].append(len(rank) - j)
      break

game.sort(key=lambda x: (x[2], ['J23456789TQKA'.index(char) for char in x[0]]))
#actual rank is determined via position in array
res = 0
for i, v in enumerate(game):
  res += int(v[1]) * (i+1)
print(res)