# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")

    p1 = Point(10,20)
    p2 = Point(30,40)

    print("\n")

    print(p1, p2)
    # output = Point(x=10, y=20) Point(x=30, y=40)

    # could also do this!
    print("\n p1's x value: ", p1.x, "\n p2's y value: ", p2.y)

    # TODO: use _replace to create a new instance
    p1 = p1._replace(x=100)

    print("replacing: ", p1)


if __name__ == "__main__":
    main()
