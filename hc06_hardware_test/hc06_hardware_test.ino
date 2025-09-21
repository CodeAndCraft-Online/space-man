// HC-06 Hardware Test Sketch
// Tests HC-06 module directly by looping Arduino Softwareserial to pass-through AT commands
// Upload this sketch, then use Arduino Serial Monitor to send AT commands to HC-06

#include <SoftwareSerial.h>

// HC-06 pins (adjust if different module)
#define BT_RX 10  // Arduino RX (connect to HC-06 TX)
#define BT_TX 11  // Arduino TX (connect to HC-06 RX)

SoftwareSerial hc06(BT_RX, BT_TX); // RX, TX for HC-06

void setup() {
    // Hardware Serial for PC communication
    Serial.begin(9600);
    Serial.println("=== HC-06 Hardware Test ===");
    Serial.println("Send AT commands via Serial Monitor (115200 baud, Newline ending)");
    Serial.println();
    Serial.println("HC-06 Wiring Check:");
    Serial.println("Arduino Pin 10 (RX) ← HC-06 TX (blue wire)");
    Serial.println("Arduino Pin 11 (TX) → HC-06 RX (green wire)");
    Serial.println("HC-06 VCC → Arduino 5V (red wire)");
    Serial.println("HC-06 GND → Arduino GND (black wire)");
    Serial.println("HC-06 KEY/EN → Arduino 5V (yellow wire - CRITICAL for AT mode)");
    Serial.println();
    Serial.println("Commands to test:");
    Serial.println("AT - Should respond 'OK'");
    Serial.println("AT+NAME? - Shows current device name");
    Serial.println("AT+VERSION? - Shows firmware version");
    Serial.println("AT+NAMEHC06-Test - Sets device name");
    Serial.println();

    // HC-06 Serial
    hc06.begin(9600);
    Serial.println("HC-06 Serial initialized at 9600 baud");
}

void loop() {
    // Forward commands from Serial Monitor to HC-06
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        Serial.print("→ HC-06: ");
        Serial.println(command);
        hc06.println(command);

        // Brief delay for response
        delay(300);
    }

    // Forward responses from HC-06 to Serial Monitor
    if (hc06.available()) {
        String response = hc06.readStringUntil('\n');
        response.trim();
        if (response.length() > 0) {
            Serial.print("← HC-06: ");
            Serial.println(response);

            // Additional info for common responses
            if (response == "OK") {
                Serial.println("  ✅ HC-06 is responding correctly!");
            } else if (response.startsWith("+VERSION:")) {
                Serial.println("  ✅ HC-06 firmware detected!");
                Serial.println("  📡 Bluetooth should be operational now.");
            } else if (response.startsWith("+NAME:")) {
                Serial.println("  📛 Current device name shown above.");
                Serial.println("  📱 This should appear in Android Bluetooth settings.");
            }
        }
    }

    // Reminder message every 10 seconds
    static unsigned long lastReminder = 0;
    if (millis() - lastReminder > 10000) {
        lastReminder = millis();
        Serial.println();
        Serial.println("📡 If no HC-06 responses:");
        Serial.println("   1. Check KEY/EN pin connected to 5V");
        Serial.println("   2. Verify TX/RX wiring (may be swapped)");
        Serial.println("   3. HC-06 module may be faulty");
        Serial.println("   4. Try HC-05 pin mapping instead");
        Serial.println();
    }
}
