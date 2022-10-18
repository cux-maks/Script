from itertools import *
max_size = int(input())

board = []
maxResult = 0

def right(map):
  returnValue = []
  for x in map:
    buffer = []
    for y in range(0, x.count(0)):
      buffer.append(0)
    for y in x:
      if y != 0: buffer.append(y)
    returnValue.append(buffer)
  map = returnValue
  returnValue = []
  for x in map:
    for y in range(len(x) - 1):
      if x[len(x) - y - 2] == x[len(x) - y - 1]:
        x[len(x) - y - 1] = x[len(x) - y - 2] + x[len(x) - y - 1]
        x[len(x) - y - 2] = 0
  for x in map:
    buffer = []
    for y in range(0, x.count(0)):
      buffer.append(0)
    for y in x:
      if y != 0: buffer.append(y)
    returnValue.append(buffer)
  return returnValue

def left(map):
  returnValue = []
  for x in map:
    buffer = []
    for y in x:
      if y != 0: buffer.append(y)
    for y in range(0, x.count(0)):
      buffer.append(0)
    returnValue.append(buffer)
  map = returnValue
  returnValue = []
  for x in map:
    for y in range(len(x) - 1):
      if x[y] == x[y + 1]:
        x[y] = x[y] + x[y + 1]
        x[y + 1] = 0
  for x in map:
    buffer = []
    for y in x:
      if y != 0: buffer.append(y)
    for y in range(0, x.count(0)):
      buffer.append(0)
    returnValue.append(buffer)
  return returnValue

def up(map):
  value = []
  returnValue = []
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(map[y][x])
    value.append(buffer)
  value = left(value)
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(value[y][x])
    returnValue.append(buffer)
  return returnValue

def down(map):
  value = []
  returnValue = []
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(map[y][x])
    value.append(buffer)
  value = right(value)
  for x in range(len(map[0])):
    buffer = []
    for y in range(len(map[0])):
      buffer.append(value[y][x])
    returnValue.append(buffer)
  return returnValue

for x in range(0, max_size):
  board.append(list(map(int, input().split())))

method = list(product([x for x in range(0, 4)], repeat = 5))
c_board = board

for y in method:
  board = c_board
  for x in range(len(y)):
    if y[x] == 0:
      board = right(board)
    elif y[x] == 1:
      board = left(board)
    elif y[x] == 2:
      board = up(board)
    elif y[x] == 3:
      board = down(board)
  for y in board:
    buffer = y
    buffer.append(maxResult)
    maxResult = max(buffer)
print(maxResult)