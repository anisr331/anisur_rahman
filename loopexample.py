

name = "anisur rahman"

list_bianary = []
list_binary_sum= []
for i in name:

    binary =(bin(ord(i)))
    binary = binary[2:]
    sum= 0
    for j in binary:
        sum=sum+int(j)
    list_binary_sum.append(sum)    
    list_bianary.append(binary)
print(list_bianary,list_binary_sum)