# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def case(option, se):
    if len(option) == 1:
        return se.pop()
    elif option[0] == 'discard':
        return se.discard(int(option[1]))
    else:
        return se.remove(int(option[1]))


n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    case(input().split(' '), s)

total = 0
for i in s:
    total += i
print(total)
