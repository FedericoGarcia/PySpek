import numpy
import pyspek.dsp.core.audio

def convert_to_mono(audio_data: pyspek.dsp.core.audio.Data) -> numpy.ndarray:
    return int(numpy.sum(audio_data.samples / audio_data.channels_count, axis = 0))