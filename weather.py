# Weather Dataset Program

print("Weather Dataset")
print("----------------")

temperature = float(input("Enter temperature in Celsius: "))
humidity = float(input("Enter humidity percentage: "))

print("\nWeather Information")
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")

if temperature > 30:
    print("Weather Condition: Hot")
elif temperature < 15:
    print("Weather Condition: Cold")
else:
    print("Weather Condition: Moderate")