# Demonstrate the use of keyword-only arguments

# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, suppressExceptions=False):
    print(arg1, arg2, suppressExceptions)

def main():
    # try to call the function without the keyword
    # throws error, TypeError: myFunction() takes 2 positional arguments but 3 were given
    # myFunction(1, 2, True)

    # now that this function uses a Keyword Arg we need to specify
    myFunction(1, 2, suppressExceptions=True)

if __name__ == "__main__":
    main()
