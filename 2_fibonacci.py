def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = fibonacci_sequence(numero)
print(resultado)

# Optei por tentar fazer um código menor mas com a mesma resultante, e deu certo. O anterior era esse abaixo:

# def fibonacci_sequence(n):
#     fib_sequence = [0, 1]
    
#     while fib_sequence[-1] < n:
#         next_value = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_value)
        
#     return fib_sequence

# def is_in_fibonacci(n):
#     fib_sequence = fibonacci_sequence(n)
    
#     if n in fib_sequence:
#         return f"O número {n} pertence à sequência de Fibonacci."
#     else:
#         return f"O número {n} não pertence à sequência de Fibonacci."

# numero = int(input("Informe um número: "))
# resultado = is_in_fibonacci(numero)
# print(resultado)