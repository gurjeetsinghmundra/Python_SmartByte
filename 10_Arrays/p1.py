
import array


numbers = array.array('i',[10,20,30,40,30])

# i for integer
# f for float
# u for unicode character ('a', 'b' etc)


print(numbers)

# Access by index 
# will print the element at index 2
print(numbers[2])


numbers.append(50)  # adding an element at the end
print(numbers)

numbers.pop()
print(numbers)  # removing the last element


print(len(numbers))  # length of the array


numbers.insert(2,14)    # inserting 14 at index 2
print(numbers)


numbers.remove(30)   # removing the first occurrence of 30
print(numbers)