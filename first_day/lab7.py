height = input()
if (height.isnumeric()):
    height=int(height)
for i in range(height):
    for j in range(height-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("#", end="")
    print()
