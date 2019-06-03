SPECIAL = ('!', '@', '#', '$', '%', '^', '&', '*')
MIN_LENGTH = 8
subStrNumbers = ""
subStrAlpha = ""
subStrLowAlpha = ""
subStrUpAlpha = ""
subStrSpecial = ""
valid = False

while not valid:
    print(
    """ 
            Password Analyzer
    
    Rules:
    Password must contain a MINIMUM of 8 characters. 
    Password CANNOT contain any spaces.
    Password must also contain:
        at least 1 number,
        at least 1 lowercase character,
        at least 1 uppercase character,
        and at least 1 special (!@#$%^&*) character

    """)

    while not valid:
        password1 = input("Enter password: ")
        password2 = input("Confirm password: ")
        if password1 != password2:
            print('Passwords do not match! Try again.')
        elif len(password1) < MIN_LENGTH:
            print('Password must contain a MINIMUM of 8 characters!')
        elif " " in password1:
            print('Password cannot contain spaces!')
        else:
            valid = True

    for char in password1:
        if char.isnumeric():
            subStrNumbers += char
        elif char in SPECIAL:
            subStrSpecial += char
        elif char.isalpha:
            subStrAlpha += char

    for char in subStrAlpha:
        if char.isupper():
            subStrUpAlpha += char
        else:
            subStrLowAlpha += char

    if len(subStrNumbers) > 0 and len(subStrSpecial) > 0 and len(subStrLowAlpha) > 0 and len(subStrUpAlpha) > 0 and valid:
        print('Password ACCEPTED')
    else:
        print('Password is NOT VALID!')
        print('Please try again and follow the rules for creating a password')
        valid = False

input('\n\nPress ENTER to exit')
