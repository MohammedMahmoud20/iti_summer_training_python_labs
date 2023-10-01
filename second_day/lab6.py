total = 0
count = 0

while True:
    number = input("Enter a number : ")
    if number == "done":
        break
    if number.isnumeric():
        number=int(number)
        total += number
        count += 1
    else:
        print("Please enter a valid number : ")
average = total / count
print(f"the total is {total}, the count is {count} and the average is {average}")

