def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    num = input(prompt)
    try:
        num = int(num)
        assert num < max and num > min
    except AssertionError:
        print("Error: number not in range")
    except ValueError:
        print("Error: wrong input")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
