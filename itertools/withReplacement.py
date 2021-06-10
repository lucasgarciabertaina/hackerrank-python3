# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
from itertools import combinations_with_replacement


def inputOrder():
    elements = input().split(' ')
    return ''.join(sorted(elements[0])).upper(), int(elements[1])


def lexiSort(string, number):
    *sort, = combinations_with_replacement(string, number)
    for element in sort:
        word = ''
        for w in element:
            word += w
        print(word)


stri, numb = inputOrder()
lexiSort(stri, numb)
