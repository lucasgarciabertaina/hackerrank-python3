#https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    newString = ''
    j = 0
    for i in range(len(string)):
        j += 1
        if j % max_width == 0:
            newString += string[i]
            newString += '\n'
        else:
            newString += string[i]
    return newString

if __name__ == '__main__':
    print(wrap(input(),int(input())))
    