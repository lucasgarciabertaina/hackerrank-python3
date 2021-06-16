# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
def inputData():
    n = int(input())
    while 2 >= n >= 10:
        n = int(input())
    *arr, = map(int, input().split(' '))
    while len(arr) != n:
        *arr, = map(int, input().split(' '))
    return sorted(arr)


def secondPlace(array):
    maxMin = []
    for i in range(len(array)-1, -1, -1):
        maxMin.append(array[i])
    for j in maxMin:
        if j != maxMin[0]:
            return j


print(secondPlace(inputData()))
