import oddeven_function


print("this app tells whether the given number is odd or even")
input_number = int(raw_input("please enter a number\n"))
if oddeven_function.odd_even(input_number) == 0:
    print("this number is even")
else:
    print("this number is odd")
