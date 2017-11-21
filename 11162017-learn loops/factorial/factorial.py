
try:
    input_number = int(raw_input("please enter an integer\n"))
except ValueError:
    print("Hey you cannot enter alphabets")
except FileNotFound:
    print("File not found")

else:
    print("no exceptions to be reported")

# result = 1
# for index in range (1, input_number+1):
#     result = result * index
#
# print("The factorial of " + str(input_number) + " is " + str(result))
