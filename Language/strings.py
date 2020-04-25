# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    
    # b'ABCD'
    print(b)
    
    s = "This is a string"
    
    # This is a string
    print(s)
    
    # TODO: Try combining them. 
    
    # TypeError: can only concatenate str (not "bytes") to str
    #print(s+b)
    
    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2 = b.decode('utf-8')
    # This is a stringABCD
    print(s+s2)

    b2 = s.encode('utf-8')
    # b'ABCDThis is a string'
    print(b+b2)
    
    # TODO: encode the string as UTF-32
    b3 = s.encode('utf-32')
    # b'\xff\xfe\x00\x00T\x00\x00\x00h\x00\x00\x00i\x00\x00\x00s\x00\x00\x00 \x00\x00\x00i\x00\x00\x00s\x00\x00\x00 
    # \x00\x00\x00a\x00\x00\x00 \x00\x00\x00s\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00n\x00\x00\x00g\x00\x00\x00'
    print(b3)


if __name__ == "__main__":
    main()
