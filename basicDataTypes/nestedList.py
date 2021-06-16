# https://www.hackerrank.com/challenges/nested-list/problem
def inputValues():
    arr = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    return arr


def secondLowest(array):
    scores = [array[student][1] for student in range(len(array))]
    secLowest = list(dict.fromkeys(sorted(scores)))[1]
    position = [score for score in range(
        len(scores)) if scores[score] == secLowest]
    people = sorted([array[name][0] for name in position])
    resolt = ''
    for i in range(len(people)):
        if i != len(people)-1:
            resolt += people[i]+'\n'
        else:
            resolt += people[i]
    return resolt


print(secondLowest(inputValues()))
