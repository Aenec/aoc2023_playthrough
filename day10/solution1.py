maze = open('input.txt', 'r').read().splitlines()
i = -1
j = -1
for k in range(len(maze)):
  if 'S' in maze[k]:
    j = maze[k].index('S')
  if j != -1:
    i = k
    break

frontier = [(i, j)]
visited = set((i, j))
solution = {}
while frontier:
  i, j = frontier.pop(0)
  if j > 0 and maze[i][j] in 'S-J7' and maze[i][j-1] in '-LF' and (i, j-1) not in visited:
    visited.add((i, j-1))
    frontier.append((i, j-1))
    solution[(i, j-1)] = (i, j)
  elif j < len(maze[i])-1 and maze[i][j] in 'S-LF' and maze[i][j+1] in '-J7' and (i, j+1) not in visited:
    visited.add((i, j+1))
    frontier.append((i, j+1))
    solution[(i, j+1)] = (i, j)
  elif i > 0 and maze[i][j] in 'S|JL' and maze[i-1][j] in '|7F' and (i-1, j) not in visited:
    visited.add((i-1, j))
    frontier.append((i-1, j))
    solution[(i-1, j)] = (i, j)
  elif i < len(maze)-1 and maze[i][j] in 'S|7F' and maze[i+1][j] in '|JL' and (i+1, j) not in visited:
    visited.add((i+1, j))
    frontier.append((i+1, j))
    solution[(i+1, j)] = (i, j)
print(len(visited) // 2)