import time


# while True:
#     print("Hello")


# while True:
#     print("Hello")
#     time.sleep(2)

# i = 0
# while True:
#     i += 1
#     print("Hello")
#     time.sleep(i)
    

i = 0
while True:
    print("Hello")
    i += 1
    if i > 3:
        print("End of loop")
        break
    time.sleep(i)
