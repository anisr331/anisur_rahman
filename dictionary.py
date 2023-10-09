dict1 ={"name":"anisur rahman","roll":16}

print(dict1["name"])

print(dict1["roll"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

x = dict1.get("name")
print(x)
dict1.pop("roll")
print(dict1)
dict1.popitem()
print(dict1)

dict1.update({"name":"rahad","roll":15})
print(dict1)