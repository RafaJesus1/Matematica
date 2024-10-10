# Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

# Input
# Read 3 floating-point numbers (double) A, B and C.

# Output
# Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a > 0:
    delta = ((b)**2) - 4 * (a * c)
    
    if delta < 0:
        print("A raiz quadrada de delta não pode ser negativa")
    
    if delta > 0:
        print(f"A raiz quadra do delta é {math.sqrt(delta):.2f}")
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"O cálculo do X1 é {x1:.2f}")
        print(f"O cálculo do X2 é {x2:.2f}")
    else:
        print("Por conta da raiz quadrada de delta ser negativa, não é possível calcular a bhaskara")
else:
    print("O a não pode ser menor que 0")



