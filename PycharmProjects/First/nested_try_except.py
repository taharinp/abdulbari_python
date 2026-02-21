l = [1,2,3,4,5]

try:

    try:
        index = int(input("Enter index: "))

    except ValueError as e:
        print("Error:", e)
        index = 0   # default value

    print(l[index])

except IndexError as e:
    print("Error:", e)

except Exception as e:
    print("Error:", e)