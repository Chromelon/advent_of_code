import re
import operator

times = []
guards = {}
minutes = {}
begin_time = 0
end_time = 0
biggest_minute_occurrances = 0
biggest_minute = 0
biggest_minute_guard = 0

correct_guard = False

with open("d4_input", 'r') as file:
  lines = file.readlines()
lines = sorted(lines)
for line in lines:
  components = re.split('] ', line)
  datetime = re.split(' ', components[0])
  date=datetime[0].strip('[')
  time=datetime[1]
  hourminute = re.split(':', time)
  hour=hourminute[0]
  minute=hourminute[1]
  if(components[1][0] == 'G'):
    wakeup = re.split('#| ', components[1])
    guardid = wakeup[2]
    guards[guardid] = {}
for line in lines:
  components = re.split('] ', line)
  datetime = re.split(' ', components[0])
  date=datetime[0].strip('[')
  time=datetime[1]
  hourminute = re.split(':', time)
  hour=hourminute[0]
  minute=hourminute[1]
  if(components[1][0] == 'G'):
    wakeup = re.split('#| ', components[1])
    guardid = wakeup[2]
  elif(components[1][0] == 'f'):
    begin_time = int(minute)
  elif(components[1][0] == 'w'):
    end_time = int(minute)
    for i in range(begin_time, end_time):
      if i in guards[guardid]:
        guards[guardid][i] += 1
      else:
        guards[guardid][i] = 1
    begin_time = 0
    end_time = 0
for guard in guards:
  for minute in guards[guard]:
    if(biggest_minute_occurrances < guards[guard][minute]):
      biggest_minute = minute
      biggest_minute_occurrances = guards[guard][minute]
      biggest_minute_guard = guard

print(biggest_minute)
print(biggest_minute_guard)
print(biggest_minute_occurrances)
print(biggest_minute * int(biggest_minute_guard))