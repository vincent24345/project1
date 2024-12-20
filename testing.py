#calculator 

#addition function
def add(a,b):
    return a+b
#subtraction funciton
def sub(a,b):
    return a-b
#multiplication function
def mult(a,b):
    return a *b
#division function
def div(a,b):
    if b == 0 :
        return "Error. Cannot be done"
    return a /b

#calculator 
def main():
    print("Welcome this is my calculator")
    print("The available operations:")
    print("addition : "+"")
    print("subtraction : "-"")
    print("division : "/"")
    print("multiplication : "*"")
    print("type exit to leave the calculator")

    while True :
        operation = input("")

#calling it
main()