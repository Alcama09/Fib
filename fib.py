import argparse


def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    :param n: i-th Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to 0.")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    nth = 0
    for _ in range(n - 1):
        nth = n1 + n0
        n0 = n1
        n1 = nth
    return nth


from functools import cache

@cache
def fibonacci_recursive(n: int) -> int:
    """
    Computes the n-th Fibonacci number with memoization.
    :param n: i-th Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to 0.")
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    nth = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    cache[n] = nth
    return nth


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")
    args = parser.parse_args()
    # n = int(args[1])
    # Habria que ejecutarlo como python fig.py 9
    result = fibonacci_iterative(args.nth)
    print(result)
# Para saber cuanto tiempo tarda time y comando en la terminal
# para medir mehor time pyhton -c "codigo" salto de linea con ;
