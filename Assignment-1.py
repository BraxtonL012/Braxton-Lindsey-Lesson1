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
