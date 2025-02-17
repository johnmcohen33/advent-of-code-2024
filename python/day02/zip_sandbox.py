list = [1, 2, 3, 4]
# list0 = [1. 2, 3, 4]
# list1 = [2, 3, 4]
# returns = [(1,2), (2,3), (3, 4)]
zippedList = [(a, b) for a,b in zip(list, list[1:])]
print(zippedList)