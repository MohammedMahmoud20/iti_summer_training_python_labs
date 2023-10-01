list_vowel=['a','e','o','u','i']
counter=0
sample=input("enter a string : ")
for i in sample:
    if(i in list_vowel):
        counter=counter+1
print(counter)