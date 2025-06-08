FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)

CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = input("Enter the temperature to convert:")
convert = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

match convert :
    case "C":
        fahrenheit = convert_to_fahrenheit(float(temperature))
        print(f"{temperature} °F  is {fahrenheit:.2f} °C")
    case "F":
        celsius = convert_to_celsius(float(temperature))
        print(f"{temperature} °C is {celsius:.2f} °F")
    case _:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")





