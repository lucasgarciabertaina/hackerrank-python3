def print_full_name(first, last):
    text = 'Hello first last! You just delved into python.'
    text = text.replace("first",first)
    text = text.replace("last",last)
    print(text)
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)