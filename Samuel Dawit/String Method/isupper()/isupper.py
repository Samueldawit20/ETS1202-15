
def check_is_upper(string):
    if string.isupper():
        print(f"The string '{string}' is completely uppercase!")
    else:
        print(f"The string '{string}' is NOT completely uppercase.")

check_is_upper("APPLE")   # Should print that the string is completely uppercase which in this case is true
check_is_upper("Apple")   # Should print that the string is NOT completely uppercase this time its false 
check_is_upper("125")   # Should print that the string is NOT completely uppercase this time its false
