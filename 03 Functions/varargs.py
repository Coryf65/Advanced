# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
# *args is more of a naming convention
def addition(base, *args):
    result = 0
    for arg in args:
        result += arg

    return result


def main():
    # TODO: pass different arguments
    print(addition())

    # TODO: pass an existing list


if __name__ == "__main__":
    main()
