student ={
    "name":"Priti",
    "age":18,
    "city":"Mumbai"
}

print(student.keys())

print(student.values())

print(student.items())

print(student.get("name"))


#To Update
student.update({"age":19,"city":"Pune"})
print(student)

#To Remove
student.pop("city")
print(student)


#To Clear
student.clear()
print(student)