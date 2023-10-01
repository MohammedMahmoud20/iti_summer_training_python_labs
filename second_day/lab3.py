def rev_string(str):
    newstr=str[::-1]
    return newstr
sample=input("enter a string : ")
if isinstance(sample,str):
    print(rev_string(sample))