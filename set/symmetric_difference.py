# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
n_emts = set(map(int, input().split()))
m = int(input())
m_emts = set(map(int, input().split()))
symmetric = n_emts ^ m_emts
for _ in range(len(symmetric)):
    minime = min(symmetric)
    print(minime)
    symmetric.discard(minime)
