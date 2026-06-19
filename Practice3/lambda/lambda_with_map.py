# Convert temperatures from Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(
    map(lambda temp: (temp * 9/5) + 32, celsius)
)

print(fahrenheit)
