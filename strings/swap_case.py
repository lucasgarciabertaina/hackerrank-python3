#https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(string):
    invertString = ''
    for letter in string:
        if letter.islower():
            invertString += letter.upper()
        elif letter.isupper():
            invertString += letter.lower()
        else:
            invertString += letter
    return invertString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)