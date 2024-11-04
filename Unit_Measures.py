from datetime import datetime

units = {
    'DataSize': {
        'Byte': 1,
        'Kilobyte': 1024,
        'Megabyte': 1024 ** 2,
        'Gigabyte': 1024 ** 3,
        'Terabyte': 1024 ** 4
    },
    'Length': {
        'Meter': 1,
        'Kilometer': 1000,
        'Inch': 0.0254,
        'Mile': 1609.34,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Yard': 0.9144,
        'Foot': 0.3048
    },
    'Mass': {
        'Gram': 0.001,
        'Kilogram': 1,
        'Milligram': 1e-6,
        'Microgram': 1e-9,
        'Tonne': 1000,
        'Ounce': 0.0283495,
        'Pound': 0.453592,
        'Stone': 6.35029,
    },
    'Time': {
        'Second': 1,
        'Millisecond': 1e-3,
        'Microsecond': 1e-6,
        'Nanosecond': 1e-9,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Year': 31557600
    }
}

# Initialize history list
conversion_history = []

# Conversion function
def convert(unit_type, from_unit, to_unit, value):
    # Check if units exist in the specified unit type
    if from_unit in units[unit_type] and to_unit in units[unit_type]:
        # Calculate conversion
        result = (value * units[unit_type][from_unit]) / units[unit_type][to_unit]
        
        # Save to history
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversion_record = {
            "timestamp": timestamp,
            "unit_type": unit_type,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "value": value,
            "result": result
        }
        conversion_history.append(conversion_record)
        
        return f"{value} {from_unit} = {result} {to_unit}"
    else:
        return "Conversion not possible with given units."

# Function to display conversion history
def display_history():
    if not conversion_history:
        print("No conversion history available.")
    else:
        for entry in conversion_history:
            print(f"{entry['timestamp']} - {entry['unit_type']}: {entry['value']} {entry['from_unit']} = {entry['result']} {entry['to_unit']}")
