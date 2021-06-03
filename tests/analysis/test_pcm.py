from pyspek.analysis.pcm import *
import numpy as np
import miniaudio as audio

# pyspek.analysis.pcm.ExtractChannelArrays()

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

def test_ExtractChannelArrays_3_channels():
    samples = audio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    audio_file = audio.DecodedSoundFile("test", 3, 48000, audio.SampleFormat.SIGNED16, samples)

    channel_1 = np.array([-10, -7, -4, -1, 2, 5, 8])
    channel_2 = np.array([-9, -6, -3, 0, 3, 6, 9])
    channel_3 = np.array([-8, -5, -2, 1, 4, 7, 10])

    assert np.testing.assert_equal(ExtractChannelArray(1, audio_file).astype(int), channel_1) is None
    assert np.testing.assert_equal(ExtractChannelArray(2, audio_file).astype(int), channel_2) is None
    assert np.testing.assert_equal(ExtractChannelArray(3, audio_file).astype(int), channel_3) is None

def test_ExtractChannelArrays_4_channels():
    samples = audio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    audio_file = audio.DecodedSoundFile("test", 4, 48000, audio.SampleFormat.SIGNED16, samples)

    channel_1 = np.array([-10, -6, -2, 2, 6, 10])
    channel_2 = np.array([-9, -5, -1, 3, 7, 11])
    channel_3 = np.array([-8, -4, 0, 4, 8, 12])
    channel_4 = np.array([-7, -3, 1, 5, 9, 13])

    assert np.testing.assert_equal(ExtractChannelArray(1, audio_file).astype(int), channel_1) is None
    assert np.testing.assert_equal(ExtractChannelArray(2, audio_file).astype(int), channel_2) is None
    assert np.testing.assert_equal(ExtractChannelArray(3, audio_file).astype(int), channel_3) is None
    assert np.testing.assert_equal(ExtractChannelArray(4, audio_file).astype(int), channel_4) is None

# pyspek.analysis.pcm.GenerateTimeArray()

def test_GenerateTimeArray_1_channel():
    samples = audio.array.array("b", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    audio_file = audio.DecodedSoundFile("test", 1, 1000, audio.SampleFormat.SIGNED16, samples)

    time = np.array([0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017, 0.018, 0.019])

    assert np.testing.assert_equal(GenerateTimeArray(audio_file), time) is None