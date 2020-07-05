import sys
multiline_input = sys.stdin.read().split('\n')
for line in multiline_input:
  if line != '':
      first, second = map(lambda x: int(x), line.split())
      print(abs(first - second))