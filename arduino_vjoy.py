import serial
import pyvjoy

# Conectar con el Arduino (ajusta COM según tu caso)
arduino = serial.Serial('COM3', 9600, timeout=1)

# Inicializar vJoy
joystick = pyvjoy.VJoyDevice(1)  # ID del dispositivo vJoy

def map_range(value, in_min, in_max, out_min, out_max):
    """Mapea un valor de un rango a otro."""
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    try:
        data = arduino.readline().decode().strip()
        if data:
            volante = map_range(int(data), 0, 1023, 1, 32768)  # Eje X

            # Enviar valor al eje X de vJoy
            joystick.set_axis(pyvjoy.HID_USAGE_X, volante)

    except Exception as e:
        print("Error:", e)
        break
