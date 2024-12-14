temp = int(input("Temperature: "))
response = input("(F)arenheit or (C)elsius: ")

if response.upper() == "F":
    conversion = (temp - 32) * (5/9)
    print("Celsius: " + str(conversion))
elif response.upper() == "C":
    conversion = temp * (9/5) + 32
    print("Farenheit: " + str(conversion))