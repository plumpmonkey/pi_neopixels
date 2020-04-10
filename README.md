# pi_neopixels
A Raspberry Pi Powered NHS Rainbow using WS2811 a neopixels string.

Inspired by a similar project, I decided to implement my own tribute to the NHS and Keyworkers during the COVID-19 lockdown. A Flask-based web interface gives basic control over the lights. 10 different light patterns have been impletemented and a pattern is randomly selected and played.

The code is setup for a default 50 LED string, but is easily changed by changing the #defines at the top of `rainbow.py`

# Kit

* [Raspberry Pi](https://www.raspberrypi.org/)
* [Power Supply](https://www.amazon.co.uk/gp/product/B07DQKM9P7)
* [WS2811 LED string lights](https://www.amazon.co.uk/gp/product/B01AU6UG70)

# Prerequisites
Download the project code using `git clone`

Install the WS2811 and Flask prerequisites using the following command:
```
    $ sudo pip3 install -r requirements.txt
```

# How to run
Run the program using the following command: (The ws2811 library needs root access so we must use sudo)
```
   $ sudo python3 rainbow.py
```

As this python program needs to be running, I suggest using something like `screen` or `byobu` to have a detachable terminal session so that you can close out out SSH session and leave the program running.

Navigate to the web interface at `<ip address>`. The flask server runs on port 80, so if you have another webserver running on this Pi, you will need to change the Flask config to use a different port.

There are 4 modes 
  * Rainbow - The main keyworker tribute
  * Cycle Lights - A basic colour cycling mode
  * Knight Rider - Well... you just have to, dont you.
  * Lights Off
  
