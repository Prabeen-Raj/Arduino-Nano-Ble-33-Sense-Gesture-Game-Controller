import serial 
import pyautogui 
import pydirectinput
ser = serial.Serial('Enter Your Arduino Port Number', 9600)
while True:
    data = ser.readline()
    if data.decode().strip() == "d":
       
        pydirectinput.keyDown('d')
        pydirectinput.keyUp('d')

    if data.decode().strip() == "a":
        pydirectinput.keyDown('a')
        pydirectinput.keyUp('a')

