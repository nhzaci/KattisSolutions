import sys

multiline_input = sys.stdin.read().split('\n')
total_dist = 0
counter = 0
results = []
prev_time = 0
for line in multiline_input:
  if counter == 0 and line != '':
    if int(line) < 0:
      break
    counter = int(line)
    continue
  elif line != '':
    speed, elasped_time= map(lambda x: int(x), line.split())
    actual_time, prev_time = elasped_time - prev_time, elasped_time
    total_dist += speed * actual_time
    counter -= 1
    if counter == 0:
      results.append(f'{total_dist} miles')
      total_dist = 0
      prev_time = 0

for result in results:
  print(result)