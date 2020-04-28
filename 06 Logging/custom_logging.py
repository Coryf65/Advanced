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
