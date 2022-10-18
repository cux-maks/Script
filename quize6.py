def my_average(*nums):
  if len(nums) == 0:
    return 'TypeError: my_average() missing 1 required positional argument: ......'
  else: 
    return sum(nums)/len(nums)

def my_callback(result):
    print('my result:', result)

def add(values):
  result = type(values[0])()
  for a in values:
    result += a
    if type(values[0]) == ' str':
      result += ' '
  return result

def apply_function(f, values, callback):
  result = f(values)
  callback(result)


print(my_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
apply_function(add, (1, 2, 3), callback=my_callback)
apply_function(add, ('script', 'programming', 'is', 'the', 'best'), callback=my_callback)