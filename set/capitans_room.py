# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import collections


def capitansRoom(listRooms):
    for elements in collections.Counter(listRooms).items():
        if elements[1] == 1:
            return elements[0]


k = int(input())
n = map(int, input().split())
print(capitansRoom(n))
