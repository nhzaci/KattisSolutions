import sys
import math

multiline_input = sys.stdin.read().split('\n')
hyp_len = 0
no_matches = 0
for line in multiline_input:
  if hyp_len == 0 and no_matches == 0 and line != '':
    no_matches, width, height = map(lambda x: int(x), line.split())
    hyp_len = math.sqrt(width ** 2 + height ** 2)
  elif line != '':
    if int(line) > hyp_len:
      print('NE')
    else:
      print('DA')