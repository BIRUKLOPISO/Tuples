def convert_temperature(temp, from_scale, to_scale):
    """
    Converts a temperature value from one scale to another.

    Parameters:
    temp (float): The temperature value to be converted.
    from_scale (str): The scale of the input temperature ('C', 'F', or 'K').
    to_scale (str): The scale to convert the temperature to ('C', 'F', or 'K').

    Returns:
    float: The converted temperature value.
    """
    # Convert the input temperature to Celsius
    if from_scale == 'C':
        celsius = temp
    elif from_scale == 'F':
        celsius = (temp - 32) * 5 / 9
    elif from_scale == 'K':
        celsius = temp - 273.15
    else:
        raise ValueError("Invalid temperature scale. Use 'C', 'F', or 'K'.")

    # Convert the Celsius temperature to the desired scale
    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return celsius * 9 / 5 + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid temperature scale. Use 'C', 'F', or 'K'.")


# Get user input
temperature = float(input("Enter the temperature value: "))
from_scale = input("Enter the input temperature scale ('C', 'F', or 'K'): ")
to_scale = input("Enter the desired temperature scale ('C', 'F', or 'K'): ")

try:
    converted_temp = convert_temperature(temperature, from_scale, to_scale)
    print(f"{temperature}°{from_scale} is equal to {converted_temp:.2f}°{to_scale}")
except ValueError as e:
    print(e)