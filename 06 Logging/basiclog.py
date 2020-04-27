# demonstrate the logging api in Python


# TODO: use the built-in logging module
import logging

def main():
    # TODO: Use basicConfig to configure logging, Now it displays all messages
    # in Append mode by default
    logging.basicConfig(level=logging.DEBUG,
                        filename="06 Logging/output.log",
                        filemode="w")

    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")

    # Normally only warning and below get displayed
    # BUT we can change this in the settings
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    # TODO: Output formatted strings to the log
    logging.info("Here is a variable {} and an int: {}".format("string", 10))


if __name__ == "__main__":
    main()
