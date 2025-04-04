# First, define a function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use the filter
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)