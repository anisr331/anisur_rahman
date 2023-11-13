class Student :
    name =''
    status =''

    def __init__ (self):
        self.status="this is auto connection"
    def about (self,x):
        self.name = x
    def output (self):
        return self.status
st1 = Student()
st1.about =("anis")
st1.name = "anis"
st2 = Student()
st2.name = "rahman"
print(st1.name)
print(st2.name)