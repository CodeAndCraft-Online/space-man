# Bluetooth 5.3 BLE Module Setup Guide (HM-10 + Arduino)

This guide shows how to connect an HM-10 Bluetooth 5.3 BLE module to Arduino Uno for wireless buzzer control, extending your existing serial-based buzzer system.

## Hardware Requirements

- Arduino Uno R3
- HM-10 Bluetooth 5.3 BLE module
- Piezo buzzer (passive buzzer)
- Breadboard (830 tie-point recommended)
- Jumper wires (male-male, male-female assorted pack)
- Optional: Breadboard power supply module for cleaner power connections

## Hardware Connections

Connect the HM-10 module to Arduino Uno as follows:

```
Arduino Uno          HM-10 Module
-----------          ------------
5V     (red)    -->  VCC
GND    (black)  -->  GND
Pin 10 (blue)   -->  TX
Pin 11 (green)  -->  RX

Buzzer Connections:
Pin 9              -->  Buzzer (+) terminal
GND                -->  Buzzer (-) terminal
```

### Wiring Diagram (ASCII Art)

```
Arduino Uno
+---------------------+
| 5V -------------> HM-10 VCC (red wire)
| GND ------------> HM-10 GND (black wire)
| Pin 10 ---------> HM-10 TX (blue wire)
| Pin 11 ---------> HM-10 RX (green wire)
| Pin 9 ----------> Buzzer + (yellow wire)
| GND -----------> Buzzer - (black wire)
+---------------------+
          |
          v
     HM-10 Module
+---------------------+
| STATE | RX | TX | GND | VCC |
+---------------------+
```

**Important Notes:**
- HM-10 operates at 3.3V-6V, but Arduino 5V is compatible
- Pins 10/11 are used for SoftwareSerial to avoid conflicts with USB serial
- Double-check TX/RX connections (they cross: Arduino TX -> HM-10 RX, Arduino RX -> HM-10 TX)

## Breadboard Assembly Instructions

Using a breadboard makes connections secure and easy to modify. Follow these steps for proper setup:

### Step-by-Step Breadboard Setup

#### Step 1: Place Components on Breadboard
```
Arduino Uno Position: Straddle the center channel of the breadboard
HM-10 Module: Place in the middle section (rows 15-25)
Buzzer: Place near the edge (rows 5-10)
```

#### Step 2: Power Rail Setup
Most breadboards have power rails along the sides. Connect:
- Arduino 5V → Red power rail (+)
- Arduino GND → Blue power rail (-)

```
Breadboard Power Rails:
+------------------+    +------------------+
| ++++++++ | ---- |    | ---- | ++++++++ |
| 5V from  |      |    |      | 5V from  |
| Arduino  |      |    |      | Arduino  |
+------------------+    +------------------+
| -------- | ++++ |    | ++++ | -------- |
| GND from |      |    |      | GND from |
| Arduino  |      |    |      | Arduino  |
+------------------+    +------------------+
```

#### Step 3: HM-10 BLE Module Connections

**First, identify HM-10 pins:** Most HM-10 modules have 6 pins in this order (left to right when antenna faces up):
- STATE (not used in basic setup)
- RX (receives data from Arduino)
- TX (sends data to Arduino)
- GND
- VCC (+3.3V-6V)
- Optionally: BRK/KEY (for entering AT command mode)

**Wiring Connections:**
```
Arduino Pin 11 (TX) → HM-10 RX (male-male jumper, orange wire)
Arduino Pin 10 (RX) → HM-10 TX (male-male jumper, yellow wire)
Arduino 5V → HM-10 VCC (male-male jumper, red wire)
Arduino GND → HM-10 GND (male-male jumper, black wire)
```

**Breadboard Layout:**
```
   Arduino Side               Breadboard                 HM-10 Side
+---------------------+    +------------------------+    +---------------------+
| Pin 11 (TX) ------> | -> | Row 25, Column A (TX) | -> | HM-10 RX (orange)  |
| Pin 10 (RX) ------> | -> | Row 24, Column A (RX) | -> | HM-10 TX (yellow)  |
| 5V ---------------> | -> | Row 26, Column + (red)| -> | HM-10 VCC (red)    |
| GND ---------------> | -> | Row 27, Column - (blk)| -> | HM-10 GND (black)  |
+---------------------+    +------------------------+    +---------------------+
```

#### Step 4: Piezo Buzzer Connections

**Important:** Use a passive piezo buzzer (has a black plastic case with a sound hole). Active buzzers (with integrated oscillator) won't work with tone() function.

```
Arduino Pin 9 → Buzzer (+) terminal (male-male jumper, green wire)
Arduino GND → Buzzer (-) terminal (male-male jumper, black wire)
```

**Buzzer on Breadboard:**
```
   Buzzer Position: Rows 5-10, Columns E-F
+---------------------+
| Buzzer (+) ------> Arduino Pin 9 (green wire)
| Buzzer (-) ------> Arduino GND (black wire)
+---------------------+
```

#### Step 5: Verify All Connections

**Power Connections (from Arduino to breadboard rails):**
- ✅ 5V jumper from Arduino to red (+ rail)
- ✅ GND jumper from Arduino to blue (- rail)

**HM-10 BLE Module:**
- ✅ Arduino Pin 11 to HM-10 RX (TX line, orange)
- ✅ Arduino Pin 10 to HM-10 TX (RX line, yellow)
- ✅ Arduino 5V to HM-10 VCC (red)
- ✅ Arduino GND to HM-10 GND (black)

**Buzzer:**
- ✅ Arduino Pin 9 to buzzer (+) (green)
- ✅ Arduino GND to buzzer (-) (black)

### Breadboard Visual Layout (Top View)

```
Arduino Uno (straddling center)
+---------------------+
|                     |
+---------------------+

Breadboard Layout:
     A    B    C    D    E    F    G    H    I    J
   +----+----+----+----+----+----+----+----+----+----+
20 |    |    |    |    |    |    |    |    |    |    |  Red (+) Rail
   +----+----+----+----+----+----+----+----+----+----+
19 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
18 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
17 |    |    |    |    |    |    |    |    |    |    |  HM-10 Module
   +----+----+----+----+----+----+----+----+----+----+
16 |    |    | HM-10  | TX | RX |GND|VCC|    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
15 |    |    |ANTENNA |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
14 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
13 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
12 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
11 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
10 |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+---1+
9  |    |    |    |    | BUZ| +  |    |    |    |    |   Buzzer
   +----+----+----+----+----+----+----+----+----+----+
8  |    |    |    |    | BUZ| -  |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
7  |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
6  |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
5  |    |    |    |    |    |    |    |    |    |    |
   +----+----+----+----+----+----+----+----+----+----+
4  |    |    |    |    |    |    |    |    |    |    |  Blue (-) Rail
   +----+----+----+----+----+----+----+----+\----+----+

Column Key:
- A-F: Component placement and jumper connections
- Red (+)/Blue (-) Rails: Power distribution

Wire Color Coding:
- Red: 5V power
- Black: Ground
- Orange: Arduino TX to HM-10 RX
- Yellow: Arduino RX to HM-10 TX
- Green: Arduino Pin 9 to buzzer +
```

### Testing Breadboard Setup

1. **Visual Inspection:** Check all jumper wires are securely inserted
2. **Power Check:** Arduino should power the breadboard (check rail connections)
3. **LED Verification:** HM-10 should have a blinking LED when powered
4. **Serial Test:** Upload basic blink sketch first to verify Arduino works
5. **Buzzer Test:** Upload original buzzer sketch to verify buzzer connection

### Common Breadboard Issues

- **Loose Connections:** Push jumpers firmly into breadboard holes
- **Reversed TX/RX:** HM-10 communication won't work (Arduino TX → HM-10 RX)
- **Power Issues:** Ensure Arduino power jumper is connected to breadboard rails
- **Component Placement:** Keep components away from Arduino USB connector
- **Wire Length:** Use appropriate length jumpers to reduce clutter

## Software Setup

### 1. Upload Arduino Code

1. Open `arduino_buzzer_control_ble/arduino_buzzer_control_ble.ino` in Arduino IDE
2. Verify the board is set to "Arduino Uno"
3. Upload the sketch to your Arduino
4. Open Serial Monitor (9600 baud) to see configuration messages

The Arduino will automatically configure the HM-10 module on startup with these settings:
- Device name: "Arduino-Buzzer"
- BLE Service: Custom buzzer control service
- Transmission power: Maximum range
- Role: Peripheral (server)

### 2. Install Python Dependencies

For BLE testing on your computer:

```bash
pip install bleak
```

### 3. Test BLE Communication

#### Option A: Python Script Testing

Run the BLE test script:

```bash
# Interactive mode (recommended first)
python ble_buzzer_test.py

# Or automated quick test
python ble_buzzer_test.py --quick
```

The script will:
1. Scan for BLE devices
2. Find your "Arduino-Buzzer" device
3. Connect and test commands
4. Play buzzer tones wirelessly

#### Option B: Smartphone BLE Apps

Use these apps to test from your phone:

**Android:**
- BLE Scanner
- nRF Connect for Mobile
- LightBlue

**iOS:**
- LightBlue
- BLE Scanner
- nRF Connect

**Steps:**
1. Open the BLE app
2. Scan for devices
3. Connect to "Arduino-Buzzer"
4. Find the Custom Service (UUID: FFE0)
5. Write string values: "BEEP", "HELLO", etc.

## Troubleshooting

### HM-10 Not Responding
- Check TX/RX wiring (they cross!)
- Verify power connections and voltage
- Try resetting Arduino (HM-10 will reconfigure)
- Check Serial Monitor for "HM-10 BLE module configured" message

### Device Not Found During BLE Scan
- Ensure HM-10 is powered (LED should blink)
- Check Bluetooth is enabled on your device
- Try scanning with smartphone first to confirm module is advertising
- Reset Arduino to restart HM-10 configuration

### Buzzer Not Working
- Verify buzzer wiring (pin 9)
- Test with original serial version first
- Check for PWM pin conflicts (pin 9 is correct)

### BLE Connection Unstable
- Increase delays in Arduino sketch
- Check for electrical interference
- Move devices closer together
- Check HM-10 antenna is clear

## Technical Details

### HM-10 Module Specifications
- Bluetooth Version: 5.3 (backward compatible to 4.0)
- Operating Voltage: 3.3V - 6V
- Operating Current: ~20mA during transmission
- Range: 10-20 meters (line of sight)
- Baud Rate: Default 9600 (configurable)

### Arduino Resource Usage
- Memory: ~6000 bytes flash (~18% of Arduino Uno)
- RAM: ~400 bytes (~19% of Arduino Uno)
- Pins Used: 9 (buzzer), 10/11 (BLE), plus power/ground
- Libraries: SoftwareSerial (built-in), tone() (built-in)

### Communication Protocol
- BLE GATT Profile: Custom service for buzzer control
- Service UUID: FFE0 (standard HM-10)
- Characteristic UUID: FFE1 (standard HM-10)
- Commands: Same as serial version ("BEEP", "HELLO", etc.)
- Encoding: UTF-8 strings with newline termination

### Dual Interface Support
The sketch supports both BLE and USB serial simultaneously:
- BLE commands from mobile apps/smartphones
- USB serial for debugging and computer control
- Same command set for both interfaces

## Advanced Configuration

### Custom HM-10 Settings

You can modify the Arduino sketch to change HM-10 configuration:

```arduino
// In setup() section:
bleSerial.println("AT+NAMEYour-Custom-Name");    // Change device name
bleSerial.println("AT+POWE0");                   // Minimum power (short range)
bleSerial.println("AT+POWE3");                   // Maximum power (long range)
bleSerial.println("AT+PASS123456");              // Set pairing password
```

### Adding New Commands

Extend the `processCommand()` function:

```arduino
else if (command == "VOLUME_UP") {
    // Add volume control logic
    sendResponse("Volume increased", fromBLE);
}
```

### Mobile App Development

For custom mobile apps:

**Service UUID:** `0000FFE0-0000-1000-8000-00805F9B34FB`
**Characteristic UUID:** `0000FFE1-0000-1000-8000-00805F9B34FB`
**Write Property:** Enabled (for sending commands)
**Read Property:** Disabled (responses not supported by default HM-10)

## Performance Comparison

| Method | Range | Latency | Power | Complexity |
|--------|-------|---------|-------|------------|
| USB Serial | Wired | <50ms | Low | Low |
| BLE HM-10 | 10-20m | 100-500ms | Medium | Medium |
| WiFi ESP32 | 50m+ | 50-200ms | High | High |

### BLE vs Other Wireless Options

**Why HM-10 BLE instead of WiFi?**
- BLE has lower power consumption (advertising mode uses ~20mA vs WiFi ~100mA)
- Faster connection time (BLE connects in ~100ms vs WiFi ~2-5 seconds)
- Better for short-range mobile control (phones/tablets)
- Simpler protocol - no IP addressing or network setup required

**When to choose WiFi instead:**
- Need longer range (>20 meters)
- Want internet connectivity
- Need higher bandwidth
- Already have WiFi infrastructure

BLE provides good balance of wireless convenience with reasonable performance.
