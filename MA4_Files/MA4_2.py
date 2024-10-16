#!/usr/bin/env python3
from numba import njit
import time
import matplotlib.pyplot as plt
from person import Person


def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n-1) + fib_py(n-2)


@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

def time_fib_methods(n_values):
    times_py = []
    times_numba = []
    times_cpp = []
    
    for n in n_values:
        #Python
        start = time.perf_counter()
        fib_py(n)
        end = time.perf_counter()
        times_py.append(end - start)

        #Numba
        start = time.perf_counter()
        fib_numba(n)
        end = time.perf_counter()
        times_numba.append(end - start)

        #C++ 
        f = Person(n)
        start = time.perf_counter()
        f.fib()
        end = time.perf_counter()
        times_cpp.append(end - start)
    
    return times_py, times_numba, times_cpp

def plot_times(n_values, times_py, times_numba, times_cpp):
    plt.plot(n_values, times_py, label="Python", marker='o')
    plt.plot(n_values, times_numba, label="Numba", marker='x')
    plt.plot(n_values, times_cpp, label="C++", marker='s')
    
    plt.xlabel("Fibonacci Number n")
    plt.ylabel("Time (seconds)")
    plt.title("Fibonacci Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("fib_comparison.png")
    

def main():
	fib_numba(20)
	n_values = list(range(20, 25))
	times_py, times_numba, times_cpp = time_fib_methods(n_values)
	plot_times(n_values, times_py, times_numba, times_cpp)

if __name__ == '__main__':
    main()
