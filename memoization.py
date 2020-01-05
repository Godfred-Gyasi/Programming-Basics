import time, math

#Iterative Factorial
def iterativeFactorial(number):
    product = 1
    for value in range(number, 1, -1):
        product *= value
    return product

#Recursive Factorial
def factorialOne(number):
    if number <= 1:
        return 1
    else:
        return number * factorialOne(number - 1)

#Memoized recursive factorial
cache = {}
def factorialTwo(number):
    if number <= 1:
        return 1
    elif number in cache:
        return cache[number]
    else:
        result = number * factorialTwo(number - 1)
        cache[number] = result
        return result

start = time.time()
for num in range(100):
    print(factorialTwo(num))
print('[Finished in {} seconds]'.format(round(time.time() - start, 3)))