#include <Wire.h>
#include <Adafruit_MCP4725.h>

// Create an instance of the MCP4725 DAC
Adafruit_MCP4725 dac;

void setup() {
  // Initialize the DAC
  dac.begin(0x60); // The I2C address of the MCP4725 is 0x60 (default)
}

void loop() {
  // Set the DAC voltage to 1 volt
  float voltage1 = 1.0;
  setDACVoltage(voltage1);

  // Wait for 2 seconds
  delay(2000);

  // Set the DAC voltage to full voltage (3.3 volts)
  float voltage2 = 3.3;
  setDACVoltage(voltage2);

  // Wait for 2 seconds
  delay(2000);
}

void setDACVoltage(float voltage) {
  // The MCP4725 is a 12-bit DAC, so the maximum value is 4095
  // The voltage reference is 3.3V for the MCP4725
  uint16_t dacValue = (voltage * 4095.0) / 3.3;

  // Check for valid values
  if (dacValue > 4095) {
    dacValue = 4095;
  }

  // Set the DAC output
  dac.setVoltage(dacValue, false);
}