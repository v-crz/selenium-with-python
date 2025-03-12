
greeting = "Good morning"
a = 4

#if greeting == "morning":
if a > 2:
    print(" Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

# for loop
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of first natural numbers 1+2+3+4+5 = 15
print("\nSum of first natural numbers 1+2+3+4+5 = 15")
summation = 0
for j in range(1,6):    #range(i,j) -> i to j-1
    summation = summation + j
print(summation)

print("\n*******************")
for k in range(1, 10, 2):
    print(k)

print("\n**************** Skipping first index ****************")
for m in range(10):
    print(m)