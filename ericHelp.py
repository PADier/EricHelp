def sum(x, y):
    output = int(x) + int(y) 
    print(output) 
    

def calculate(x, y, operand):
    if(operand == "Add"):
        output = int(x) + int(y) 

    print(output) 


firstInt = input("Enter a number: ")
secondInt = input("Enter a number: ")
operandInput = input("Enter a operation: ")


sum(firstInt, secondInt)
calculate(firstInt, secondInt, operandInput)

test