'''
Setear todo
Leer el canal de el fotodetector
calcular la correccion
Enviar a el generador

checkeos:
Enviar algo y leerlo con el daq
enviar algo y leerlo con el osci
'''
import time
from simple_PID import PID
import matplotlib.pyplot as plt
import numpy as np

## Settings
P = 1
I = 1
D = 1
setpoint = 1

class laser():
    def __init__(self):
        pass
    def write(self,value):
        pass
    def read(self):
        pass

pid = PID(P,I,D,setpoint = setpoint)
pid.proportional_on_measurement = True

while True:
    v = laser.read()
    change = pid(v)
    v = laser.write(change)




