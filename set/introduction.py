# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    s = set(array)
    print(s)
    total = 0
    for i in s:
        total += i
    return '%.3f' % float(total/len(s))


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
