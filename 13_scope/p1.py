# Local Scope 
# Variable created inside a function
# Only accessible within that function

def fun():
    x=10  # Local variable
    print("Inside function:", x)


fun()

print("Outside function:", x)  # Error: x is not defined"