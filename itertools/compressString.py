# https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby


def group(string):
    groups = []
    uniquekeys = []
    for k, g in groupby(string):
        groups.append(list(g))
        uniquekeys.append(int(k))
    return groups, uniquekeys


def doTup(group, keys):
    tup = ''
    j = 0
    for i in keys:
        tup += str((len(group[j]), i))+' '
        j += 1
    print(tup)


g, k = group(input())
doTup(g, k)
