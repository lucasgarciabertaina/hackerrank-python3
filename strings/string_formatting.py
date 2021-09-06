#https://www.hackerrank.com/challenges/python-string-formatting/problem
decimal = [0,1,2,3,4,5,6,7,8,9]
octal = [0,1,2,3,4,5,6,7]
binary = [0,1]
number = '0'


def numberArray(number):
    array = [digit for digit in str(number)]
    return array

"""
def verificator(array,arrayElemtns,times,change):
    if array[arrayElemtns:] == [0 for i in range(arrayElemtns)] and ''.join(array).count('1') == times:
        array[-1] = '1'e
        number = ''.join(arrayNumber)
        print(number, i)
"""

def binary(decimalNumber):
    number = ''
    for i in range(decimalNumber):
        arrayNumber = numberArray(number)
        if i == 0 or i == 1:
            number = str(i)
            print(number, i)
        elif number.count('1') == len(number):
            number = number.replace('1','0')
            arrayNumber = numberArray(number)
            arrayNumber[0] = '1'
            arrayNumber.append('0')
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-1] == '0' and number.count('1') == 1:
            arrayNumber[-1] = '1'
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-2:] == ['0','0'] and number.count('1') == 2:
            arrayNumber[-1] = '1'
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-1] == '1' and arrayNumber[-2] == '0':
            arrayNumber[-2] = '1'
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-2:] == ['1','1'] and arrayNumber[-3] == '0':
            arrayNumber[-3] = '1'
            arrayNumber[-2:] = ['0','0']
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-3:] == ['1','1','1'] and arrayNumber[-4] == '0':
            arrayNumber[-4] = '1'
            arrayNumber[-3:] = ['0','0','0']
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-2:] == ['0','0'] and number.count('1') == 3:
            arrayNumber[-1] = '1'
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-4:] == ['1','1','1','1'] and arrayNumber[-5] == '0':
            arrayNumber[-5] = '1'
            arrayNumber[-4:]  = ['0','0','0','0']
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-2:] == ['0','0'] and number.count('1') == 4:
            arrayNumber[-1] = '1'
            number = ''.join(arrayNumber)
            print(number, i)
        elif arrayNumber[-5:] == ['1','1','1','1','1'] and arrayNumber[-6] == '0':
            arrayNumber[-6] == '1'
            arrayNumber[-5:]  = ['0','0','0','0','0']
            number = ''.join(arrayNumber)
            print(number, i)

def replaceNumber(numbers,number,numberReplace):
    invertArray = [str(numbers)[n] for n in range(len(numbers)-1,-1,-1)]
    invertArray[invertArray.index(numberReplace)] = number
    array = [invertArray[n] for n in range(len(invertArray)-1,-1,-1)]
    return ''.join(array)

def octal(decimalNumber):
    for i in range(decimalNumber):
        if i < 10:
            number = str(i)
            print(number)
        elif i%16 == 0:
            number = '1'+'0'*len(str(number))
            print(number)
        elif i%10 == 0:
            number = replaceNumber(number,'A','9')
            print(number)
            


octal(17)