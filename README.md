# Arduino Uno Steering Wheel

I started this project because I really like car games, specially F1, but i got tired of playing it with a normal controller, so I decided to make this.

I wanted to buy nothing (except of the 3D print), but Arduino Uno (the one I have) does not support HID, so I had to look for an alternative. 

This project uses vJoy to use this Arduino as a controller, but I needed "bridge" to connect the serial output from the arduino to vjoy. So i made It in Python.

## How to Use

### 1️⃣ Install and Configure vJoy  
Before running the script, you need to install and set up **vJoy**, a virtual joystick driver.

#### 🔹 Download vJoy  
1. Download vJoy from **[this link](https://sourceforge.net/projects/vjoystick/)**.  
2. Install it and restart your computer if needed.  

#### 🔹 Configure vJoy  
1. Open **vJoy Configurator** (`vJoyConf.exe`).  
2. Make sure **Device 1 is enabled**.  
3. Enable at least the **X-Axis** (and later Y-Axis, if needed).  
4. Click **Apply** to save the settings.  

---

### 2️⃣ Connect the Potentiometer  
- Wire the potentiometer as a **voltage divider**:  
  - **Middle pin** → Connect to an **analog pin** on the Arduino (e.g., `A0`).  
  - **One side** → Connect to **5V**.  
  - **Other side** → Connect to **GND**.  
- I used a **25K potentiometer**, but a similar value (e.g., **10K - 50K**) should work fine.  

---

### 3️⃣ Upload the Code to the Arduino  
1. Open the **Arduino IDE**.  
2. Load the **Arduino code** onto your board.  
3. **Close the Arduino IDE** after uploading the code.  
   - 📌 **Important:** If you leave it open, it might block the serial port.  

---

### 4️⃣ Run the Python Script  
1. Open a **terminal** or **command prompt**.
2. Navigate to the folder where `arduino_vjoy.py` is located.  
3. Install the required libraries
   ```sh
   pip install pyserial pyvjoy
4. Run the script:  
   ```sh
   python arduino_vjoy.py
5. If everything is set up correctly, your steering wheel should now be detected as a virtual joystick.

