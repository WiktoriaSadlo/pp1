with open("lorem_ipsum.txt") as file:
    while file.readline():
        for i in range(5):
            print(file.readline(), end="")
        input("Press to Continue")