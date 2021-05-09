def print_full_name(first, last):
    first_name = first
    last_name = last
    
    print("Hello", first_name, last_name + "!", "You just delved into python.")

if __name__ == '__main__':
        first_name = input()
        last_name = input()
        print_full_name(first_name, last_name)