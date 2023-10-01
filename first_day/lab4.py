sample=input("enter a string : ")
vowels=['a','e','i','o','u']
new_sample=''
for i in sample.lower():
    if(i not in vowels):
        new_sample+=i
print(new_sample)