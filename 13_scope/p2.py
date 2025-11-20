# Global Scope
# Variable created outside functions
# Accessible anywhere in the program


x = 50 # Global variable

def fun():
    print("Inside function:", x)  # Accessing global variable

fun()
print("Outside function:", x)  # Accessing global variable