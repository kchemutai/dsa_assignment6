import random
import time
import matplotlib.pyplot as plt

def measure_time(func, arr, k):
    """
    Measures the execution time of the given function.
    """
    start = time.time()
    func(arr, k)
    return time.time() - start

# Generate input data of different sizes
input_sizes = [100, 1000, 5000, 10000, 20000]
times_deterministic = []
times_randomized = []

for size in input_sizes:
    arr = [random.randint(1, size) for _ in range(size)]
    k = random.randint(1, size)

    # Measure time for deterministic algorithm
    times_deterministic.append(measure_time(median_of_medians, arr, k))

    # Measure time for randomized algorithm
    times_randomized.append(measure_time(randomized_quickselect, arr, k))

# Plot the results
plt.plot(input_sizes, times_deterministic, label='Deterministic Algorithm (Median of Medians)')
plt.plot(input_sizes, times_randomized, label='Randomized Algorithm (Quickselect)')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Empirical Comparison of Selection Algorithms')
plt.legend()
plt.show()
