#!/usr/bin/env python3
"""
BLE Buzzer Control Test Script
Tests BLE communication with Arduino HM-10 module for buzzer control

Prerequisites:
- Install bleak: pip install bleak
- Arduino with HM-10 module programmed with BLE sketch
"""

import asyncio
import sys
from bleak import BleakScanner, BleakClient

# HM-10 BLE service/characteristic UUIDs
SERVICE_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

class BLEBuzzerController:
    def __init__(self):
        self.client = None
        self.device = None

    async def scan_for_device(self, device_name="Arduino-Buzzer"):
        """Scan for BLE devices and find our Arduino buzzer controller"""
        print(f"Scanning for BLE device: {device_name}")

        devices = await BleakScanner.discover()
        for device in devices:
            print(f"Found: {device.name} - {device.address}")
        if device.name and ("Space-Man-Buzzer".lower() in device.name.lower() or device_name.lower() in device.name.lower()):
                self.device = device
                print(f"Found target device: {device.name}")
                return True

        print(f"Device '{device_name}' not found")
        return False

    async def connect(self):
        """Connect to the BLE device"""
        if not self.device:
            print("No device selected. Run scan_for_device() first.")
            return False

        try:
            self.client = BleakClient(self.device)
            await self.client.connect()
            print(f"Connected to {self.device.name}")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    async def send_command(self, command):
        """Send a command to the Arduino via BLE"""
        if not self.client or not self.client.is_connected:
            print("Not connected to device")
            return None

        try:
            # Send command with newline
            data = (command + "\n").encode('utf-8')

            # Write to the characteristic
            await self.client.write_gatt_char(CHARACTERISTIC_UUID, data)
            print(f"Sent: {command}")

            # Wait a bit for Arduino to process and respond
            await asyncio.sleep(0.5)

            # Try to read response (HM-10 might not support responses well)
            # This depends on your HM-10 configuration
            return "Command sent successfully"

        except Exception as e:
            print(f"Send command failed: {e}")
            return None

    async def disconnect(self):
        """Disconnect from BLE device"""
        if self.client:
            await self.client.disconnect()
            print("Disconnected from device")

async def interactive_mode():
    """Interactive testing mode"""
    controller = BLEBuzzerController()

    # Scan for device
    found = await controller.scan_for_device()
    if not found:
        print("Available devices:")
        devices = await BleakScanner.discover()
        for device in devices:
            print(f"  {device.name} - {device.address}")
        return

    # Connect
    connected = await controller.connect()
    if not connected:
        return

    try:
        print("\nBLE Buzzer Control Commands:")
        print("BEEP - Play musical sequence")
        print("BEEP_ON - Continuous tone")
        print("BEEP_OFF - Stop tone")
        print("HELLO - Test connection")
        print("QUIT - Exit")
        print()

        while True:
            cmd = input("Enter command: ").strip().upper()
            if cmd == "QUIT":
                break

            if cmd in ["BEEP", "BEEP_ON", "BEEP_OFF", "HELLO"]:
                await controller.send_command(cmd)
            else:
                print("Unknown command. Try: BEEP, BEEP_ON, BEEP_OFF, HELLO, QUIT")

    finally:
        await controller.disconnect()

async def quick_test():
    """Quick automated test"""
    controller = BLEBuzzerController()

    print("BLE Buzzer Quick Test")
    print("=" * 30)

    # Scan and connect
    found = await controller.scan_for_device()
    if not found:
        return

    connected = await controller.connect()
    if not connected:
        return

    try:
        # Test sequence
        commands = ["HELLO", "BEEP", "BEEP_ON"]
        await asyncio.sleep(1)  # Wait for connection to stabilize

        for cmd in commands:
            print(f"\nTesting: {cmd}")
            result = await controller.send_command(cmd)
            await asyncio.sleep(2)  # Wait between commands

        print("\nStopping continuous tone...")
        await controller.send_command("BEEP_OFF")

    finally:
        await controller.disconnect()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        # Quick automated test
        asyncio.run(quick_test())
    else:
        # Interactive mode
        print("BLE Buzzer Test Script")
        print("Run with --quick for automated test")
        asyncio.run(interactive_mode())

if __name__ == "__main__":
    main()
