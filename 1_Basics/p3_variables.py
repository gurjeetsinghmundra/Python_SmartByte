#Type of Datas in Python
# Variable is a container to store different values


a=10;
b="Priti"
c=True
d=3.5
e=None

''' 
1) Integer: int (Numbers)
2) String: str (Text / Alphabets)
3) Boolean: bool (True / False)
4) Float: float    (Decimal Numbers)
5) NoneType: None (Null Value)

'''

# To check the type of variable we use type() function

print(type(a))
print(type(b))      
print(type(c))
print(type(d))
print(type(e))


#Assign Multiple Values

x,y,z=1,"Harshprit",3.5

# Output Variables
print(x, y,z)

a1 = "Python"
a2= "is " 
a3 = "Awesome"

print(a1 + a2 + a3)  # Concatenation of strings


# Global Variables

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)