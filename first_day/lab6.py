number = input()
if(number.isnumeric()):
    number=int(number)
lst = []
for i in range(1, number+1):
    row = []
    for j in range(1, i+1):
        row.append(i*j)
        lst.append(row)
print(lst[::2])
