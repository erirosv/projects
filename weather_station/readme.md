# PI waether station

This PI is connected with a BME280 chipset to read the temperature, humidity and pressure. 
The PI used for the project is a Raspberry PI 4 4GB model. 

<img src="docs/pi.png" alt="Raspberry Pi 4" width="400" height="400" />


Any rspberry pi or alternative SOC can be used. In this project, this was the SOC available. 

<img src="docs/bme.png" alt="BME280" width="400" height="400" />

The BME280 does com in mayn different flavors, the one used was the cheapest one on amazon. 

The projet host a webserver and pushes the data to a Postgres database. In this project the database is hosted in my home-lab on a NAS. The database is hosten within a docker container. Hence, there is a bit more work to get it working. The database can also be hosten locally on the Pi. However, from my initial testing, the webserver hosted on the Pi did not have the grates response. 

## Setup
To get this to run on your PI, you need the following libraries:
- SMBus
- BME280
- socket
- psycopg2