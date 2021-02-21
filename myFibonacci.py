def fibonacci(num):
    if num == 1:
        return 1
    lst = [1,1]
    for i in range(2,num +1):
        number = lst[i - 2] + lst[i - 1]
        lst.append(number)
    return lst[num - 1]

for num in range(1, 10):
    print(num, "->", fibonacci(num))
        
        