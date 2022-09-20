from collections import Counter
cars = ["civic","camry","lexus","civic","acura","camry"]
cars_map = Counter(cars)
#print(cars_map)
dict2 = {}
rev_map = {v:k for k, v in cars_map.items()}
#print(rev_map)
for i in cars_map:
    dict2.setdefault(cars_map[i],[]).append(i)
print(dict2)

s="hello"
s1 = list(s)
print(s1)
s2 = {}
for i in s1:
    s2[i] = 1 + s2.get(i, 0)
print(s2)
s3 = {}
for k, v in s2.items():
    s3[v] =s2.get(v, []) + [k]
print(s3)
