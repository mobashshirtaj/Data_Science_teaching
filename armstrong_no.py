def is_armstrong(num):
    temp, num_digits, sum_of_powers = num, len(str(num)), 0
    while temp > 0:
        sum_of_powers += (temp % 10) ** num_digits
        temp //= 10
    return sum_of_powers == num
result = is_armstrong(30)
print(result)
