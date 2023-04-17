import serial
import time
import tkinter as tk
from tkinter import messagebox

def set_voltage(event=None):
    try:
        voltage = voltage_entry.get()
        if voltage == "":
            arduino.write("POT".encode())
            messagebox.showinfo("Info", "Potentiometer mode activated. Enter a voltage value to exit this mode.")
        else:
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
        messagebox.showerror("Error", "Invalid input. Please enter a valid voltage between 0 and 4.61 volts or leave the field empty to use the potentiometer.")

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

set_voltage_button = tk.Button(frame, text="Set Voltage", command=set_voltage)
set_voltage_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

exit_button = tk.Button(frame, text="Exit", command=exit_program)
exit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
