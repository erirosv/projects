#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <WiFi.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "your-ssid";
const char* password = "your-password";
const char* serverIP = "192.168.50.12";
const int serverPort = 5050;

Adafruit_BME280 bme;

String sensorId = "default_sensor";
String location = "default_location";

AsyncWebServer server(80);

void handleGetParams(AsyncWebServerRequest *request) {
  String response = "{\"id\":\"" + sensorId + "\",\"location\":\"" + location + "\"}";
  request->send(200, "application/json", response);
}

void handleSetParams(AsyncWebServerRequest *request) {
  if (request->hasParam("id") && request->hasParam("location")) {
    sensorId = request->getParam("id")->value();
    location = request->getParam("location")->value();
    request->send(200, "text/plain", "Parameters updated successfully");
  } else {
    request->send(400, "text/plain", "Bad Request");
  }
}

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

    server.on("/getParams", HTTP_GET, handleGetParams);
    server.on("/setParams", HTTP_POST, handleSetParams);

    server.begin();
}

void loop() {
    // Read sensor data
    float temperature = bme.readTemperature();
    float pressure = bme.readPressure() / 100.0F;
    float humidity = bme.readHumidity();

    WiFiClient client;
    if (client.connect(serverIP, serverPort)) {
        String message = String(sensorId) + ":" + String(location) + ":" + String(temperature) + ":" + String(pressure) + ":" + String(humidity);
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
    //delay(600000); // Delay 10 min
}
