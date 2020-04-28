# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # list version
    ftemps_list = [(t*9/5)+32 for t in ctemps]
    ftemps_set = {(t*9/5)+32 for t in ctemps}

    # printing each one
    print("List: ", ftemps_list)
    # List:  [41.0, 50.0, 53.6, 57.2, 50.0, 73.4, 105.8, 86.0, 53.6, 75.2, 53.6, 64.4, 84.2]

    print("Set: ", ftemps_set)
    # Set:  {64.4, 73.4, 41.0, 105.8, 75.2, 50.0, 84.2, 53.6, 86.0, 57.2}
    # these Sets have no dupes!

    # TODO: build a set of unique Fahrenheit temperatures, no dupes !

    # TODO: build a set from an input source, convert all the chars to upperase, also removing the space character
    sTemp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)

if __name__ == "__main__":
    main()
