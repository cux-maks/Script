import operator

prices = {
  'ABC': 89.23,
  'KIUP BANK': 100.54,
  'SHINHAN BANK': 38.48,
  'SAMSUNG': 201.78,
  'LG': 200.45,
  'APPLE': 167.85,
  'TOMATO': 134.78,
  'KAKAO': 162.51,
  'NC': 87.12,
  'NEXON': 56.02,
}

prices_key = sorted(prices.items())
print("key sort 하위 5개: ", prices_key[0:5])
prices_key = prices_key[::-1]
print("key sort 상위 5개: ", prices_key[0:5])

prices_value = sorted(prices.items(), key=operator.itemgetter(1))
print("value sort 하위 5개: ", prices_value[0:5])
prices_value = prices_value[::-1]
print("value sort 하위 5개: ", prices_value[0:5])