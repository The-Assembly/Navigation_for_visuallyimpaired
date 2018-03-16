# Navigation for the visually impaired

## Introduction to Today's Workshop
OBJECTIVE:Since the smartphone, getting around the city is perilous without the use of a navigation app. Even the visually impaired use special smartphones designed for them to use as a tool to improve their live. <br/>

For the circuit diagram, use the image below as a guide.<br/>

![circuit_bb](https://user-images.githubusercontent.com/32713072/37547282-22135dac-298a-11e8-9caa-6f82e9498edf.jpg)

## Installing the Libraries
To enable the functionalities of all the different functions we will be using on python. Certain libraries need to be installed to enable us to use these "functionalities" for the further use.

### Install Python 3 and PIP
Usually Python3 is pre-installed when you install Raspbian on your Raspberry PI. 

But, not all Python packages are available in the Raspbian archives, and those that are can sometimes be out-of-date. If you can't find a suitable version in the Raspbian archives, you can install packages from the Python Package Index (PyPI). To do so, use the pip tool.

**Pip** is installed by default in Raspbian Jessie (but not Raspbian Wheezy or Jessie Lite). You can install it with apt:

-sudo apt-get install python3-pip

### Changing the Audio output
Changing the audio output
There are two ways of setting the audio output.

#### COMMAND LINE
The following command, entered in the command line, will switch the audio output to HDMI:
- amixer cset numid=3 2 

Here the output is being set to 2, which is HDMI. Setting the output to 1 switches to analogue (headphone jack). The default setting is 0 which is automatic. 

#### RASPI-CONFIG
Open up raspi-config by entering the following into the command line:
- sudo raspi-config

This will open the configuration screen:

Select Option 8 Advanced Options and press Enter, then select Option A6:  Audio and press Enter.

Now you are presented with the two modes explained above as an alternative to the default Auto option.<br/>
Select a mode, press Enter and press the right arrow key to exit the options list, then select Finish to exit the configuration tool.


### Google API
In our application we are using a library called - **gTTS (text to speech library)** <br/>
gTTS is a module and command line utility to save spoken text to mp3.
It uses the Google Text to Speech (TTS) API.
This module supports many languages and sounds very natural.

#### Installation
Install with the python package tool (pip):
- sudo pip install gTTS <br/>

#### Example
```python
from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
```
If you want to test it on the command line use:
- gtts-cli.py “Hello” -l ‘en’ -o hello.mp3 <br/>

In addition, we are also using an inbuilt library, that come with speechrecognition library, when you install it. 
**FOR MORE INFO: https://pythonprogramminglanguage.com/text-to-speech/**

### Setting up the GPIO pins on a Raspberry PI
The newest version of Raspbian has the RPi.GPIO library pre-installed. You’ll probably need to update your library, so using the command line, run:
- sudo apt-get install rpi.gpio
If it isn’t already installed it will be installed. If it is already installed it will be upgraded if a newer version is available.

#### Using the RPi.GPIO Library
Now that you’ve got the package installed and updated, let’s take a look at some of the functions that come with it. Open the Leafpad text editor and save your sketch as “myInputSketch.py”. From this point forward, we’ll execute this script using the command line:

- sudo python myInputSketch.py

All of the following code can be added to this same file. Remember to save before you run the above command. To exit the sketch and make changes, press Ctrl+C.

To add the GPIO library to a Python sketch, you must first import it: <br/>
```python
import RPi.GPIO as GPIO
```

Then we need to declare the type of numbering system we’re going to use for our pins: <br/>
```python
#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)
```
#### Examples: 
https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins <br/>
https://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/

### Setting up the program to run on terminal, after boot
A simple way to see how you can setup to run python file on Raspberry Pi startup (using the terminal).

- Save the python file on home/pi
- On the terminal, navigate to  /home/pi
- now open a hidden file  .bashrc  ( type "sudo nano .bashrc" on terminal and press enter)
- At the end of the file type "python" followed by your file name (eg: python3 speechtotext)
- If you want the terminal to revert back to its normal format, either comment out the command on the .bashrc file or remove it (you can access the bash file in /home/pi).
