import serial
import time

def send_buzzer_command(ser, command):
    """Send a command to the Arduino over serial"""
    ser.write((command + '\n').encode())
    print(f"Sent command: {command}")
    time.sleep(1)  # Small delay after sending command

def main():
    try:
        # Connect to Arduino on COM6
        ser = serial.Serial('COM6', 9600, timeout=1)
        print("Connected to Arduino Uno R3 on COM6")

        # Wait a moment for Arduino to be ready
        time.sleep(2)

        print("Playing tone sequence...")

        # Send command to play the "ba dum tss" sequence
        send_buzzer_command(ser, "BEEP")

        print("Tone sequence initiated")

        ser.close()
        print("Serial connection closed")

    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
