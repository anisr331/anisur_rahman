# size =len("anisur rahman")

# name = "anisur rahman"
# count=0
# for i in name:
#     count=count+1
# print(count)

# def size (x):
#     count= 0
#     for i in x:
#         count=count+1
#     return(count)
    


# name=input("enter your name: ")
# size=size(name)
# print(size)


def key_dic(x):
    l = []
    for i in x:
        l.append(x[i])
    return l

dict1= {"a":10,"b":20}
result=key_dic(dict1)
print(result)