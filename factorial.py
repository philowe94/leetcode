def factorial(n):
		if n <= 1:
				return 1

		return n * factorial(n - 1)

print(factorial(3))
# 3 * factorial(2)
# 3 * 2 * factorial(1)
# 3 * 2 * 1
# 3 * 2
# 6

def factorialiter(n):
		result = 1
		for i in range(1, n + 1):
				result *= i
		return result

print(factorialiter(3))