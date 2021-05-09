def solve(s):

    for substring in s.split():

        s = s.replace(substring, substring.capitalize())
    
    return s 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()