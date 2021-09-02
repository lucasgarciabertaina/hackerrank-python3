# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
e = int(input())
e_stu = set(map(int, input().split()))
f = int(input())
f_stu = set(map(int, input().split()))
print(len(e_stu & f_stu))
