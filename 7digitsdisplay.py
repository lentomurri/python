patterns = {
"0": ("###","# #", "# #", "# #", "###"),
"1": ("  #", "  #", "  #", "  #", "  #")
  }

numbers = ["0","1"]

digits = [patterns[i] for i in numbers]

for i in range(5):
    for num in digits:
        if digits.index(num) == len(digits) - 1:
            print(num[i], end = "\n")
        else:
            print(num[i], end = " ")

# print(digits)