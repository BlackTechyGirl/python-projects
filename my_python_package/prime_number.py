if __name__ == '__main__':
    num = int(input("Enter a number: "))

    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
