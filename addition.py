
def add_two(n,n2):
    answer = int(n) + int(n2)
    print( "The sum of " + str(n) + " and " + str(n2)
           + " is " + str(answer))



# Do not change anything below these lines
def main():
    n = input("number")
    n2 = input("second number")
    add_two(n,n2)

if __name__ == '__main__':
    main()