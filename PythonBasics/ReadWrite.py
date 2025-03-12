file = open('test.txt')
# Read all the contents of file
# print(file.read())

# Read n number of characters by passing parameter
# print(file.read(5))

#read one single line at a time readline()
# print(file.readline())
# print(file.readline())

#Print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#values = [abc, bvdsf, cat, dog, elephant]
for line in file.readlines():
    print(line)

file.close()