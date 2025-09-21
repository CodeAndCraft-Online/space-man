// Arduino HC-06 enabled buzzer control with Bluetooth Classic module
// Connect buzzer to pin 9
// Connect HC-06: Arduino pin 10 (RX) <-> HC-06 TX, Arduino pin 11 (TX) <-> HC-06 RX
// Connect HC-06 key/EN pin to Arduino 5V for AT command mode, can be disconnected after setup
// Power: Arduino 5V <-> HC-06 VCC, Arduino GND <-> HC-06 GND

#include <SoftwareSerial.h>

#define BUZZER_PIN 9
#define BT_RX 10  // Arduino RX (connect to HC-06 TX)
#define BT_TX 11  // Arduino TX (connect to HC-06 RX)

SoftwareSerial btSerial(BT_RX, BT_TX); // RX, TX for Bluetooth module

void setup() {
    // Initialize hardware serial for debugging
    Serial.begin(9600);
    Serial.println("Arduino HC-06 buzzer controller starting...");

    // Initialize SoftwareSerial for HC-06 Bluetooth module
    btSerial.begin(9600);

    Serial.println("Configuring HC-06 Bluetooth module...");

    delay(1000); // Wait for module to boot (ensure key/EN pin is connected to 5V)

    // Test AT communication
    btSerial.println("AT");
    delay(200);

    if (btSerial.available()) {
        String response = btSerial.readStringUntil('\n');
        Serial.println("HC-06 AT response: " + response);
    } else {
        Serial.println("No AT response (check HC-06 key/EN pin connection)");
    }

    // Set device name for discovery
    btSerial.println("AT+NAMESpace-Man-Buzzer");
    delay(200);
    if (btSerial.available()) {
        String response = btSerial.readStringUntil('\n');
        Serial.println("HC-06 name set: " + response);
    }

    // Get version info
    btSerial.println("AT+VERSION?");
    delay(200);
    if (btSerial.available()) {
        String response = btSerial.readStringUntil('\n');
        Serial.println("HC-06 version: " + response);
    }

    // Set pin if needed (default usually 0000 or 1234)
    btSerial.println("AT+PIN1234");
    delay(200);

    Serial.println("HC-06 configuration complete");
    Serial.println("BT buzzer controller ready - pair with Android device");
    Serial.println("Use a Bluetooth serial terminal app to send commands: BEEP, HELLO, etc.");
}

void loop() {
    // Check for HC-06 Bluetooth data (commands from Android app)
    if (btSerial.available() > 0) {
        String command = btSerial.readStringUntil('\n');
        command.trim();
        Serial.println("BT command received: " + command);  // Echo to serial for debugging
        processCommand(command, true); // true = from Bluetooth
    }

    // Also check hardware serial for USB debug/control
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        Serial.println("USB command received: " + command);
        processCommand(command, false); // false = from USB
        // Forward non-buzzer commands to Bluetooth module for testing
        if (command.startsWith("AT")) {
            btSerial.println(command);
            Serial.println("Forwarded to HC-06: " + command);
        }
    }
}

void processCommand(String command, bool fromBT) {
    Serial.println("Processing: " + command);  // Debug

    if (command == "BEEP") {
        // Play a nice "ba dum tss" sequence
        tone(BUZZER_PIN, 150, 200);  // 150Hz for 200ms (ba)
        delay(250);
        tone(BUZZER_PIN, 120, 200);  // 120Hz for 200ms (dum)
        delay(150);
        tone(BUZZER_PIN, 200, 300);  // 200Hz for 300ms (tss)

        sendResponse("Tone sequence played", fromBT);
    }
    else if (command == "BEEP_ON") {
        // Continuous tone for compatibility
        tone(BUZZER_PIN, 440, 0);  // 440Hz continuous
        sendResponse("Tone ON (440Hz)", fromBT);
    }
    else if (command == "BEEP_OFF") {
        noTone(BUZZER_PIN);
        sendResponse("Tone OFF", fromBT);
    }
    else if (command == "HELLO") {
        sendResponse("Hello from Arduino HC-06!", fromBT);
    }
    else if (command == "AT" || command == "AT+VERSION?" || command.startsWith("AT+")) {
        // AT commands forwarded or responded
        sendResponse("AT commands handled", fromBT);
    }
    else {
        sendResponse("Unknown command: " + command, fromBT);
    }
}

void sendResponse(String message, bool toBT) {
    if (toBT) {
        btSerial.println(message);
    } else {
        Serial.println(message);
    }
}
