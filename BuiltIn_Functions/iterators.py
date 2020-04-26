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
    with open("testfile.txt", "r") as fp:
        # it looks for the  empty string to indicate that is the end of our file
        for line in iter(fp.readline, ''):
            print(line)

    # TODO: use regular interation over the days

    # TODO: using enumerate reduces code and provides a counter

    # TODO: use zip to combine sequences


if __name__ == "__main__":
    main()
