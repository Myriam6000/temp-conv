
"""
Celsius = 21.5
Farenheit = Celsius * 9/5 + 32
print (Farenheit)

#upgraded with function and parameters and keyword "return"

def converter (celsius):
    result = (celsius*9/5) + 32
    return result

print (converter (21.5))
print (converter (-7))
print (converter (11))
print (converter (0))

#simplified

def converter (celsius):
    return(celsius*9/5) + 32
    
print (converter (21.5))
print (converter (-7))
print (converter (11))
print (converter (0))

"""
"""
#Example input()
x= input("Enter a number: ")
y = input("Enter a second number: ")
result = float(x) + float(y)
message = "The result of " + x + " plus " + y + " is " + str(result)

print(message)
"""
#converter with input
#as done by Nico
def temp_converter (celsius):
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farhenheit."
    result = (celsius *9/5) + 32
    return str(celsius) + msg_1 + str(result) + msg_2

user_input = input("Enter a temperature in degrees Celsius:")
farhenheit_result = temp_converter(float(user_input))

print (farhenheit_result)

"""
#myway 
def converter ():
    celsius = input ("Mimi demands to enter a temperature in degrees Celsius : ")
    result = (float(celsius) *9/5) + 32
    print (celsius + " degrees celsius are " + str(result) +" degrees Farenheit.")

converter()
"""

#myway - another way
def converter (celsius):
    result = (float(celsius) *9/5) + 32
    print (celsius + " degrees celsius are " + str(result) +" degrees Farenheit.")

user_input = input ("Mimi also demands to enter a temperature in degrees Celsius : ")
converter (user_input)
 
 
"""example by another student (doesn't work ?)
def temp_conv(cel):
    return (float(cel)*9/5)+32
    print( cel + " degrees Celsius are "+ str(temp_conv(cel)) + " degrees Farenheit")
 
cel=input("enter Celsius temperature: ")
"""