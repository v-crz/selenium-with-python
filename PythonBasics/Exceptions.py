ItemsInCart = 0

#2 items will be added to cart
if ItemsInCart != 2:
    # raise Exception("Products Cart count not matching")
    pass

# assert(ItemsInCart == 2)    # Fails
assert(ItemsInCart == 0)

# try, catch
try:
    with open('filelog.txt', 'r') as reader:    #Fail
    # with open('test.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    # print("Some how I reached this block because there ir failure in try block")
    print(e)

finally:    #No matter if the except is executed
    print("Cleaning up resources")