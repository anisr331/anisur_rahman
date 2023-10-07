name = "anis"
phone = "01642397176"
email = "a"

size_name =len(name)
size_phone = len(phone)
size_email = len(email)
print(size_name)

if(size_name ==0 or size_phone ==0 or size_email ==0):
    print("the filed cannot be empty")
else:
    
    if size_name <4:
    
        print("the name must be minimum 4")
    elif size_phone !=11:
        print("phone number must be 11")
    else: 
        print("success")