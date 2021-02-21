def life():
    result = 0
    user = input ("Enter your date of birth in format DD MM YYYY: >")
    for i in user:
        user = user.replace(" ", "")
    try:
        userdate = [int(i) for i in user]
        for i in userdate:
            result += i
            if result > 9:
                sum_1 = result % 10
                sum_2 = result // 10
                result = sum_1 + sum_2
        print(result)
    except:
        print("Please enter a valid number")

life()