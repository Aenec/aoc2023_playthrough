with open('input.txt', 'r') as file:
  lines = file.read().splitlines()
con, image = [], []
for line in lines:
  if line:
    image.append(line)
  elif image:
    con.append(image)
    image = []
if image:
  con.append(image)

def calc(image):
  for i in range(1, len(image)):
    top = image[:i][::-1]
    bottom = image[i:]
    if top[:len(bottom)] == bottom[:len(top)]:
      return i
  return 0

res = 0
for image in con:
  res += calc(image) * 100 + calc(list(zip(*image)))
print(res)