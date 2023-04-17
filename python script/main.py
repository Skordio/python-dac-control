import serial
import time
from math import trunc

def main():
    # First value is Arduino's serial port identifier
    # (e.g., 'COM4' on Windows, '/dev/ttyACM0' or '/dev/ttyUSB0' on Linux)
    arduino = serial.Serial('COM4', 9600)
    time.sleep(2)  # Give the connection some time to establish

    while True:
        try:
            user_input = input("Enter the desired voltage (0 to 4.61): ")
            if user_input == "":
                continue
            # get user input between 0 and 5
            voltage = float(user_input)
            voltage = voltage * 1.085
            # divide by three
            # split into number and decimal
            voltage = str(voltage).split(".")
            # format with only up to two decimal places
            voltage = f'{voltage[0]}.{voltage[1][:2]}'
            if 0 <= float(voltage) <= 5:
                arduino.write(voltage.encode())

                # Wait for the validation message from the Arduino
                validation_message = arduino.readline().decode().strip()
                print(validation_message)
            else:
                raise ValueError()
        except ValueError:
            print("Invalid input. Please enter a valid voltage between 0 and 4.61 volts.")
        except KeyboardInterrupt:
            print("\nExitting...")
            break

    arduino.close()

if __name__ == "__main__":
    main()
