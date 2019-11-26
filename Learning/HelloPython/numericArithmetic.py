spam_amount = 0
type(spam_amount)
type(19.95)
'''
Operator 	Name 	Description
a + b 	Addition 	Sum of a and b
a - b 	Subtraction 	Difference of a and b
a * b 	Multiplication 	Product of a and b
a / b 	True division 	Quotient of a and b
a // b 	Floor division 	Quotient of a and b, removing fractional parts
a % b 	Modulus 	Integer remainder after division of a by b
a ** b 	Exponentiation 	a raised to the power of b
-a 	Negation 	The negative of a
'''
print(5 / 2)
print(6 / 2)# -*- coding: utf-8 -*-

print(5 // 2)
print(6 // 2)

''' Order of operations'''
''' PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction '''

8 - 3 + 2
-3 + 4 * 2



hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

''' 
Parentheses are your useful here. You can add them to force Python to evaluate sub-expressions in whatever order you want.
'''
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)
