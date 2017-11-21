import fizzbuzzFunction as fb

input_number = int(raw_input("please enter a number\n"))

if fb.fizzbuzz(input_number) == 1:
    print("it's a FIZZ BUZZ!")
elif fb.fizzbuzz(input_number) == 2:
    print("it's a BUZZ!")
elif fb.fizzbuzz(input_number) == 3:
    print("it's a FIZZ!!!!")
