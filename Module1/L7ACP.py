ch = input("Enter a character: ")

if len(ch) == 1:
    ascii_value = ord(ch)
    print("The ASCII value of", ch, "is", ascii_value)
else:
    print("Please enter only a single character.")