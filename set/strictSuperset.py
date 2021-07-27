# https://www.hackerrank.com/challenges/py-check-subset/problem
def strictSubset(a, listOfSubsets):
    lenA = len(a)
    for i in listOfSubsets:
        if lenA < len(i):
            return False
        for j in i:
            a.add(j)
            if lenA != len(a):
                return False
    return True


setA = set(map(int, input().split()))
n = int(input())
otherSets = []
for i in range(n):
    otherSets.append(set(map(int, input().split())))
print(strictSubset(setA, otherSets))
