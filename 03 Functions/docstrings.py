# Demonstrate the use of function docstrings

# put as first line in custom function
# """FunctionName(args, args2=None) --> Description of what this does!
#     Parameters:
#     args: Description of this arg
#     args2: decription, defaults to None
#"""

def myFunction(arg1, arg2=None):
    """myFunction(args, args2=None) --> Prints the values that you pass in!
        
    Parameters:
    args: Description of this arg
    args2: decription, defaults to None
    """
    print(arg1, arg2)


def main():
    # See the doc strings by running this!
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
