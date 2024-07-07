# temp_conversion_tool.py

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the conversion formula."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the conversion formula."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
