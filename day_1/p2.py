import sys
import re
import collections

def main():
  lines = open('p1_input').read().split()
  sum=0
  prev_sums=[]
  found=False
  while True:
    for line in lines:
      sum+=int(line)
      prev_sums.append(sum);
      if prev_sums.count(sum) > 1:
        print(sum)
        found=True
        break
    if found:
      break
main()