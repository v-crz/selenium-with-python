
values = [1, 2, "name", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0]) # 1
print(values[3]) # 4
print(values[-1]) # 5
print(values[1:3]) # 2 name


values.insert(3, "shetty") # [1, 2, 'name', 'shetty', 4, 5]
print(values)
values.append("End")    # [1, 2, 'name', 'shetty', 4, 5, 'End']
print(values)

values[2] = "NAME" # Updating position 2
print(values)

del values[0]   # [2, 'NAME', 'shetty', 4, 5, 'End']
print(values)

# Tuple - Same as List data type but immutable
val = (1, 2, "name", 4.5)
print(val[1])
# val[2] = "NAME"
print(val)


# Dictionary
dic = {
    "a": 2,
    4: "bcd",
    "c": "hello world"
}
print(dic[4])
print(dic["c"])


#
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "shetty"
dict["gender"] = "Male"
print(dict)
print(dict["lastname"])