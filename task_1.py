import tkinter as tk
from tkinter import messagebox


def create_gradient(canvas, width, height, color1, color2):
    steps = height
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    r_ratio = (r2 - r1) / steps
    g_ratio = (g2 - g1) / steps
    b_ratio = (b2 - b1) / steps

    for i in range(steps):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color, width=2)


def convert_temp():
    try:
        z = float(entry_temp.get())
        degree = unit_var.get().lower()

        if degree == 'celsius':
            k = z + 273.15
            f = ((9 / 5) * z) + 32
            result_label.config(text=f"Kelvin: {k:.2f}\nFahrenheit: {f:.2f}")

        elif degree == 'fahrenheit':
            c = (z - 32) * 5 / 9
            k = (z + 459.67) * 5 / 9
            result_label.config(text=f"Celsius: {c:.2f}\nKelvin: {k:.2f}")

        elif degree == 'kelvin':
            c = z - 273.15
            f = (z * 9 / 5) - 459.67
            result_label.config(text=f"Celsius: {c:.2f}\nFahrenheit: {f:.2f}")

        else:
            messagebox.showerror("Error", "Please enter a valid unit of measurement (Celsius, Fahrenheit, Kelvin).")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature value.")


# Creating main window
root = tk.Tk()
root.title("Temperature Conversion")

# Set window size
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=500)
canvas.grid(row=0, column=0, rowspan=5, columnspan=2)

create_gradient(canvas, 500, 500, "light blue", "#D3B3E5")

# Input fields
tk.Label(root, text="Enter the temperature value:", font=("Arial", 13), bg="light blue").grid(row=0, column=0, padx=10,
                                                                                              pady=10, sticky="e")
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=12, pady=12)

tk.Label(root, text="Enter the unit of measurement:  \n(Celsius/Kelvin/Fahrenheit)", font=("Arial", 13),
         bg="light blue").grid(row=1, column=0, padx=10, pady=10, sticky="e")
unit_var = tk.StringVar()
entry_unit = tk.Entry(root, textvariable=unit_var)
entry_unit.grid(row=1, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.grid(row=2, column=0, columnspan=4, pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 15), bg="light blue")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()