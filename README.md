# Arduino Buzzer Control Project

This project implements a serial-controlled buzzer system for Arduino Uno R3, allowing Python and Go scripts to trigger musical tones and sequences. Features both USB serial and Bluetooth Low Energy (BLE) wireless control options.

## 🎵 Core Features

- **Musical Tone Generation**: Uses Arduino's `tone()` function for precise musical frequencies instead of basic buzzing
- **Command System**: Simple text-based commands (BEEP, BEEP_ON, BEEP_OFF, HELLO)
- **Multi-Platform Control**: Python and Go language support with error handling
- **BLE Integration**: Wireless control via HM-10 Bluetooth 5.3 module
- **Backward Compatibility**: Maintains USB serial interface alongside BLE
- **Memory Bank Documentation**: Comprehensive project documentation in memory-bank/ directory

## 🛠️ Hardware Requirements

### Basic Setup (Serial Control)
- Arduino Uno R3 microcontroller
- Piezo buzzer (passive, 3-5V)
- USB cable for serial communication on COM6

### BLE Setup (Wireless Control)
- All basic components plus:
- HM-10 Bluetooth 5.3 BLE module
- Wires for HM-10 to Arduino connection

## 🔌 Hardware Connections

### Buzzer Wiring
```
Buzzer (+) ---- Arduino Pin 9 (PWM)
Buzzer (-) ---- Arduino GND
```

### BLE Module Wiring (Optional)
```
HM-10 VCC ---- Arduino 5V
HM-10 GND ---- Arduino GND
HM-10 TX ---- Arduino Pin 10 (RX)
HM-10 RX ---- Arduino Pin 11 (TX)
```

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CodeAndCraft-Online/space-man.git
   cd space-man
   ```

2. **Upload Arduino Sketch**
   - For USB serial control: Upload `arduino_buzzer_control/arduino_buzzer_control.ino`
   - For BLE control: Upload `arduino_buzzer_control_ble/arduino_buzzer_control_ble.ino`

3. **Install Python Dependencies** (if needed)
   ```bash
   pip install pyserial bleak
   ```

4. **Install Go Dependencies** (for Go version)
   ```bash
   go mod download
   ```

## 🚀 Usage

### USB Serial Control

**Python:**
```bash
python buzzer_beep.py
```

**Go:**
```bash
go run buzzer_beep.go
```

### BLE Wireless Control

**Python:**
```bash
python ble_buzzer_test.py
```

### Arduino Serial Setup
- Port: COM6 (adjust for your system)
- Baud Rate: 9600
- Data Bits: 8, Parity: None, Stop Bits: 1

### Command Reference

| Command | Action | Response |
|---------|---------|----------|
| `BEEP` | Play musical sequence "ba dum tss" | "Tone sequence played\n" |
| `BEEP_ON` | Continuous 440Hz tone | "Tone ON (440Hz)\n" |
| `BEEP_OFF` | Stop all tones | "Tone OFF\n" |
| `HELLO` | Connection test | "Hello from Arduino!\n" |

## 🎼 Technical Details

### Tone Generation
- Uses Arduino `tone(pin, frequency, duration)` function
- PWM output via Timer/Counter for audio generation
- Square wave output (50% duty cycle)
- Frequency range: 31Hz - 65535Hz

### Serial Communication
- UTF-8 text commands terminated with newline
- 9600 baud rate, 8N1 format
- Commands processed in Arduino `loop()`

### BLE Protocol
- HM-10 Bluetooth 5.3 module integration
- SoftwareSerial for communication (pins 10/11)
- Compatible with standard BLE scanner apps
- Maintains same command protocol as serial version

## 📁 Project Structure

```
space-man/
├── arduino_buzzer_control/          # Basic USB serial Arduino sketch
│   └── arduino_buzzer_control.ino
├── arduino_buzzer_control_ble/      # BLE-enabled Arduino sketch
│   └── arduino_buzzer_control_ble.ino
├── arduino_buzzer_control_hc06/     # HC-06 Bluetooth version
│   └── arduino_buzzer_control_hc06.ino
├── hc06_hardware_test/              # HC-06 hardware diagnostics
│   └── hc06_hardware_test.ino
├── buzzer_beep.py                   # Python serial control script
├── buzzer_beep.go                   # Go serial control script
├── arduino_connect.py               # Arduino connection utility
├── ble_buzzer_test.py               # BLE control script
├── hc06_diagnostic.py               # HC-06 diagnostics
├── README_BLE_SETUP.md              # Detailed BLE setup guide
└── memory-bank/                     # Project documentation
    ├── projectbrief.md
    ├── productContext.md
    ├── techContext.md
    ├── systemPatterns.md
    ├── activeContext.md
    └── progress.md
```

## 🧪 Testing

### Hardware Tests
- Buzzer produces clear musical tones
- Serial connection stable (9600 baud)
- BLE module connects and responds to commands
- Arduino IDE upload successful

### Software Tests
- Python scripts handle connection errors gracefully
- Go programs compile and run successfully
- Cross-platform compatibility verified
- Error handling tested with disconnected hardware

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update documentation if needed
5. Test thoroughly
6. Submit a pull request

## 📚 Documentation

- **[setup guide](README_BLE_SETUP.md)**: Detailed BLE setup instructions
- **[memory-bank/](memory-bank/)**: Comprehensive project documentation including requirements, architecture, and development history

## 📄 License

This project is open source. See individual files for license terms.

## 📞 Support

For issues or questions:
- Check the memory-bank documentation
- Review the troubleshooting section in README_BLE_SETUP.md
- Ensure all hardware connections are correct
- Verify Arduino sketch is uploaded successfully

## 🎯 Future Enhancements

- Volume/PWM duty cycle control
- Additional musical sequences
- Multiple buzzer polyphonic support
- Web interface for control
- MIDI input integration
- Mobile app companion
