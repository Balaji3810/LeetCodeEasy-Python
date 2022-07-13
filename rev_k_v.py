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
