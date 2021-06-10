# https://www.hackerrank.com/challenges/itertools-combinations/problem
from itertools import combinations


def inputOrder():
    elements = input().split(' ')
    return ''.join(sorted(elements[0])), int(elements[1])


def lexiSort(string, number):
    for n in range(1, number+1):
        *sort, = combinations(string, n)
        for element in sort:
            word = ''
            for w in element:
                word += w
            print(word)


stri, numb = inputOrder()
lexiSort(stri, numb)
