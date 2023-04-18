#include <Wire.h>
#include <Adafruit_MCP4725.h>

Adafruit_MCP4725 dac;
const int potPin = A0;
bool potMode = true;
const int POT_MIN_VALUE = 0;
const int POT_MAX_VALUE = 1500;

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
  int linearPotValue = map(potValue, 0, POT_MAX_VALUE, POT_MIN_VALUE, maxPotValue);
  float voltage = (linearPotValue * 5.0) / 1023.0;
  setDACVoltage(voltage);
}
