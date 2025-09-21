#!/usr/bin/env python3
"""
HC-06 Bluetooth Diagnostic Script
Step-by-step testing of HC-06 module connections and functionality
"""

import serial
import time
import sys

def wait_for_response(ser, timeout=2):
    """Wait for response from HC-06 module"""
    response = ""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
            response += data
            time.sleep(0.1)  # Allow more data to arrive
            if '\n' in response or 'OK' in response:
                break
        time.sleep(0.05)
    return response.strip()

def test_basic_connection():
    """Test if Arduino is connected and HC-06 sketch is running"""
    try:
        ser = serial.Serial('COM6', 9600, timeout=1)
        print("✅ Arduino connected on COM6")

        # Give Arduino time to boot and show startup messages
        time.sleep(2)

        # Read startup output
        startup_output = wait_for_response(ser, timeout=3)
        print("Arduino startup output:")
        for line in startup_output.split('\n'):
            if line.strip():
                print(f"  {line}")

        # Send HELLO to test USB connection
        print("\n📤 Testing USB serial connection...")
        ser.write(b"HELLO\n")
        time.sleep(0.5)
        response = wait_for_response(ser)
        if response:
            print(f"✅ USB response: {response}")
        else:
            print("❌ No USB response - buzzer commands may not work")

        ser.close()
        return True

    except serial.SerialException as e:
        print(f"❌ Serial connection failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("  - Check if Arduino is connected to computer")
        print(f"  - Verify Arduino IDE shows board on COM6: arduino-cli board list")
        print("  - Try a different USB cable")
        return False

def test_at_commands():
    """Test HC-06 AT command communication"""
    try:
        ser = serial.Serial('COM6', 9600, timeout=1)
        time.sleep(1)  # Wait for stable connection

        print("\n📡 Testing HC-06 AT commands...")

        # Test if AT commands work by sending directly to HC-06 pins
        # (This tests the hardware connection to HC-06)
        test_command = "AT+NAME?\n"  # Query current name without changing it
        print(f"📤 Sending: {test_command.strip()}")
        ser.write(test_command.encode())

        time.sleep(0.5)
        response = wait_for_response(ser)
        if response:
            print(f"✅ HC-06 responded: {response}")
            if 'HC-06' in response or 'Space-Man' in response:
                print("✅ HC-06 module is responding correctly")
                return True
            else:
                print("⚠️  HC-06 responded but with unexpected output")
                return True
        else:
            print("❌ No response from HC-06")
            print("\n🔧 Possible issues:")
            print("  - HC-06 KEY/EN pin not connected to 5V (yellow wire)")
            print("  - HC-06 TX/RX wires swapped")
            print("  - HC-06 module not powered (check red and black wires)")
            print("  - HC-06 module faulty")
            return False

    except Exception as e:
        print(f"❌ AT command test failed: {e}")
        return False
    finally:
        ser.close()

def main():
    print("🔍 HC-06 Bluetooth Module Diagnostic")
    print("=" * 40)

    # Test 1: Basic Arduino connection
    if not test_basic_connection():
        print("\n❌ Cannot proceed - Arduino not connected")
        sys.exit(1)

    # Test 2: HC-06 AT communication
    if test_at_commands():
        print("\n✅ HC-06 hardware connection appears working")
        print("\n📱 Bluetooth Discovery Test:")
        print("  1. Check Android Bluetooth settings")
        print("  2. Look for devices (may show as 'HC-06', 'Space-Man-Buzzer', etc.)")
        print("  3. Pair with PIN: 1234")
        print("  4. Use Bluetooth Serial Terminal app to send 'HELLO'")
    else:
        print("\n❌ HC-06 module not responding to AT commands")
        print("\n📋 Wiring Checklist:")
        print("  □ HC-06 VCC (pin) → Arduino 5V (red wire)")
        print("  □ HC-06 GND (pin) → Arduino GND (black wire)")
        print("  □ HC-06 TX (pin) → Arduino Pin 10 (blue wire)")
        print("  □ HC-06 RX (pin) → Arduino Pin 11 (green wire)")
        print("  □ HC-06 KEY/EN (pin) → Arduino 5V (yellow wire) - CRITICAL")
        print("\n  Double-check all connections against HC-06 module labels")

if __name__ == "__main__":
    main()
