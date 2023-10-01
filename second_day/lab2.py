def number_div(num):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num %3==0:
        print("Fizz")
    elif num % 5==0 :
        print("buzz")
number=input("enter a number: ")
if(number.isnumeric()):
    number=int(number)
number_div(number)
