def is_prime(num):
#
# Write your code here.
#
    if num < 0:
        return False
    if num < 4:
        return True
    if num % 2 == 0:
        return False
    for i in range(4, num):
        if num % i == 0 and i < num:
            return False
        else:
            return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
