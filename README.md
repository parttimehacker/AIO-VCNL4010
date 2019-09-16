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
git clone 
```
- Copy python source to the systemd directory and font file to the fonts directory
```
cp *.py systemd
cp *.tf fonts
```
## Configuring the application

- Setup the application in the systemd directory and git the required files from Adafruit
```
cd systemd
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python3 setup.py install
cd ..
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python3 setup.py install
cd ..
git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git 
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install
```
- Edit the sharktank.py to enter the AIO key and the AIO username

- Run sharktank.py in python3
```
sudo python3 sharktank.py
```
## Visit Adafruit.io

- The last step is to login to your Adafruit.io account and build dashboards, etc.

- Have fun

