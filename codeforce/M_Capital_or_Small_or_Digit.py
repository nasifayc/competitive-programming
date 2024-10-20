x = input()

if x.isdigit():
    print("IS DIGIT")
elif x.isalpha():
    print("ALPHA")
    if x.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")

    