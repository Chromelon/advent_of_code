with open("d6_input", 'r') as file:
  lines = file.readlines()
for line in lines:
  line = line.strip()

coords = set()
max_r = max_c = 0

for line in lines:
  r, c = map(int, line.split(", "))
  coords.add((r, c))
  max_r = max(max_r, r)
  max_c = max(max_c, c)

size_shared_region = 0

for i in range(max_r + 1):
  for j in range(max_c + 1):
    size_shared_region += int(sum(abs(r - i) + abs(c - j) for r, c in coords) < 10000)

print(size_shared_region)