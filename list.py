fruits = ['apple', 'banana', 'orange', 'cherry']
cars = ['bmw', 'ford','toyota']
size= len(fruits)
print(fruits[-4:1])
print("before append",fruits)
fruits.append("blackberry")
print("after append",fruits)
x = fruits.copy()

print(x)

count_f = fruits.count("orange")
print(count_f)

fruits.extend(cars)
print(fruits)

p = fruits.index("banana")
print(p)

fruits.insert(3,"pineapple")
print(fruits)

fruits.pop(1)

fruits.remove("pineapple")
print(fruits)

print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()

print(fruits)