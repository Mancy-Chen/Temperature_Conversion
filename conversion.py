# Functions for converting temperature between celsius, fahrenheit, and kelvin

# Convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

# Convert celsius to kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15
