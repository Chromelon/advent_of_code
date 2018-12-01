import sys
import re

def main():
  sum = 0
  with open("p1_input", 'r') as file:
    lines = file.readlines()
  for line in lines:
    if line[0] == '+':
      sum+=int(line[1:])
    else:
      sum-=int(line[1:])
  print(sum)

main()