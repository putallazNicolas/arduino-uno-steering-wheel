# Arduino Uno Steering Wheel

I started this project because I really like car games, specially F1, but i got tired of playing it with a normal controller, so I decided to make this.

I wanted to buy nothing (except of the 3D print), but Arduino Uno (the one I have) does not support HID, so I had to look for an alternative. 

This project uses vJoy to use this Arduino as a controller, but I needed "bridge" to connect the serial output from the arduino to vjoy. So i made It in Python.

## How to use

First, connect the potentiometer as a voltage divider to one analog pin, I used a 25K pot, but a bit more or less is Ok. 

Then, load the arduino code into your arduino, and close Arduino IDE. (If you don´t close it it won't work).

After that, run *arduino_vjoy.py*, and It should be working now.

You'll probably have to configure the steering wheel in your game, It probably won't get recongnized by anything, In my case F1 detected a controller and made me to put every control, i put some keyboard buttons for accelerator and the brakes, but I'll be adding them later.
