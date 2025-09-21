import serial
import time

try:
    ser = serial.Serial('COM6', 9600, timeout=1)
    print("Successfully connected to Arduino Uno R3 on COM6 (9600 baud)")
    print("Sending test message...")
    ser.write(b"AT+VERSION\r\n")
    print("Waiting for response...")
    start_time = time.time()
    while time.time() - start_time < 10:  # Wait 10 seconds for response
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore').strip()
            if data:
                print("Received from Arduino:", repr(data))
                break
        time.sleep(0.1)
    else:
        print("No response received within 10 seconds")
    ser.close()
    print("Serial connection closed")
except serial.SerialException as e:
    print("Serial error:", e)
except Exception as e:
    print("Unexpected error:", e)
