for i in range(1,5,2):
  print(i)

list1 = ["apple","banana","cherry","orange","pineapple"]

list1_size= len(list1)
print(list1[2])
for i in range(list1_size):
  print(i,list1[i])
for i in list1:
    print(i)

dict1 = {"name":"anisur","roll":16}
for i in dict1.items():
    print(i)

list2 = []
num=int(input("how many values you want to keep in your list: "))
for i in range(num):
    x =int(input("give yor values: "))
    list2.append(x)
print(i)

sum = 0
for i in list2:
    sum=sum+i
print(sum)

if(sum%2==0):
    print("the values is even")
else:
    print("the number is odd")

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist= []
# for i in fruits:
#     if "b" in i:
#       newlist.append(i)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[i for i in fruits  if "a" in i]
# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =(i for i in fruits if i != "banana")
print(newlist)