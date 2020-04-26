# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)

    # move to the next item
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel

    # Processing from testfile.txt
    with open("02 BuiltIn_Functions/testfile.txt", "r") as fp:
        # it looks for the  empty string to indicate that is the end of our file
        for line in iter(fp.readline, ''):
            print(line)

    # TODO: use regular interation over the days
    for m in days:
        print(m)

    # starting at number one more complex than ness
    for m in range(len(days)):
        print(m+1, days[m])


    # TODO: using enumerate reduces code and provides a counter

    # using an enumerator can be more simple
    for i,m in enumerate(days, start=1):
        print(i, m)

    # TODO: use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)

    # TODO: use zip AND Enumerate
    for i,m  in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], '=', m[1], 'in French')


if __name__ == "__main__":
    main()
