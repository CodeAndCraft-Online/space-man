package main

import (
	"fmt"
	"log"
	"time"

	"go.bug.st/serial"
)

func sendBuzzerCommand(port serial.Port, command string) error {
	_, err := port.Write([]byte(command + "\n"))
	if err != nil {
		return err
	}
	fmt.Printf("Sent command: %s\n", command)
	time.Sleep(1 * time.Second) // Small delay after sending command
	return nil
}

func main() {
	mode := &serial.Mode{
		BaudRate: 9600,
		DataBits: 8,
		Parity:   serial.NoParity,
		StopBits: serial.OneStopBit,
	}

	// Open serial connection
	port, err := serial.Open("COM6", mode)
	if err != nil {
		log.Fatalf("Failed to open serial port: %v", err)
	}
	defer port.Close()

	fmt.Println("Connected to Arduino Uno R3 on COM6")

	// Wait a moment for Arduino to be ready
	time.Sleep(2 * time.Second)

	fmt.Println("Playing tone sequence...")

	// Send command to play the "ba dum tss" sequence
	err = sendBuzzerCommand(port, "BEEP")
	if err != nil {
		log.Fatalf("Failed to send command: %v", err)
	}

	fmt.Println("Tone sequence initiated")

	fmt.Println("Serial connection closed")
}
