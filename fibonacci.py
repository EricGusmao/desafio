"""
  Calculando por meio de recursão, porém utilizando iteração linear (ou Tail Recursion) como uma forma de otimização

  - Sem Iteração Linear: O(2^n)
  - Com Iteração Linear: O(n)

  Tomei como base o livro SICP (https://web.mit.edu/6.001/6.037/sicp.pdf) na Seção 1.2
"""


def fib_iter(current: int, previous: int, count: int) -> int:
    if count == 0:
        return previous
    return fib_iter(current + previous, current, count - 1)


def fib(n: int) -> int:
    return fib_iter(1, 0, n)


def is_fibonacci(num: int) -> bool:
    i = 0
    while True:
        fib_num = fib(i)
        if fib_num == num:
            return True
        elif fib_num > num:
            return False
        i += 1


if __name__ == "__main__":
    num = int(input("Informe um número: "))

    if is_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
