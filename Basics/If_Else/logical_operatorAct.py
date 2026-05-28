# AI generated problem

age = 20
has_ticket = True
is_admin = False
score = 85

# 1. Use "and"
# to print:
# "Allowed Entry"
# if age >= 18 and has_ticket is True
# 2. Use "or"
# to print:
# "Access Granted"
# if is_admin is True
# or score >= 80
# 3. Create:
# username = "admin"
# password = "1234"
# use "and"
# to check both conditions
# 4. Create:
# weather = "rainy"
# use "or"
# to check:
# rainy or cloudy
# 5. Create:
# is_banned = False
# use "not"
# to print:
# "User Active"
# 6. Explain using comments:
# what "and" does
# 7. Explain using comments:
# what "or" does
# 8. Explain using comments:
# what "not" does
# 9. Predict:
# what will print?
x = 5
if x > 1 and x < 10:
    print("Inside")
# 10. Predict:
# what will print?
logged_in = False
if not logged_in:
    print("Please Login")

if age >= 18 and has_ticket:
    print("Allowed Entry")

if is_admin or score >= 80:
    print("Access Granted")

username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login Successful")

weather = "rainy"
if weather == "rainy" or weather == "cloudy":
    print("Take an umbrella")

is_banned = False
if not is_banned:
    print("User Active")

# "and" checks if both conditions are true

# "or" checks if at least one condition is true

# "not" inverts the condition

# my prediction: "Inside" will print because both conditions are true

# my prediction: "Please Login" will print because logged_in is False