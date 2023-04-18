import serial
import time
import tkinter as tk
from tkinter import messagebox

potentiometer_mode = True
potentiometer_mode_text = ''

def potentiometer_mode_toggle():
    try:
        arduino.write("POT".encode())
        messagebox.showinfo("Info", "Potentiometer mode activated. Set a voltage value to exit this mode.")
    except Exception as e:
        messagebox.showerror("Error", e)
        

def set_voltage(event=None):
    try:
        voltage = voltage_entry.get()
        if voltage == "":
            potentiometer_mode = True
            arduino.write("POT".encode())
            messagebox.showinfo("Info", "Potentiometer mode activated. Enter a voltage value to exit this mode.")
        else:
            potentiometer_mode = False
            voltage = float(voltage)
            if 0 <= voltage <= 4.61:
                voltage *= 1.085
                voltage_str = f'{voltage:.2f}'
                arduino.write(voltage_str.encode())

                validation_message = arduino.readline().decode().strip()
                messagebox.showinfo("Info", validation_message)
            else:
                raise ValueError()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid voltage between 0 and 4.61 volts, or click potentiometer mode to use potentiometer.")

def exit_program():
    arduino.close()
    root.destroy()


# First value is Arduino's serial port identifier
# (e.g., 'COM4' on Windows, '/dev/ttyACM0' or '/dev/ttyUSB0' on Linux)
arduino = serial.Serial('COM4', 9600)
time.sleep(2)

root = tk.Tk()
root.title("MCP4725 Voltage Control")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

voltage_label = tk.Label(frame, text="Enter the desired voltage (0 to 4.61) or leave empty to use the potentiometer:")
voltage_label.grid(row=0, column=0, padx=5, pady=5)

voltage_entry = tk.Entry(frame)
voltage_entry.grid(row=0, column=1, padx=5, pady=5)
voltage_entry.bind('<Return>', set_voltage)

set_potentiometer_mode_button = tk.Button(frame, text=f"Potentiometer Mode", command=potentiometer_mode_toggle)
set_potentiometer_mode_button.grid(row=2, column=0, columnspan=1, padx=5, pady=5)

set_voltage_button = tk.Button(frame, text="Click to set voltage (or press enter)", command=set_voltage)
set_voltage_button.grid(row=1, column=0, columnspan=1, padx=5, pady=5)

exit_button = tk.Button(frame, text="Exit", command=exit_program)
exit_button.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

root.mainloop()
