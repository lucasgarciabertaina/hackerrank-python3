#https://www.hackerrank.com/challenges/designer-door-mat/problem
height = int(input())
width = height*3
j = 3
patron = '.|.'
for i in range(height):
    string = width*'-'
    j += 3
    print(string[0:height+1]+string[height+1:(height*2)-j]+patron*(i+1)+string[height:height-j]+string[0:height+1])

print(len('------.|.---------------'))