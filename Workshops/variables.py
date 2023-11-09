# -----------------------------------------------------------
# Karl Melendez
# Date: 11/01/2023
#
# This program demonstrates the use of variables in Python.
# -----------------------------------------------------------


# Define Variables:
# In your Python file, define a variable for each primitive data type.

integer_variable = 42
float_variable = 3.14
string_variable = "Hello, world!"

# Concatenate Variables:
# Concatenate the variables with the correct type conversions and store the result in a new variable.

concatenated_string = str(integer_variable) + \
    str(float_variable) + string_variable

# Investigate Integer and Float Limits:
# You can add comments to your Python file with information about the limits of integers and floats in Python.

# Integer limit in Python
int_limit = 2**31 - 1  # On most systems

# Float limit in Python
float_limit = 1.8e308

# Sum of First n Even Numbers:
# Research and apply the formula to calculate the sum of the first 'n' even numbers. Use the integer variable you defined earlier as 'n'.

n = integer_variable
sum_of_even_numbers = n * (n + 1)

# Print Results:
# Print the results of the previous tasks.

print("Concatenated String:", concatenated_string)
print("Integer Limit:", int_limit)
print("Float Limit:", float_limit)
print("Sum of First n Even Numbers:", sum_of_even_numbers)


# -----------------------------------------------------------

# Notas de clase

# Asignamos valores a las variables y tipos de datos primitivos
num_entero = 10
num_real = 13.1415
tipo_cadena = "Hola mundo"
tipo_booleano = True

# imprimimos los valores de las variables y tipos de datos primitivos
print(num_entero)
print(num_entero)
print(tipo_cadena)
print(tipo_booleano)

# cambiar el tipo de la variable x de entero a string
x = 42
# x es un entero
x = str(x)
# Ahora x es una cadena que representa el número 42
print("El valor de x es: " + x)
# El valor de x es: 42

# // es la división entera / es la división flotante o decimal
print(5//2)
# 2

# -----------------------------------------------------------
