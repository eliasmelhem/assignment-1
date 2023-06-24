value = 1000
prime = [x for x in range(2, value) if all(x % y != 0 for y in range(2, x))]
print(prime)