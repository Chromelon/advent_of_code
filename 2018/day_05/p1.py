with open("d5_input", 'r') as file:
  line = file.read()

line = line.strip()

length = len(line)
i = 0
done = False
while i < len(line)-1:
  if(line[i].lower() == line[i+1].lower() and line[i] != line[i+1]):
    line=line[:i]+line[i+2:]
    if i > 0:
      i -= 1
    continue
  i+=1
print(len(line))