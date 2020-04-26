# use transform functions like sorted, filter, map

# Checks if the given nums are divisible by 2 evenly
def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

# checks for if the given value is an uppercase
def filterFunc2(x):
    if x.isupper():
        return False
    return True

# returns X^2
def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return 'A'
    elif (x >= 80 and x < 90):
        return 'B'
    elif (x >= 70 and x < 80):
        return 'C'
    elif (x >= 65 and x < 70):
        return 'D'
    return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    odd_nums = list(filter(filterFunc, nums))
    print("odds: ", odd_nums)

    # TODO: use filter on non-numeric sequence
    lower_chars = list(filter(filterFunc2, chars))
    print("lower case values: ", lower_chars)

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print("Squares: ", squares)

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    letter_grade = list(map(toGrade, grades))
    print("Letter Grades: ", letter_grade)


if __name__ == "__main__":
    main()
