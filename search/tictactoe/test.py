board = [[1, 1, 1], [1, 1, 1], [1, 0, 1]]
if all(map(lambda x: all(x), board)):
    print("True")
else:
    print("False")