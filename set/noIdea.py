# https://www.hackerrank.com/challenges/no-idea/problem
import collections


def happy():
    n, m = map(int, input().split())
    elements = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    interA = (set(elements) & a)
    interB = (set(elements) & b)
    ab = (interA | interB)
    happines = []
    elements.sort()
    counter = 0
    for e in collections.Counter(elements).items():
        for i in list(ab):
            if e[0] == i:
                happines.append(e[1])
    for j in range(len(happines)):
        if j < len(interA):
            counter += happines[j]
        else:
            counter -= happines[j]
    return counter


print(happy())
"""
def happines(array):
    elements = list(listInt())
    a = set(listInt())
    b = set(listInt())
    happy = 0
    interA = list(({*elements, } & a))
    interB = list(({*elements, } & b))
    for j in interA:
        happy += elements.count(j)
    for k in interB:
        happy -= elements.count(k)
    return happy


print(happines(list(listInt())))
"""
