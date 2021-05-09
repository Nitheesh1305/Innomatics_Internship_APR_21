def swap_case(s):
    n = ''
    for char in s:
        if char.isupper():
            n += char.lower()
        else:    
            n += char.upper()
    return n

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)