while True:
  jack, jill = [int(x) for x in input().split()]
  cd = 0
  if jack == 0 and jill == 0:
    break
  jackSet = set(int(input()) for _ in range(jack))
  jillSet = set(int(input()) for _ in range(jill))
  diff = jackSet & jillSet
  print(len(diff))