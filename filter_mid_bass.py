#Bibliotecas
import numpy
import wave
import struct
from scipy import signal

#Parámetros del filtro medios-graves.
fl=200.0
fu=1000.0
fs=44100.0
fnyq=fs/2
finf=fl/fnyq
fsup=fu/fnyq
#Declarando el filtro de medios-graves[200-1000].
b2,a2=signal.butter(3,[finf,fsup],btype='band',analog=False)
edo = numpy.zeros(6)
G2=0.8