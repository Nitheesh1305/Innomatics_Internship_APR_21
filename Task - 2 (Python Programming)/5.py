#Question 5 - Lists

if __name__ == '__main__':
    L = []
    N = int(input())
    for _ in range(N):
        input_command = input().split()
        command = input_command[0]
        arguments = input_command[1:]
        if (command != "print"):
            command += "("+ ",".join(arguments) +")"
            eval("L." + command)
        else:
            print(L)

#can be also done by writing elif ladder