import re

filled_squares = [[0 for i in range(0,1000)] for i in range(0, 1000)]

with open("d3_input", 'r') as file:
  lines=file.readlines()
for line in lines:
  components = re.split('@|:', line)
  coords = re.split(',', components[1])
  size = re.split('x|\n', components[2])
  for x in range(int(size[0])):
    for y in range(int(size[1])):
      filled_squares[y+int(coords[1])][x+int(coords[0])] += 1

for line in lines:
  components = re.split('@|:', line)
  coords = re.split(',', components[1])
  size = re.split('x|\n', components[2])

  uniq = True
  for x in range(int(size[0])):
    for y in range(int(size[1])):
      if uniq and filled_squares[y+int(coords[1])][x+int(coords[0])] == 1:
        continue
      else:
        uniq = False
  if uniq:
    print(components[0])