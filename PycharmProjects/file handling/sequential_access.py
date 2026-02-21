with open('data','r') as file:
    ch1 = file.read(1)
    print(ch1)
    ch2 = file.read(4)
    print(ch2)
    ch3=file.read()
    print(ch3)