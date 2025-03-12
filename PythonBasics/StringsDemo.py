str = "Google.com"
str1 = "web site"
str3 = "Google"

print(str[1]) #o

print(str[0:5]) #if you want substring in python

print(str + str1)   #concatenation

print(str3 in str)  #substring check

var = str.split(".")
print(var)
print(var[0])


str4 = " great "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())