import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🌡️ CLI Temperature Converter")
    
    parser.add_argument("temperature", type=float, help="Temperature value to convert")
    parser.add_argument("unit", type=str, choices=["celsius", "fahrenheit", "kelvin"],
                        help="Unit of the input temperature")

    args = parser.parse_args()

    temp = args.temperature
    unit = args.unit.lower()

    print(f"\n🔹 Input: {temp}° {unit.capitalize()}")

    if unit == "celsius":
        print(f"Fahrenheit: {celsius_to_fahrenheit(temp):.2f} °F")
        print(f"Kelvin: {celsius_to_kelvin(temp):.2f} K")
    elif unit == "fahrenheit":
        print(f"Celsius: {fahrenheit_to_celsius(temp):.2f} °C")
        print(f"Kelvin: {fahrenheit_to_kelvin(temp):.2f} K")
    elif unit == "kelvin":
        print(f"Celsius: {kelvin_to_celsius(temp):.2f} °C")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.2f} °F")
