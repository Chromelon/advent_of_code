import difflib
def main():
  with open("d2_input", 'r') as file:
    lines = file.readlines()
  lines = sorted(lines)
  for i in range(len(lines)-1):
    output=[li for li in difflib.ndiff(lines[i],lines[i+1]) if li[0] != ' ']
    if(len(output) == 2):
      print(lines[i])
      print(lines[i+1])
      print(output)
main()