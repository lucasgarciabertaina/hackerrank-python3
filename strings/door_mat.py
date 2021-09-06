#https://www.hackerrank.com/challenges/designer-door-mat/problem
height,width = input().split(' ')
height = int(height)
width = int(width)
j = 3
patron = '.|.'
for i in range(int(height/2)):
    if i == 0:
        string = '-'*(int(width/2)-1)+patron+'-'*(int(width/2)-1)
    else:
        string = '-'*(int(width/2)-(1+j))+patron*i+patron+patron*i +'-'*(int(width/2)-(1+j))
        j += 3
    print(string)
print('-'*(int(width/2)-3)+'WELCOME'+('-'*(int(width/2)-3)))
for i in range(int(height/2),-1,-1):
    if i != int(height/2):
        string = '-'*(int(width/2)-(1+j))+patron*i+patron+patron*i +'-'*(int(width/2)-(1+j))
        print(string)
    j -= 3
