from pyspek.analysis.pcm import *
import numpy as np
import miniaudio as audio

def test_ExtractChannelArrays_1_channel():
    samples = audio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    audio_file = audio.DecodedSoundFile("test", 1, 48000, audio.SampleFormat.SIGNED16, samples)

    channel_1 = np.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    assert np.testing.assert_equal(ExtractChannelArray(1, audio_file).astype(int), channel_1) is None

def test_ExtractChannelArrays_2_channels():
    samples = audio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    audio_file = audio.DecodedSoundFile("test", 2, 48000, audio.SampleFormat.SIGNED16, samples)

    channel_1 = np.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    channel_2 = np.array([-9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11])

    assert np.testing.assert_equal(ExtractChannelArray(1, audio_file).astype(int), channel_1) is None
    assert np.testing.assert_equal(ExtractChannelArray(2, audio_file).astype(int), channel_2) is None