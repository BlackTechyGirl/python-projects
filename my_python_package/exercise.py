

if __name__ == "__main__":
    user_input = int(input('Enter a number: '))
    total_sum = 0
    # n = 1
    # print("The factors of {} are: ".format(r))
    # while n <= r:
    #     if r % n == 0:
    #         total = total + n
    #         print(n, ' ', end='')
    #     n = n + 1
    # print()
    # print("Sum of the factors of {} = {}".format(r, total))

    print("The factors of {} are: ".format(user_input))
    for x in range(1, user_input):
        if user_input % x == 0:
            total_sum += x
            # print(x)
            print(x, ' ', end='')
        x += 1
    print("\nSum of the factors of {} = {}".format(user_input, total_sum))

    if total_sum == user_input:
        print("This is a perfect number -:")
    else:
        print("zero talent")