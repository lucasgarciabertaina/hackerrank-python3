# https://www.hackerrank.com/challenges/list-comprehensions/problem
def intPrevNumbers(number):
    array = []
    for n in range(number+1):
        array.append(n)
    return array


x = intPrevNumbers(int(input()))
y = intPrevNumbers(int(input()))
z = intPrevNumbers(int(input()))
n = int(input())
my_list = [[i, j, k] for i in x for j in y for k in z if i+j+k != n]
print(my_list)
