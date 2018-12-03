import re
import collections

filled_squares = []

with open("d3_input", 'r') as file:
  lines = file.readlines()
for line in lines:
  components = re.split('@|:', line)
  coords = re.split(',', components[1])
  size = re.split('x|\n', components[2])
  for x in range(int(size[0])):
    for y in range(int(size[1])):
      filled_squares.append((int(coords[0])+int(x), int(coords[1])+int(y)))
print(len([k for k, v in collections.Counter(filled_squares).items() if v > 1]))