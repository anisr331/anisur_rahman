score =int(input("enter your number:"))
if (score < 0 or score >100):
    print("invlid number")
elif (score >0 and score < 33):
    print("f")
elif (score >32 and score < 40):
    print("D")
elif (score >39 and score <50):
    print("C")
elif (score > 49 and score < 60):
    print("B")
elif ( score >59 and score < 70):
    print("A-")
elif (score > 69 and  score < 80):
    print("A")
else:
    print("A+")