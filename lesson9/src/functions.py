def add(a, b):
    return a + b

def division(a, b):
    return a / b

# 5! = 1 * 2 * 3 * 4 * 5
def factorial(n):
    """Calculate the factorial of n"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_anagram(word1, word2):
    """Check if two words are anagrams"""
    return sorted(word1) == sorted(word2)


def filter_even_numbers(numbers):
    """Filter even numbers from a list of numbers"""
    return [number for number in numbers if number % 2 == 0]


def find_primes(n):
    """Find all prime numbers up to n"""
    primes = []
    for number in range(2, n + 1):
        is_prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


def triangle_area(a, b, c):
    """Calculate the area of a triangle given its three sides"""
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def convert_to_24_hour(time_str):
    """Convert a time string to 24-hour format"""
    time, period = time_str.split()
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if period == "PM":
        hours += 12
    return f"{hours:02d}:{minutes:02d}"
