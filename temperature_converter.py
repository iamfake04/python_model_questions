import tkinter as tk

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius:.2f}")
    except ValueError:
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, "Invalid input")

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = celsius * 9.0 / 5.0 + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the labels
fahrenheit_label = tk.Label(root, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=0, padx=10, pady=5)

celsius_label = tk.Label(root, text="Celsius")
celsius_label.grid(row=0, column=1, padx=10, pady=5)

# Create and place the entry fields
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=5)
fahrenheit_entry.insert(0, "32.0")

celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)
celsius_entry.insert(0, "0.0")

# Create and place the buttons
to_celsius_button = tk.Button(root, text="oo>", command=fahrenheit_to_celsius)
to_celsius_button.grid(row=2, column=0, padx=10, pady=5)

to_fahrenheit_button = tk.Button(root, text="<oo", command=celsius_to_fahrenheit)
to_fahrenheit_button.grid(row=2, column=1, padx=10, pady=5)

# Start the main event loop
root.mainloop()