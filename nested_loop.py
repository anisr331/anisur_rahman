
list_2 =[[1,2,3,4],[5,6,7],[7,8,9,10]]
print(list_2[1][0])



for i in range(len(list_2)):
    print(list_2[i])
    for j in range(len(list_2[i])):
       print(list_2[i],[j])


for i in list_2:
    for j in i:
       print(j)