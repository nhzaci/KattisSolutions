import functools

initial_state = []

def init_state():
  # Mutates
  for i in range(4):
    initial_state.append(map(lambda x: int(x), input().split()))

def get_changed_state(move, initial_state):
  row1, row2, row3, row4 = get_copy_of_state(initial_state)
  if move == 0:
    functools.reduce()

def get_copy_of_state(current_state):
  return current_state[0].copy(), current_state[1].copy(), current_state[2].copy(), current_state[3].copy()