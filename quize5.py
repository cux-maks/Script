str_1 = "A woman finds a pot of treasure on the road while she is returning from work. Delighted (very happy) with her luck, she decides to keep it. As she is taking it home, it keeps changing. However, her enthusiasm refuses to fade away (disappear or faint slowly)."
str_2 = "This classic fable (story) tells the story of a very slow tortoise (another word for turtle) and a speedy hare (another word for rabbit). The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than him, but when the two actually race, the results are surprising."

str_1 = list(str_1)
str_2 = list(str_2)

while(')' in str_1 or '(' in str_1 or '.' in str_1 or ',' in str_1 or ')' in str_2 or '(' in str_2 or '.' in str_2 or ',' in str_2):
  if '(' in str_1: str_1.remove('(')
  if ')' in str_1: str_1.remove(')')
  if '.' in str_1: str_1.remove('.')
  if ',' in str_1: str_1.remove(',')
  if '(' in str_2: str_2.remove('(')
  if ')' in str_2: str_2.remove(')')
  if '.' in str_2: str_2.remove('.')
  if ',' in str_2: str_2.remove(',')

str_1 = ''.join(x for x in str_1)
str_2 = ''.join(x for x in str_2)

dict_1 = {}
str_1 = str_1.split(' ')

dict_2 = {}
str_2 = str_2.split(' ')

for x in str_1:
  if x in dict_1:
    dict_1[x] += 1
  else:
    dict_1[x] = 1

for x in str_2:
  if x in dict_2:
    dict_2[x] += 1
  else:
    dict_2[x] = 1


result_1 = []
result_2 = []

for x, y in dict_1.items():
  result_1.append((x, y))

for x, y in dict_2.items():
  result_2.append((x, y))

print(result_1)
print(result_2)

plus_result = []

for x, y in dict_1.items():
  if x in dict_2:
    plus_result.append((x, dict_2[x] + dict_1[x]))
  else:
    plus_result.append((x, y))

for x, y in dict_2.items():
  if x not in dict_1:
    plus_result.append((x, y))

print(plus_result)

minus_result = []

for x, y in dict_1.items():
  if x in dict_2:
    if y > dict_2[x]:
      minus_result.append((x, y - dict_2[x]))
    else:
      pass
  else:
    minus_result.append((x, y))

print(minus_result)