#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <WiFi.h>

const char* ssid = "SSID";
const char* password = "password";
const char* serverIP = "192.168.50.12"; 
const int serverPort = 5050;
const char* location = "Living Room";  

Adafruit_BME280 bme;

void setup() {
    Serial.begin(115200);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");

    if (!bme.begin()) {
        Serial.println("Could not find a valid BME280 sensor, check wiring!");
        while (1);
    }
}

void loop() {
    // Read sensor data
    float temperature = bme.readTemperature();
    float pressure = bme.readPressure() / 100.0F;
    float humidity = bme.readHumidity();

    WiFiClient client;
    if (client.connect(serverIP, serverPort)) {
        String message = String(location) + ":" + String(temperature) + ":" + String(pressure) + ":" + String(humidity);
        client.print(message.length());
        delay(10);
        client.print(message);
        delay(10);
        client.stop();
        Serial.println("Data sent to server");
    } else {
        Serial.println("Failed to connect to server");
    }

    delay(10000); // delay for testing 10 sec
    //delay(600000); // Dealy 10 min
}
