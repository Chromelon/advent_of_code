import collections

def main():
  sum2=0
  sum3=0
  
  with open("d2_input", 'r') as file:
    lines = file.readlines()
  for line in lines:
    import collections
    letterfreq = collections.Counter(line)
    letterinfo=sorted(dict(letterfreq).values(), reverse=True)
    if(2 in letterinfo):
      sum2+=1;
    if(3 in letterinfo):
      sum3+=1;

    
  print(sum2 * sum3)

main()