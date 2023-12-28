#include <WiFi.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

// Load the necessary libraries
#include <FS.h>
#include <ArduinoJson.h>

// Define the path to the configuration file
const char* configFilePath = "/config.json";

// Declare variables to store configuration
char ssid[32];
char password[32];
char serverIP[16];
int serverPort;

// BME280 sensor setup
Adafruit_BME280 bme;

// WiFi client
WiFiClient client;

// Function to load configuration from file
void loadConfig() {
  File configFile = SPIFFS.open(configFilePath, "r");
  if (configFile) {
    size_t size = configFile.size();
    std::unique_ptr<char[]> buf(new char[size]);
    configFile.readBytes(buf.get(), size);
    configFile.close();

    DynamicJsonDocument jsonDoc(1024);
    DeserializationError error = deserializeJson(jsonDoc, buf.get());

    if (!error) {
      strcpy(ssid, jsonDoc["WIFI_SSID"]);
      strcpy(password, jsonDoc["WIFI_PASSWORD"]);
      strcpy(serverIP, jsonDoc["SERVER_IP"]);
      serverPort = jsonDoc["SERVER_PORT"];
    } else {
      Serial.println("Failed to read configuration file, using default values");
    }
  } else {
    Serial.println("Failed to open configuration file, using default values");
  }
}

void setup() {
  Serial.begin(115200);

  // Initialize the file system
  if (!SPIFFS.begin()) {
    Serial.println("Failed to mount file system");
    return;
  }

  // Load configuration from file
  loadConfig();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize BME280 sensor
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  // Your existing setup code goes here...
}

void loop() {
  // Read BME280 sensor data
  float temperature = bme.readTemperature();
  float humidity = bme.readHumidity();
  float pressure = bme.readPressure() / 100.0F;

  if (client.connect(serverIP, serverPort)) {
    Serial.println("Connected to server");

    // Create a JSON payload
    String payload = "{\"temperature\":" + String(temperature) +
                     ",\"humidity\":" + String(humidity) +
                     ",\"pressure\":" + String(pressure) + "}";

    // Send the payload to the server
    client.println("POST /upload HTTP/1.1");
    client.println("Host: " + String(serverIP));
    client.println("Content-Type: application/json");
    client.println("Content-Length: " + String(payload.length()));
    client.println();
    client.println(payload);

    delay(5000); // Adjust the delay as needed
  } else {
    Serial.println("Connection to server failed");
  }

  client.stop();
  delay(5000); // Adjust the delay between readings as needed
}
