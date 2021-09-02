from itertools import combinations


def elements():
    lenElements = int(input())
    arrayEents = input().split(' ')
    ements = ''.join(arrayEents)
    while len(ements) != lenElements:
        arrayEents = input().split(' ')
        ements = ''.join(arrayEents)
    numberOfIndex = int(input())
    return ements, numberOfIndex


def combine(string, number):
    *comb, = combinations(string, number)
    return(comb)


def probability(comb):
    apper = 0
    confirmation = False
    for i in comb:
        for j in i:
            if j == 'a':
                confirmation = True
        if confirmation == True:
            apper += 1
            confirmation = False
    return "{0:.12}".format(apper/len(comb))


elmnts, nIndex = elements()
print(probability(combine(elmnts, nIndex)))
