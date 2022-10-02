def iterate():
    counter = 1
    while counter != 3:
        grade = int(input("Input a grade: "))
        if 0 < grade > 100:
            print("Wrong input.", grade)
        elif grade >= 90:
            print("A")
        elif grade >= 70:
            print("B")
        elif grade >= 50:
            print("C")
        elif grade >= 40:
            print("D")
        elif grade >= 30:
            print("E")
        # else:
        #     print("ZERO TALENT!!!")
        counter += 1

if __name__ == "__main__":
        iterate()