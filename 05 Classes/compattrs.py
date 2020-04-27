# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)            
        elif attr == "hexcolor":
            # creates the Hex conversion on the fly
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
            # puts # before the color, which is for CSS
            # each number is represented by a 2 character hex string
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            # always make sure to cal the super class
            super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return("red", "green", "blue", "rgbcolor", "hexcolor")

def main():
    # create an instance of myColor
    cls1 = myColor()
    print("\n")
    # TODO: print the value of a computed attribute
    # print RGB version
    print("rgb version: ", cls1.rgbcolor)
    # print Hexadecimal version
    print("Hex version: ", cls1.hexcolor)

    # TODO: set the value of a computed attribute
    print("\n")
    print("set to a new color")
    cls1.rgbcolor = (16, 200, 89)
    print("rgb version: ", cls1.rgbcolor)
    print("Hex version: ", cls1.hexcolor)


    # TODO: access a regular attribute
    print("\naccess a regular attribute")
    print(cls1.red)

    # TODO: list the available attributes
    print("\nshowing dir(), list of attributes my object supports")
    print(dir(cls1))


if __name__ == "__main__":
    main()
