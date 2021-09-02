# https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen
def setOperation(a_list, n_list, operation):
    if operation == 'update':
        a_list.update(n_list)
    elif operation == 'intersection_update':
        a_list.intersection_update(n_list)
    elif operation == 'difference_update':
        a_list.difference_update(n_list)
    elif operation == 'symmetric_difference_update':
        a_list.symmetric_difference_update(n_list)
    return a


a_elmts = int(input())
a = set(input().split())
for _ in range(int(input())):
    setMutation, lengh = input().split()
    n = set(input().split())
    a = setOperation(a, n, setMutation)
total = 0
for i in [*a, ]:
    total += int(i)

print(total)
