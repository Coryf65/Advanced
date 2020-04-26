# Advanced_Python

- Follow along with me on Linkedin, 
[link](https://www.linkedin.com/learning/advanced-python)

# Python Language Features

### Coding Styles

- Style guide found on [Python Foundation](https://www.python.org/dev/peps/pep-0008/) website.

1. Structure and Format

    - Import Statements go at the top, and each have their own line

    - Indent with spaces Not tabs

    - Use four spaces for each indentation level

    - Limit lines to 79 characters (72 for doc string comments)

    - Seperate functions and classes by two blank lines

    - Within Classes, seperate methods by one blank line each

    - No spaces around function calls, indexes, keyword args

2. Whitespace Conventions

    - Avoid extraneous whitespace in the following situations:

    - Immediately inside parentheses, brackets or braces:

        ```Python
        # Correct:
        spam(ham[1], {eggs: 2})

        # Wrong:
        spam( ham[ 1 ], { eggs: 2 } )
        ```

    - Between a trailing comma and a following close parenthesis:

        ```Python
        # Correct:
        foo = (0,)

        # Wrong:
        bar = (0, )
        ```

    - Immediately before a comma, semicolon, or colon:

        ```Python
        # Correct:
        if x == 4: print x, y; x, y = y, x

        # Wrong:
        if x == 4 : print x , y ; x , y = y , x
        ```

    - However, in a slice the colon acts like a binary operator, and should have equal amounts on either side 
        (treating it as the operator with the lowest priority). 
        In an extended slice, both colons must have the same amount of spacing applied. Exception: 
        when a slice parameter is omitted, the space is omitted:

        ```Python
        # Correct:
        ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
        ham[lower:upper], ham[lower:upper:], ham[lower::step]
        ham[lower+offset : upper+offset]
        ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
        ham[lower + offset : upper + offset]

        # Wrong:
        ham[lower + offset:upper + offset]
        ham[1: 9], ham[1 :9], ham[1:9 :3]
        ham[lower : : upper]
        ham[ : upper]
        ```

    - Immediately before the open parenthesis that starts the argument list of a function call:


        ```Python
        # Correct:
        spam(1)

        # Wrong:
        spam (1)
        ```

    - Immediately before the open parenthesis that starts an indexing or slicing:

        ```Python
        # Correct:
        dct['key'] = lst[index]

        # Wrong:
        dct ['key'] = lst [index]
        ```

    - More than one space around an assignment (or other) operator to align it with another:

        ```Python
        # Correct:
        x = 1
        y = 2
        long_variable = 3

        # Wrong:
        x             = 1
        y             = 2
        long_variable = 3
        ```

3. Truth Value Testing

    -  In general, any object is considered to be equivalent to Boolean true, 
        unless it's class defines a Bool method that returns false, or has a len method that returns a zero length. 
    
    - False Values

        - False and None

        - Numeric 0 values

        - Decimal(0), Fraction(0, x)

        - Empty sequences / collections: '', (), [], {}

        - Empty sets and ranges: set(), range(0)

    - True Values

        - custom objects Unless they return a bool value of false

        ```Python
            class myClass:
              def __bool__(self):
                return false

              def __len__(self):
                return 0 
        ```
        
        | Boolean Operation  | Result |
        | ------------- | ------------- |
        | X and Y  | true if X and Y are both true  |
        | X or Y  | true if either X or Y are true  |
        | not X  | if X is false, then true, else false  |

4. Strings and Bytes

    - strings in Python 3 are a sequence of Unicode characters
    
    - bytes are a sequence of raw eight-bit values

# Advanced Python Functions

## Documenting Code

1. Using a Docstring

    - Enclose docstrings in triple quotes

    - First line should be a summary sentence of functionality

    - Modules: List the important classes, finctions, and exceptions

    - Classes: List important methods

    - Functions

        - List parameters and explain eaxh, one per line

        - if there's a return value, then list it; otherwise omit

        - If the function raises exceptions, mention those

2. Example

    - Documenting a Function

    ```Python
        def myFunction(arg1, arg2=None):
        """myFunction(args, args2=None) --> Prints the values that you pass in!
            
        Parameters:
        args: Description of this arg
        args2: decription, defaults to None
        """
        print(arg1, arg2)
    ```

    - To See Documentation about a module, class, method

    ```Python
        # function_name.__doc__
        print(myFunction.__doc__)
    ```

## Variable Argument lists

1. Define functions that can take variable number of parameters

    - example:

        ```Python
            def addition(*numbers)
        ```

    - a message logging func

        ```Python
            def log_message(msgType, msg, *args)
        ``` 
                
    - NOTE: *args is more of a naming convention,
        could be named whatever but other devs understand this naming

## Lambda Functions

- small anonymous functions

-  can be passed as arguments where you need a function

- Typically used in place just when needed

- Defined as:

    ```Python
        lambda (parameters) : (expression)
    ```

- Useful when running simple functions

- example:
    (converting Celsisus to Fahrenheit vice versa)

    ```Python
    def CelsisusToFahrenheit(temp):
        return (temp * 9/5) + 32


    def FahrenheitToCelsisus(temp):
        return (temp-32) * 5/9


    def main():
        ctemps = [0, 12, 34, 100]
        ftemps = [32, 65, 100, 212]

    
        print('\n Calling as Functions \n')

        print(list(map(FahrenheitToCelsisus, ftemps)))
        print(list(map(CelsisusToFahrenheit, ctemps)))

        print('\n Calling as Lamdas \n')    
    
        print(list(map(lambda t: (t-32) * 5/9, ftemps)))
        print(list(map(lambda t: (t * 9/5) + 32, ctemps)))

    if __name__ == "__main__":
        main()
    ```

# Advanced Collections

1. Basic Collections

    | ---|--- |
    | list []  | Mutable sequence of values  |
    | tuple ,  | Fixed sequence of values  |
    | set {}  | Sequence of distinct values, Mutable  |
    | dictionary  | Colection of key-value pairs, Mutable  |

2. Advanced Collections Module

    - use 'import collections'