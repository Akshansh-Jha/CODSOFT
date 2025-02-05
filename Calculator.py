print ("*****CALCULATOR*****")

num1=float (input("Enter the First value: "))
num2=float (input("Enter the Second value:"))
operation=input("""Enter the operation: 
For Addition:-              (+)
For Devision:-              (/)
For Subtraction:-         (-)
For Multiplacation:-    (*) """)
if operation=="+":
  print(num1+num2)
elif operation=="-":
  print(num1-num2)
elif operation=="*":
  print (num1*num2)
elif operation=="/":
  print (num1/num2)
else:
  print("You Enter an Invaled opreater.")
