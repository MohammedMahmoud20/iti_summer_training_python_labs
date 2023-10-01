from validate_email_address import validate_email
boole=False
while(boole==False):
    name=input("enter your name : ")
    if isinstance(name,str) and name !="" and not isinstance(name,int):
        boole=True
e_boole=False
while(e_boole==False):
    email=input("enter your email : ")
    if validate_email(email):
        e_boole=True
print(f"your name is {name} and your email is {email}")
