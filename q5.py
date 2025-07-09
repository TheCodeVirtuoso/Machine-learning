import random
import statistics

def analyze_random_numbers():
    nums = [random.randint(100, 150) for _ in range(100)]
    print(f"Numbers: {nums}")
    print("Mean:", statistics.mean(nums))
    print("Median:", statistics.median(nums))
    try:
        print("Mode:", statistics.mode(nums))
    except statistics.StatisticsError:
        print("No unique mode found.")

analyze_random_numbers()
