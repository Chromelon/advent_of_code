with open("d5_input", 'r') as file:
  line = file.read()
original = line
best = len(line)
for j in range(0,26):
  line = original
  line = line.replace(chr(ord("a") + j),"")
  line = line.replace(chr(ord("A") + j),"")
  oldline = None
  while oldline != line:
    oldline = line
    for i in range(0,26):
      line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
      line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
  if len(line) < best:
    best = len(line) 
print(best)

#shamelessly stolen because i'm bad at programming lmao