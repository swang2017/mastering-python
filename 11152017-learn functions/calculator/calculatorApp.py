
import calculator_helper as calculator
While True:
    input1 = float(raw_input("please enter the first number\n"))
    input2 = raw_input("please enter the operand\n")
    input3 = float(raw_input("please enter the second number\n"))

    if input2 == "+":
        calculator.add(input1,input3)
    elif input2 == "-":
        calculator.subtract(input1,input3)
    elif input2 == "*":
        calculator.time(input1,input3)
    elif input2 == "/":
        calculator.divide(input1,input3)

    choice = raw_input("Press q to quit")
    if choice == "q":
        break    
