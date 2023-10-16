# PI waether station

This PI is connected with a BME280 chipset to read the temperature, humidity and pressure. 
The PI used for the project is a Raspberry PI 4 4GB model. 

The projet host a webserver and pushes the data to a Postgres database. You can modify the code
if you want to use another database on no database at all. The same for the Webserver.

## Setup
To get this to run on your PI, you need the following libraries:
- SMBus
- BME280
- socket
- psycopg2