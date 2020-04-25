# Advanced_Python

- Follow along with me on Linkedin
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
        In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted:

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