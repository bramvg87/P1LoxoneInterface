# P1LoxoneInterface

## Purpose
Purpose of this code is to read out the P1 port on a smart meter (made for Belgian P1 meters : Sagecom T211-D or Sagecom S211) 
and to expose this data to an external device using a REST API.
This code was written and tested to integrate the P1 meter to Loxone. 

## Start
Connect Raspberry PI to P1 port using a Serial-to-USB cable.
Make sure P1 port is activated (Fluvius portal). 

## Deployment
1) Copy files to RPi 
```git clone https://github.com/bramvg87/P1LoxoneInterface```

2) Install dependencies
```pip install -r requirements.txt```

3) Set up to run as service in background

* Open a new file:
```sudo nano /lib/systemd/system/P1Reader.service```

* Create a .service file for your service as below:
```sudo nano /lib/systemd/system/P1Reader.service
Add the below text:
[Unit]
Description=P1 Reader Service
After=multi-user.target

[Service]
Type=idle 
ExecStart=/usr/bin/python /home/pi/P1meter/P1LoxoneInterface/main.py 
User=pi 

[Install] 
WantedBy=multi-user.target
```
* Save and exit the nano editor (by pressing Ctrl+X).	

* The permission on the unit file needs to be set to 644 :
```sudo chmod 644 /lib/systemd/system/P1Reader.service```

* Next you can start the service using: 
```sudo systemctl start P1Reader.service```

## Using
P1 reading will be published as json using HTTP GET request on ```x.x.x.x:5000/P1``` (x.x.x.x = the IP address of device where code is installed) 

## References
More detailed deployment instructions can be found on [my blog](https://bram.vangenabet.com/home-automation/connecting-p1-port-to-rpi)  

Serial connection to the P1 meter and parsing has been based on a script written by [JensD ](https://github.com/jensdepuydt/belgian_digitalmeter_p1)
