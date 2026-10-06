# section 1

name = "Hubert"
age = 42
height = "6.4"
is_student = True

# section 2

name = input("Please state your name:" )
Year_of_birth = input("Please enter the year that you were born: ")
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hello, {name}! You are approximately {age} years old.")

# section 3

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

product = num1 * num2
print(f"{num1} * {num2} = {product}")

# section 4

item = "Helix CRM Software"
price = 48.99
quantity = 1

total = price * quantity

print("=" * 30)
print ("  RECEIPT")
print("=" * 30)
print(f"Item:    {item}")
print(f"Price:   ${price:.2f}")
print(f"Quantity:   {quantity}")
print("-" * 30)
print(f"Total:    ${total:.2f}")
print("=" * 30)

# section 5

from datetime import date

name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input(" Tell me one fun fact about yourself: ")
birth_year = int(input("What year were you born? "))

age = date.today().year - birth_year

print("+" + "-" * 38 + "+")
print(f"|. PROFILE: {name:<26}|")
print("+" + "-" * 38 + "+")
print(f"{'Hometown:':<12}{hometown}")
print(f"{'Hobby:':<12}{hobby}")
print(f"{'Fun Fact:':<12}{fun_fact}")
print(f"{'Age:':<12}{age}")
