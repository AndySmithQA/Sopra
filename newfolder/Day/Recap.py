while True:
    numbers = 0
    caps = 0
    lowers = 0
    syms = 0
    symbols = "';:£$%^&*"
    pw = input("Please enter Password")
    for chars in pw:
        if len(pw) < 8:
            print("Password too Short")
        else:
            if chars.isnumeric():
                numbers += 1
            elif chars.isupper():
                caps += 1
            elif chars.islower():
                lowers +=1
            elif chars in symbols:
                syms += 1
            else:
                print("PW contains an invalid character")

    if numbers < 1:
        print("PW contained no numbers")
    if caps < 1:
        print("PW contained no Capitals")
