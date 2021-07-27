# https://www.hackerrank.com/challenges/py-check-subset/problem
def subConjunt(a, b):
    aList = [*a, ]
    lenB = len(b)
    for i in aList:
        b.add(i)
        if len(b) != lenB:
            return False
    return True


cases = int(input())
for i in range(cases):
    lenA = int(input())
    setA = set(map(int, input().split()))
    lenB = int(input())
    setB = set(map(int, input().split()))
    print(subConjunt(setA, setB))
