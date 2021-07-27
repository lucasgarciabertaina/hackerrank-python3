# https://www.hackerrank.com/challenges/python-lists/problem
def listOperation(lis, string):
    array = string.split()
    if array[0] == 'insert':
        lis.insert(int(array[1]), int(array[2]))
    elif array[0] == 'print':
        print(lis)
    elif array[0] == 'remove':
        lis.remove(int(array[1]))
    elif array[0] == 'append':
        lis.append(int(array[1]))
    elif array[0] == 'sort':
        lis.sort()
    elif array[0] == 'pop':
        lis.pop()
    elif array[0] == 'reverse':
        lis.reverse()


l = list([])
n = int(input())
for _ in range(n):
    listOperation(l, input())
