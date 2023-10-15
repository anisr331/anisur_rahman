fruits = ['apple', 'banana', 'orange', 'cherry']
fruits_size = len(fruits)
print(fruits[0])

for i in range(fruits_size):
    print(i,fruits[i])

for i in fruits:
    print(i)


dict1 ={"name":"anisur rahman","roll":16}

for i in dict1.items():
    print(i)

list1 =[]
num = int(input("how many values you want to keep in your list:"))
for i in range(num):
    x = int(input("give your list value:"))
    list1.append(x)

sum = 0
for i in list1:
    sum=sum+i
print(sum)

sum = 1
for i in list1:
    sum=sum*i
print(sum)

if(sum%2==0):
    print("the value is even")

else:
    print("the value is odd")


print(list1)