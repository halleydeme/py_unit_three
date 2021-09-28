
def area(a,b,c):
   s = a / 2 + b / 2 + c / 2
   A = (s * (s - a) * (s - b) * (s - c)) ** .5
   return A
def main():
    print(area(3,4,5))

main()
