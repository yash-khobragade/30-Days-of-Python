import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def celsius_to_kelvin(c): return c + 273.15
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k): return k - 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

# Main conversion logic
def convert_temperature():
    try:
        temp = float(temp_entry.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = celsius_to_fahrenheit(temp)
            k = celsius_to_kelvin(temp)
            result_label.config(text=f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        elif unit == "Fahrenheit":
            c = fahrenheit_to_celsius(temp)
            k = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif unit == "Kelvin":
            c = kelvin_to_celsius(temp)
            f = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        else:
            messagebox.showerror("Error", "Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI setup
window = tk.Tk()
window.title("🌡️ Temperature Converter")
window.geometry("350x250")
window.resizable(False, False)

# Input field
tk.Label(window, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
temp_entry = tk.Entry(window, font=("Arial", 12))
temp_entry.pack()

# Unit dropdown
tk.Label(window, text="Select Unit:", font=("Arial", 12)).pack(pady=5)
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(window, textvariable=unit_var, state="readonly",
                         values=["Celsius", "Fahrenheit", "Kelvin"])
unit_menu.pack()

# Convert button
convert_btn = tk.Button(window, text="Convert", font=("Arial", 12), command=convert_temperature)
convert_btn.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run the app
window.mainloop()
