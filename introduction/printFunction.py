def printConsecutive(number):
    consecutive = ""
    for n in range(1, number+1):
        consecutive += str(n)
    print(consecutive)


n = int(input())
printConsecutive(n)
