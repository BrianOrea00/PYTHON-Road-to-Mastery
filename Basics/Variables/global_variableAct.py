# AI generated problem
# 1. Create a variable outside the function then create a function that will use the variable outside it.
# 2. Create a new function that will overwrite the value of the outside variable make sure it has same name as the outside variable.
# 3. Create a function that uses the global then change the value use the keyword "global".
# 4. print all
message = "Hello CMI!"

def FirstFunc():
    print("Good Day and "+ message)
FirstFunc()

def SecondFunc():
    message = "Lezgoo"
    print("Local: "+ message)
SecondFunc()
print("Global: "+ message)

def ThirdFunc():
    global message
    message = "Hello CMI! 2.0"
ThirdFunc()
print("Updated Global: "+ message)
