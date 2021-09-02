# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen
"""
def inputData():
    arr = []
    for i in range(int(input())):
        arr.append(input().split(' '))
    return arr, input()

def average(array, name):
    total = 0
    for element in array:
        if element[0] == name:
            for number in range(len(element)):
                if number != 0:
                    total += float(element[number])
    return "{:.2f}".format(total/3)


array, name = inputData()
print(average(array, name))
"""


student_marks = {}
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total = 0
for n in student_marks[query_name]:
    total += n
print("{:.2f}".format(total/3))
