
def fibonacci(n):

    if n ==0:
        return 0
    elif n ==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    

print('Fibonacci Series till nth position...(enter n) ')
n = int(input('>'))
for i in range(n):
    print(fibonacci(i),end=' ')
print('\n')