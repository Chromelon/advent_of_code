import re
import operator

times = []
guards = {}
minutes = {}
begin_time = 0
end_time = 0
placehold_time = 0
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
    guards[guardid] = 0;
  elif(components[1][0] == 'f'):
    placehold_time = int(minute)
  elif(components[1][0] == 'w'):
    placehold_time = int(minute) - placehold_time
    guards[guardid] += placehold_time
    placehold_time = 0
guards = sorted(guards.items(), key=lambda kv: kv[1]) #sorts lowest to highest
guards = guards[::-1]
worst_guard_id = guards[0][0]
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
    if(guardid == worst_guard_id):
      correct_guard = True
    else:
      correct_guard = False
  if(correct_guard == True):
    if(components[1][0] == 'f'):
      begin_time = int(minute)
    elif(components[1][0] == 'w'):
      end_time = int(minute)
      for i in range(begin_time, end_time):
        if i in minutes:
          minutes[i] += 1
        else:
          minutes[i] = 1
      begin_time = 0
      end_time = 0
minutes = sorted(minutes.items(), key=lambda kv: kv[1])
minutes = minutes[::-1]
most_sleeping = minutes[0][0]

print(int(worst_guard_id) * most_sleeping)