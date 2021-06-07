import numpy
import pyspek
import scipy.fft

'''
def FrequencyPowerArray(sample_buffer: numpy.ndarray) -> numpy.ndarray:
    return scipy.fft.rfftfreq(), scipy.fft.rfft()
'''


def dBFS(magnitude: int, bit_depth: int) -> float:
    return 20*numpy.log10(abs(magnitude)/(2**(bit_depth-1)-1))