import serial
import time

def main():
    # First value is Arduino's serial port identifier
    # (e.g., 'COM3' on Windows, '/dev/ttyACM0' or '/dev/ttyUSB0' on Linux)
    arduino = serial.Serial('COM4', 9600)
    time.sleep(2)  # Give the connection some time to establish

    while True:
        try:
            voltage = float(input("Enter the desired voltage (0 to 3.3): "))
            if 0 <= voltage <= 3.3:
                arduino.write(str(voltage).encode())
            else:
                print("Please enter a valid voltage between 0 and 3.3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

    arduino.close()

if __name__ == "__main__":
    main()
