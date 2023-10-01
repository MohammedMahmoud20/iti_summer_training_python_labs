sample=input("enter a string: ")
locations=[]
for i in range(len(sample)):
        if (sample[i] =='i'):
            locations.append(i)
print(locations)