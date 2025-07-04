def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Якщо результат вже в кеші - повертаємо його
        if n in cache:
            return cache[n]

        # Рекурсивний виклик та збереження у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci



if __name__ == "__main__":
    fib = caching_fibonacci()
    n = 10  # приклад: обчислити 10-е число Фібоначчі
    print(f"Fibonacci({n}) = {fib(n)}")
