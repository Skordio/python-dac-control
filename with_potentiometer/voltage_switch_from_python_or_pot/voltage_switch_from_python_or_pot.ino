#include <Wire.h>
#include <Adafruit_MCP4725.h>

Adafruit_MCP4725 dac;
const int potPin = A0;
bool potMode = false;

void setup() {
  Serial.begin(9600);
  dac.begin(0x60);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "POT") {
      potMode = true;
    } else {
      potMode = false;
      float voltage = command.toFloat();
      setDACVoltage(voltage);
      Serial.print("Voltage updated to ");
      Serial.print(voltage / 1.085, 2);
      Serial.println(" V.");
    }
  }

  if (potMode) {
    usePotentiometer();
  }
}

void setDACVoltage(float voltage) {
  uint16_t dacValue = (voltage * 4095.0) / 5.0;

  if (dacValue > 4095) {
    dacValue = 4095;
  }

  dac.setVoltage(dacValue, false);
}

void usePotentiometer() {
  int potValue = analogRead(potPin);
  int linearPotValue = mapPotValue(potValue);
  float voltage = (linearPotValue * 5.0) / 1023.0;
  setDACVoltage(voltage);
}

int mapPotValue(int potValue) {
  // Assuming a logarithmic potentiometer with 10% to 90% mapping
  const int minPotValue = (1023 * 10) / 100;
  const int maxPotValue = (1023 * 90) / 100;

  int mappedValue = map(potValue, 0, 1023, minPotValue, maxPotValue);
  return mappedValue;
}
