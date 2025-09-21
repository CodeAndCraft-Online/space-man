// Arduino code for buzzer control with musical tones
// Connect buzzer to pin 9

#define BUZZER_PIN 9

void setup() {
    // Initialize serial communication at 9600 baud
    Serial.begin(9600);

    Serial.println("Arduino tone buzzer controller ready");
}

void loop() {
    // Check if data is available on serial port
    if (Serial.available() > 0) {
        // Read the incoming string until newline character
        String command = Serial.readStringUntil('\n');

        // Remove any trailing whitespace
        command.trim();

        // Process the command
        if (command == "BEEP") {
            // Play a nice "ba dum tss" sequence
            tone(BUZZER_PIN, 150, 200);  // 150Hz for 200ms (ba)
            delay(250);
            tone(BUZZER_PIN, 120, 200);  // 120Hz for 200ms (dum)
            delay(150);
            tone(BUZZER_PIN, 200, 300);  // 200Hz for 300ms (tss)
            Serial.println("Tone sequence played");
        }
        else if (command == "BEEP_ON") {
            // Continuous tone for compatibility
            tone(BUZZER_PIN, 440, 0);  // 440Hz continuous
            Serial.println("Tone ON (440Hz)");
        }
        else if (command == "BEEP_OFF") {
            noTone(BUZZER_PIN);
            Serial.println("Tone OFF");
        }
        else if (command == "HELLO") {
            Serial.println("Hello from Arduino!");
        }
    }
}
