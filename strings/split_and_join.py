#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(string):
    array = string.split(" ")
    correctString = ''
    for i in array:
        if array.index(i) != len(array)-1:
            correctString += i
            correctString += '-'
        else:
            correctString += i
    return correctString

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)