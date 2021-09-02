#https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    if position > 0 and  position != len(string)-1 :
        new_string = string[0:position]+character+string[position+1:]
    elif position == 0:
        new_string = character+string[1:]
    elif position == len(string)-1:
        new_string = string[:-1]+character
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)