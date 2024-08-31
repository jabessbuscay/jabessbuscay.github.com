#Create a Python program to perform arithmetic Operations  (Addition, Subtraction, Division, Multiplication, Modulus, Exponent) using two variable numbers for int, float and complex

num1 = 19  
num2 = 5

result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2
result_mod = num1 % num2
result_exp = num1 ** num2

print("Addition: ", result_add)
print("Subtraction: ", result_sub)
print("Multiplication: ", result_mul)
print("Division: ", result_div)
print("Modulus: ", result_mod)
print("Exponent: ", result_exp)

num1 = 20.5
num2 = 7.5

result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2
result_mod = num1 % num2
result_exp = num1 ** num2

print("\nAddition (float): ", result_add)
print("Subtraction (float): ", result_sub)
print("Multiplication (float): ", result_mul)
print("Division (float): ", result_div)
print("Modulus (float): ", result_mod)
print("Exponent (float): ", result_exp)

num1 = 3 + 4
num2 = 2 + 5
result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2
result_mod = abs(num1 - num2)  
result_exp = num1 ** 0.5  
print("\nAddition (complex): ", result_add)
print("Subtraction (complex): ", result_sub)
print("Multiplication (complex): ", result_mul)
print("Division (complex): ", result_div)
print("Modulus (complex): ", result_mod)
print("Exponent (complex): ", result_exp)


#Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num1 and num2 on two separate lines.

num1 = 25_000_000 
num2 = 25000000 

print(num1)
print(num2)


#Creating int,float and complex variable then check the type using the Python Code

int_var = 19
float_var = 19.0
complex_var = 19 + 0

print(f"Type of int_var: {type(int_var)}")
print(f"Type of float_var: {type(float_var)}")
print(f"Type of complex_var: {type(complex_var)}")
