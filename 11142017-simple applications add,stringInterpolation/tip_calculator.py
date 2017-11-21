total_amount = raw_input("please enter the total amount \n")
percentage = raw_input("please enter the tip percentage (0-100) you want to give \n")
TA = float(total_amount)
PE = int(percentage)
tip_amount = TA*PE/100
SUM = TA+tip_amount
message1= "the total_amount before tax is ${0},\n the percentage is {1}%,\n the tip amount is ${2},\n and the sum is ${3}".format(TA,PE,tip_amount,SUM)
print(message1)
