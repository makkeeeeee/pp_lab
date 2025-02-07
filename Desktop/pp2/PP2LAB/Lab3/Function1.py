import random
from itertools import permutations

# 1. Grams to ounces
def g_to_o(g):
    return 28.3495231 * g

# 2. Fahrenheit to Celsius
def f_to_c(f):
    return (5 / 9) * (f - 32)

# 3. Solve chicken - rabbit puzzle
def solve(h, l):
    for c in range(h + 1):
        r = h - c
        if 2 * c + 4 * r == l:
            return c, r
    return None

# 4. Filter primes
def filter_p(nums):
    return [n for n in nums if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))]

# 5. Print string permutations
def print_perm(s):
    for p in permutations(s):
        print(''.join(p))

# 6. Reverse sentence words
def rev_words(s):
    return ' '.join(s.split()[::-1])

# 7. Check for adjacent 3s
def has_33(nums):
    return any(nums[i] == nums[i + 1] == 3 for i in range(len(nums) - 1))

# 8. Check for 007 sequence
def spy_game(nums):
    code = [0, 0, 7]
    i = 0
    for n in nums:
        if n == code[i]:
            i += 1
            if i == 3:
                return True
    return False

# 9. Sphere volume
def sphere_vol(r):
    return (4 / 3) * 3.14159 * r ** 3

# 10. Get unique list
def unique_lst(lst):
    u = []
    for i in lst:
        if i not in u:
            u.append(i)
    return u

# 11. Check palindrome
def is_pal(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 12. Print histogram
def hist(lst):
    for n in lst:
        print('*' * n)

# 13. Guess number game
def guess_num():
    name = input("Hi! What's your name?\n")
    print(f"Hey, {name}, I'm thinking of a num from 1 - 20.")
    num = random.randint(1, 20)
    tries = 0
    while True:
        guess = int(input("Take a guess.\n"))
        tries += 1
        if guess < num:
            print("Too low.")
        elif guess > num:
            print("Too high.")
        else:
            print(f"Great, {name}! You got it in {tries} tries!")
            break