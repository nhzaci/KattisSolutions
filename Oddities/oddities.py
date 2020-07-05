no = int(input())
for i in range(no):
  temp = int(input())
  if temp % 2 == 0:
    print(f'{temp} is even')
  else:
    print(f'{temp} is odd')