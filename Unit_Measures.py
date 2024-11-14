import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage


def convert_length(value, from_unit, to_unit):
    length_units = {
        'meter': 1,
        'kilometer': 1000,
        'mile': 1609.344,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'centimeter': 0.01,
        'millimeter': 0.001
    }
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in length_units or to_unit not in length_units:
        print(f"Invalid length units: {from_unit}, {to_unit}")
        return None


    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]



def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'gram': 0.001,
        'kilogram': 1,
        'milligram': 1e-6,
        'ton': 1000,  # Metric Ton (Tonne)
        'us ton': 907.18474,  # US Ton = 2000 lbs
        'ounce': 0.0283495,
        'pound': 0.453592
    }
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in weight_units or to_unit not in weight_units:
        print(f"Invalid weight units: {from_unit}, {to_unit}")
        return None


    value_in_kg = value * weight_units[from_unit]
    return value_in_kg / weight_units[to_unit]



def convert_speed(value, from_unit, to_unit):
    speed_units = {
        'm/s': 1,
        'km/h': 3.6,
        'mile/h': 2.23694
    }
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in speed_units or to_unit not in speed_units:
        print(f"Invalid speed units: {from_unit}, {to_unit}")
        return None

    value_in_mps = value * speed_units[from_unit]
    return value_in_mps / speed_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9 / 5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5 / 9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9 / 5 + 32
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5 / 9 + 273.15
    return value


def convert_time(value, from_unit, to_unit):
    time_units = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'year': 31557600
    }
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in time_units or to_unit not in time_units:
        print(f"Invalid time units: {from_unit}, {to_unit}")
        return None

    value_in_seconds = value * time_units[from_unit]
    return value_in_seconds / time_units[to_unit]


def convert_area(value, from_unit, to_unit):
    area_units = {
        'square meter': 1,
        'square kilometer': 1e-6,
        'square mile': 3.861e-7,
        'acre': 0.000247105,
        'square foot': 10.7639,
        'square yard': 1.19599
    }
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in area_units or to_unit not in area_units:
        print(f"Invalid area units: {from_unit}, {to_unit}")
        return None


    value_in_square_meters = value * area_units[from_unit]
    return value_in_square_meters / area_units[to_unit]



def convert_data_size(value, from_unit, to_unit):
    data_units = {
        'byte': 1,
        'kilobyte': 1024,
        'megabyte': 1024 ** 2,
        'gigabyte': 1024 ** 3,
        'terabyte': 1024 ** 4
    }
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in data_units or to_unit not in data_units:
        print(f"Invalid data size units: {from_unit}, {to_unit}")
        return None


    value_in_bytes = value * data_units[from_unit]
    return value_in_bytes / data_units[to_unit]


def calculate_thunderstorm_distance():
    try:
        time_diff = float(entry_time_diff.get())

        if time_diff < 0:
            messagebox.showerror("Error", "Time difference cannot be negative!")
            return

        speed_of_sound = 343  # in meters per second
        distance = speed_of_sound * time_diff
        label_result_distance.configure(text=f"Distance to Thunderstorm: {distance:.2f} meters")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Calculate Height of Cliff
def calculate_cliff_height():
    try:
        time_fall = float(entry_fall_time.get())
        g = 9.8  # Acceleration due to gravity in m/s^2
        height = 0.5 * g * (time_fall ** 2)
        label_result_height.configure(text=f"Cliff Height: {height:.2f} meters")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

def conversion_frame():
    hide_frame()
    conversion_frame.pack(fill="both", expand=1)

def thunderstorm_frame():
    hide_frame()
    thunderstorm_frame.pack(fill="both",expand=1)

def cliff_frame():
    hide_frame()
    cliff_frame.pack(fill="both",expand=1)

def hide_frame():
    conversion_frame.pack_forget()
    thunderstorm_frame.pack_forget()
    cliff_frame.pack_forget()
#main window
root = ctk.CTk()
root.title("Unit Measures")
root.geometry("300x400")
root.after(201,lambda :root.iconbitmap("C:\\Users\\DELL\\Pictures\\Measurement_Tool_Small_Logo.png"))



menubar = tk.Menu(root)

tools_menu = tk.Menu(menubar,tearoff=0,font=("Arial",10))
tools_menu.add_command(label="Unit Conversion",command=conversion_frame )
tools_menu.add_command(label="Thunderstorm distance",command=thunderstorm_frame)
tools_menu.add_command(label="Height Measurement",command=cliff_frame)
menubar.add_cascade(label="Tools", menu=tools_menu)
root.configure(menu=menubar)


# Conversion
conversion_frame = tk.Frame(root)
conversion_frame.pack(fill="both", expand=True)
conversion_type = tk.StringVar()
conversion_type_combobox = ttk.Combobox(conversion_frame, textvariable=conversion_type,font=("Arial",13))
conversion_type_combobox['values'] = ['Length', 'Weight', 'Speed', 'Temperature', 'Time', 'Area', 'Data Size']
conversion_type_combobox.set('Length')
conversion_type_combobox.grid(row=1, column=0, columnspan=2, pady=5)

# from Unit
from_unit_label = ctk.CTkLabel(conversion_frame ,text="From Unit:")
from_unit_label.grid(row=2, column=0)
from_unit_combobox = ttk.Combobox(conversion_frame,font=("Arial",12))
from_unit_combobox.grid(row=2, column=1)

# to Unit
to_unit_label = ctk.CTkLabel(conversion_frame, text="To Unit:")
to_unit_label.grid(row=3, column=0)
to_unit_combobox = ttk.Combobox(conversion_frame, font=("Arial",12))
to_unit_combobox.grid(row=3, column=1)

# value
value_label = ctk.CTkLabel(conversion_frame, text="Value:")
value_label.grid(row=4, column=0)
value_entry = ctk.CTkEntry(conversion_frame,font=("Arial",11), corner_radius=10)
value_entry.grid(row=4, column=1)

# Result
result_label = ctk.CTkLabel(conversion_frame, text="Result: ", font=("Helvetica", 14))
result_label.grid(row=5, column=0, columnspan=2, pady=10)


# Thunderstorm Distance Frame
thunderstorm_frame = tk.Frame(root)

label_time_diff = ctk.CTkLabel(thunderstorm_frame, text="Time Difference (seconds):")
label_time_diff.pack(pady=5)
entry_time_diff = tk.Entry(thunderstorm_frame,font=("Arial",15))
entry_time_diff.pack(pady=5)

button_calculate_distance = ctk.CTkButton(thunderstorm_frame, text="Calculate Distance", command=calculate_thunderstorm_distance,corner_radius=10)
button_calculate_distance.pack(pady=10)

label_result_distance = ctk.CTkLabel(thunderstorm_frame, text="Distance to Thunderstorm:",)
label_result_distance.pack(pady=5)

# Cliff Height Frame
cliff_frame = tk.Frame(root)

label_fall_time = ctk.CTkLabel(cliff_frame, text="Time for Object to Fall (seconds):")
label_fall_time.pack(pady=5)
entry_fall_time = tk.Entry(cliff_frame,font=("Arial",15))
entry_fall_time.pack(pady=5)

button_calculate_height = ctk.CTkButton(cliff_frame, text="Calculate Height", command=calculate_cliff_height)
button_calculate_height.pack(pady=10)

label_result_height = ctk.CTkLabel(cliff_frame, text="Cliff Height:")
label_result_height.pack(pady=5)

# Function to update units based on conversion type
def update_units(event=None):
    conversion_type_value = conversion_type.get()
    units = []

    if conversion_type_value == "Length":
        units = ['Meter', 'Kilometer', 'Inch', 'Mile', 'Centimeter', 'Millimeter', 'Yard', 'Foot']
    elif conversion_type_value == "Weight":
        units = ['Gram', 'Kilogram', 'Milligram', 'Ton', 'US Ton', 'Ounce', 'Pound']
    elif conversion_type_value == "Speed":
        units = ['Meter per second', 'Kilometer per hour', 'Foot per second', 'Mile per hour', 'Knot']
    elif conversion_type_value == "Temperature":
        units = ['Celsius', 'Fahrenheit', 'Kelvin']
    elif conversion_type_value == "Time":
        units = ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Year']
    elif conversion_type_value == "Area":
        units = ['Square Meter', 'Square Kilometer', 'Square Mile', 'Square Yard', 'Square Foot']
    elif conversion_type_value == "Data Size":
        units = ['Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte']

    from_unit_combobox['values'] = units
    to_unit_combobox['values'] = units

    if units:
        from_unit_combobox.set(units[0])
        to_unit_combobox.set(units[0])


# Calculate button function
def calculate_conversion():
    try:
        value = float(value_entry.get())
    except ValueError:
        result_label.configure(text="Invalid value entered!")
        return

    type_conversion = conversion_type.get()
    from_unit = from_unit_combobox.get()
    to_unit = to_unit_combobox.get()

    if not from_unit or not to_unit:
        result_label.configure(text="Please select both units!")
        return

    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if type_conversion == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif type_conversion == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif type_conversion == "Speed":
        result = convert_speed(value, from_unit, to_unit)
    elif type_conversion == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif type_conversion == "Time":
        result = convert_time(value, from_unit, to_unit)
    elif type_conversion == "Area":
        result = convert_area(value, from_unit, to_unit)
    elif type_conversion == "Data Size":
        result = convert_data_size(value, from_unit, to_unit)

    if result is not None:
        result_label.configure(text=f"Result: {result:.5f}")
    else:
        result_label.configure(text="Conversion failed due to invalid units!")



calculate_button = ctk.CTkButton(conversion_frame, text="Calculate", command=calculate_conversion,corner_radius=20,)
calculate_button.grid(row=8, column=0, columnspan=2, pady=20)


conversion_type_combobox.bind('<<ComboboxSelected>>', update_units)


update_units()
root.mainloop()
