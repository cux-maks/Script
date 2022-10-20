'''
1) 임의의 시퀀스 데이터가 주어졌을 때 중복을 제거하는 함수(my_func) 만들기
입력은 아래 x, y와 같은 시퀀스가 주어질 수 있으며 각 입력의 원소는 'int' 혹은 'str' 타입을 가질 수 있음
출력은 중복이 제거된 list가 반환되어야 함
2) 사전을 원소로만 갖는 임의의 시퀀스 데이터가 주어졌을 때 지정하는 key에 대응하는 value의 중복을 제거하는 함수(my_func2) 만들기
입력은 아래 x2, y2와 같은 시퀀스가 주어질 수 있으며 각 입력의 원소는 오직 사전 'dict' 타입만 가질 수 있음
함수(my_func2)의 또 다른 입력으로써 중복을 제거하길 원하는 key를 임의로 입력되어야 함
출력은 중복이 제거된 list가 반환되어야 함
'''

def my_func(a):
    return list(set(a))

def my_func2(a, key):

    def item_value(item, key):
        values = []
        for _key in key:
            values.append(item.get(_key))
        return tuple(values)

    result = []
    seen = set()

    for items in a:
        val = items if key is None else item_value(items, key)
        if val not in seen:
            result.append(items)
            seen.add(val)
        elif val == (None, ):
            result.append(items)
    return result    

x = [1, 5, 2, 1, 9, 1, 5, 10]
y = ['a', 'bc', 'a', 'b_', 123, 78, 'bc', '123', 123, 'b']

x2 = [
  {'a':1, 'b':1},
  {'a':1, 'b':2},
  {'a':1, 'b':1},
  {'a':2, 'b':2}
]
y2 = [
  {'a': 'x', 'b': 'y'}, 
  {'a': 'x1', 'b': 'y1'}, 
  {'a': 'x', 'b': 'y'}, 
  {'a': 'x1'}, 
  {'b': 'y1'}, 
  {'b': 'y2'}
]

x_ = my_func(x)
y_ = my_func(y)

print("print(my_func(x)) -> ", x_)
print("print(my_func(y)) -> ", y_)

x2_ = my_func2(x2, key = ('a', 'b'))
x22_ = my_func2(x2, key = ('a'))
y2_ = my_func2(y2, key = ('a', 'b'))
y22_ = my_func2(y2, key = ('a'))

print("print(my_func2(x2, key=('a', 'b'))) -> ", x2_)
print("print(my_func2(x2, key=('a'))) -> ", x22_)
print("print(my_func2(y2, key=('a', 'b'))) -> ", y2_)
print("print(my_func2(y2, key=('a'))) -> ", y22_)