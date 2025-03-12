# read a file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:
    # content = reader.readlines()    #[abc, bvdsf, cat, dog, elephant]
    content = reader.read().splitlines()  # this will split each line
    reversed(content)   #[elephant, dog, cat, bvdsf, abc]
    with open('test.txt', 'w') as writer:   # file in 'w' mode will replace its current text save the file with new contents
        for line in reversed(content):
            writer.write(line + "\n")