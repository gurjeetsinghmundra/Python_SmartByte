colors = {"red","blue","green"}

print(colors)

# To add an element

colors.add("yellow")
print(colors)


colors.update(["black","white"])
print(colors)


# To remove an element
colors.remove("blue")
print(colors)   

colors.discard("green")
print(colors)


# Remove and return a random item
items = colors.pop()

print(items)
print(colors)


#clear (empty the set)


colors.clear()
print(colors)

