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
            values = data.split(",")
            if len(values) == 3:
                volante = map_range(int(values[0]), 0, 1023, 1, 32768)  # Eje X
                boton1 = int(values[1]) == 0  # Botón 1 (invertido por PULLUP)
                boton2 = int(values[2]) == 0  # Botón 2 (invertido por PULLUP)

                # Enviar valor del eje X a vJoy
                joystick.set_axis(pyvjoy.HID_USAGE_X, volante)

                # Enviar botones a vJoy
                joystick.set_button(1, boton1)  # Botón 1
                joystick.set_button(2, boton2)  # Botón 2

    except Exception as e:
        print("Error:", e)
        break
