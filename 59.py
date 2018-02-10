a = [1, 2, 3] 


# i = 0
# for e in a:
#     print("Item {0} has index {1}".format(e,i))
#     i += 1

for index, item in enumerate(a):
    print("Item %s has index %s"%(item, index))