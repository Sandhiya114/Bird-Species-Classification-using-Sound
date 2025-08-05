temp = float(input("Enter the temperature value: "))
print("Choose conversion direction:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
    result = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {result:.2f}°F")
elif choice == '2':
    result = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {result:.2f}°C")
else:
    print(" Invalid choice. Please enter 1 or 2.")
