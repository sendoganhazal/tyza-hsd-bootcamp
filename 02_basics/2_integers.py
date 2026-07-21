#integers (int)
print("*** INTEGERS ***")

age = 34
student_quantity = 55000
degree = -5

print(age)
print(student_quantity)
print(degree)

#calculation

a = 10
b = 5

print("a:",a,", b:",b)

sum = a + b
print("a+b",sum)

multiplication = a * b
print("a*b",multiplication)

subtraction = a - b
print("a-b",subtraction)

division = a / b
print("a/b",division)

# There is a quantity of products and each product has a unit price. 
# I want to know the total cost of the products I bought.

product_quantity = 8
unit_price = 100

cost_of_product = product_quantity * unit_price

print("Quantity of Products:",product_quantity, ", Unit Price:", unit_price)
print("Cost of Product:", cost_of_product)


# Raise calculator app

unit_price = 250
print("unit price:", unit_price)

rate_of_rise = int(input("Write the rate_of_rise:"))
print("Rate of rise", rate_of_rise)

updated_price = unit_price + unit_price * rate_of_rise / 100
print("Updated price", updated_price)