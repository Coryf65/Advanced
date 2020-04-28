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

    |type | info |
    | --- | ---- |
    | list []  | Mutable sequence of values |
    | tuple ,  | Fixed sequence of values |
    | set {}  | Sequence of distinct values, Mutable |
    | dictionary  | Colection of key-value pairs, Mutable |

2. Advanced Collections Module

    |type | info |
    | --- | ---- |
    | namedtuple  | Tuple with named fields |
    | OrderedDict, defaultdict  | Dictionaries with special properties |
    | counter  | Counts distinct values |
    | deque  | Double-ended list object |

# Advanced Classes

1. Things you can do with classes in python

    - Create enumerations

    - Customize string and byte representations of objects

        | String Function | Called When | What is it ? |
        | --------------- | ----------- | ------------ |
        | `object.__str__(self)` | str(object), print(object), "{0}", .format(object)  | nicely formatted human readable string |
        | `object.__repe__(self)`  | repr(object) | Try to return a python expression that could be used to recreate the object with the same values |
        | `object.__format__(self, format_spec)` | format(object, format_spec) | Up to you to implement the format object by spec |
        | `object.__bytes__(self)` | bytes(objects) | display your object in a bytes format |

    - Define computed and default attributes

        | Attribute Function | Called When |
        | ------------------ | ----------- |
        | `object.__getattribute__(self, attr)`  | ! object.attr  |
        | `object.__getattr__(self, attr)`  | object.attr |
        | `object.__setattr__(self, attr, val)`  | object.attr = val |
        | `object.__delattr__(self)`  | del object.attr |
        | `object.__dir__(self)`  | dir(object) |

        ! = python calls this when reading your class, be careful

    - Control how objects are logically compared to each other

        | Comparison Function | Called When |
        | ------------------ | ----------- |
        | `object.__gt__(self, other)`  | self > other  |
        | `object.__ge__(self, other)`  | self >= other  |
        | `object.__It__(self, other)`  | self < other  |
        | `object.__le__(self, other)`  | self <= other  |
        | `object.__eq__(self, other)`  | self == other  |
        | `object.__ne__(self, other)`  | self != other  |

    - Give objects numeric-like behavior (addition, subtraction, etc.)

        | Numeric Function | Called When |
        | ------------------ | ----------- |
        | `object.__add__(self, other)`  | self + other  |
        | `object.__sub__(self, other)`  | self - other  |
        | `object.__mul__(self, other)`  | self * other  |
        | `object.__div__(self, other)`  | self / other  |
        | `object.__floordiv__(self, other)`  | self // other  |
        | `object.__pow__(self, other)`  | self ** other  |
        | `object.__and__(self, other)`  | self & other  |
        | `object.__or__(self, other)`  | self | other  |
        etc.

# Logging (for debugging)

1. Why ?

    - Captures and records events while the app is running

    - Useful debugging feature

        - Not always practical to debug in realtime
    
    - Events can be categorized for easier analysis

    - Provides transaction record of a program's execution

    - Highly customizable

2. How ?

    - import logging

        - DEBUG `logging.debug("debug-level message")`, Diagnostic info useful for debugging
        - INFO `logging.info("info-level message")`, General info about program execution results
        - WARNING `logging.warning("warning-level message")`, Something, unexpected, or an approaching problem
        - ERROR `logging.error("error-level message")`, Unable to preform a specific operation due to a problem
        - CRITICAL `logging.critical("critical-level message")`, Program may not be able to continue, serious error

3. Write log messages to a log file example:

    ```Python
    demonstrate the logging api in Python


    # TODO: use the built-in logging module
    import logging

    def main():
        # TODO: Use basicConfig to configure logging, Normally only warning and below get displayed, in Append mode by default
        # level= which level and up to display messages for
        # filename= Filepath for a file to write to
        # filemode= Changed to 'w' to OverWrite everytime
        logging.basicConfig(level=logging.DEBUG,
                    filename="06 Logging/output.log",
                    filemode="w")

        # Try out each of the log levels
        logging.debug("This is a debug message")
        logging.info("This is a info message")

        # Normally only warning and below get displayed
        # BUT we can change this in the settings, logging.basicConfig()
        logging.warning("This is a warning message")
        logging.error("This is a error message")
        logging.critical("This is a critical message")

        # TODO: Output formatted strings to the log
        logging.info("Here is a variable {} and an int: {}".format("string", 10))


    if __name__ == "__main__":
        main()
    ```

4. Customized Logging

    - The basic config also takes these two args

        - `format=`  The format argument specifies a string that controls the precise formatting of the output message that is sent to the log.

        - `datefmt=`  The date format argument is used in conjunction with the format argument. 
            If the format argument contains a date specifier then the date format argument is used to format the date string using 
            the same kind of date formatting strings that you would pass to the strftime function. 

    ```Python
        basicConfig(
            format= formatstr,
            datefmt= date_format_str
        )
    ```

    | Some Useful Formats | About |
    | ------------------- | ----- |
    | `%(asctime)s`  | Human reable date format when the record was created  |
    | `%(filename)s`  | File name where the log message originated  |
    | `%(funcName)s`  | Function name where the log message originated from  |
    | `%(levelname)s`  | String representation of the message level  |
    | `%(levelno)d`  | Numeric repesentation of the message level  |
    | `%(lineno)d`  | Source line number where the logging call was issued (if available)  |
    | `%(message)s`  | The logged message string itself  |
    | `%(module)s`  | The Module name portion of the filename where the meddage was logged  |

5. Example with using custom loggging

```Python
# Demonstrate how to customize logging output

import logging

# global var to hold example special data, as a Dictionary
extData = {
    'user' : 'joem@example.com'
}

# TODO: add another function to log from
def anotherFunction():
    logging.debug("This is a debug message", extra=extData)


def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"

    datestr = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(filename="06 Logging/output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("This is an info-level log message", extra=extData)

    # example: 2020-04-27 19:23:39,048: WARNING: main Line:19 This is a warning-level message
    logging.warning("This is a warning-level message", extra=extData)

    # example: User:joem@example.com 04/27/2020 07:30:03 PM: DEBUG: anotherFunction Line:12 This is a debug message
    anotherFunction()


if __name__ == "__main__":
    main()

```


6. More very cool Advanced things

    [Python Docs - Logging](https://docs.python.org/3/howto/logging-cookbook.html)

# Python Comprehensions

    - A way to write python code in a different way

example:

*normal way*
```Python
    list(  map(FahrenheitToCelsius, [32, 65, 104, 212])  )
```

*Comprehension way, to write a list*
```Python
    [ (t*9/5) + 32   for t   in [32, 65, 104, 212])  ]
```