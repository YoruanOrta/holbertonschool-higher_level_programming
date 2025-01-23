def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(roman_string):  # Process from right to left
        current_value = roman_values.get(char, 0)

        if current_value < prev_value:
            total -= current_value  # Subtract in cases like IV (4), IX (9)
        else:
            total += current_value  # Add value normally

        prev_value = current_value

    return total
