# AIO-VCNL4010
Simple Python3 application on a Raspberry Pi which updates Adafruit.io with ambient light measurements from a VCNL4010 sensor.

## Directory, git and file transfers

- Create a working directory that will be referenced by systemctl, a logs directory and a fonts directory
```
mkdir systemd
mkdir logs
mkdir fonts
```
- Clone this repositiory
```
git clone https://github.com/parttimehacker/AIO-VCNL4010.git
```
- Copy **python 3** source to the systemd directory and font file to the fonts directory
```
cp *.py ../systemd
cp Tahoma.ttf ../fonts
```

## Visit Adafruit.io to create an account

- You will need an adafruit.io account to use this application. 
- The Shark Tank application will require a username and the AIO key
- The link to [Adafruit IO](https://io.adafruit.com)

## Configuring the application

- Setup the application in the systemd directory and git the required files from Adafruit
```
cd systemd
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
cd ..
```
```
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python3 setup.py install
cd ..
```
```
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git 
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install
cd ..
```
```
sudo pip3 install adafruit-io
```
- Edit the sharktank.py to enter the AIO key and the AIO username
- Run sharktank.py in python3
```
sudo python3 sharktank.py
```
## Visit Adafruit.io visualize the data

- The last step is to login to your Adafruit.io account and build dashboards, etc.
- Have fun

## Extra - Setting up systemctl service

- It is a good idea to run sharktank.py as a system service at boot time
- Edit the sharktank.service file and enter your user directory 
- Enter the following commands to install the service
```
sudo cp sharktank.service /lib/systemd/system/sharktank.service
sudo chmod 644 /lib/systemd/system/sharktank.service
sudo systemctl daemon-reload
sudo systemctl enable sharktank.service
```
- Reboot is recommended


