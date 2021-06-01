import numpy as np
import matplotlib as plt
import miniaudio as audio

samples = audio.decode_file("pyspek/music.wav")
print(samples)