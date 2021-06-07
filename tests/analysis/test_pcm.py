import miniaudio
import numpy
import pyspek

# pyspek.analysis.pcm.ExtractChannelArrays()

def test_ExtractChannelArrays_1_channel():
    samples = miniaudio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    audio_file = miniaudio.DecodedSoundFile("test", 1, 48000, miniaudio.SampleFormat.SIGNED16, samples)

    channel_1 = numpy.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(1, audio_file).astype(int), channel_1) is None

def test_ExtractChannelArrays_2_channels():
    samples = miniaudio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    audio_file = miniaudio.DecodedSoundFile("test", 2, 48000, miniaudio.SampleFormat.SIGNED16, samples)

    channel_1 = numpy.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    channel_2 = numpy.array([-9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(1, audio_file).astype(int), channel_1) is None
    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(2, audio_file).astype(int), channel_2) is None

def test_ExtractChannelArrays_3_channels():
    samples = miniaudio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    audio_file = miniaudio.DecodedSoundFile("test", 3, 48000, miniaudio.SampleFormat.SIGNED16, samples)

    channel_1 = numpy.array([-10, -7, -4, -1, 2, 5, 8])
    channel_2 = numpy.array([-9, -6, -3, 0, 3, 6, 9])
    channel_3 = numpy.array([-8, -5, -2, 1, 4, 7, 10])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(1, audio_file).astype(int), channel_1) is None
    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(2, audio_file).astype(int), channel_2) is None
    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(3, audio_file).astype(int), channel_3) is None

def test_ExtractChannelArrays_4_channels():
    samples = miniaudio.array.array("b", [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    audio_file = miniaudio.DecodedSoundFile("test", 4, 48000, miniaudio.SampleFormat.SIGNED16, samples)

    channel_1 = numpy.array([-10, -6, -2, 2, 6, 10])
    channel_2 = numpy.array([-9, -5, -1, 3, 7, 11])
    channel_3 = numpy.array([-8, -4, 0, 4, 8, 12])
    channel_4 = numpy.array([-7, -3, 1, 5, 9, 13])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(1, audio_file).astype(int), channel_1) is None
    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(2, audio_file).astype(int), channel_2) is None
    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(3, audio_file).astype(int), channel_3) is None
    assert numpy.testing.assert_equal(pyspek.analysis.pcm.ExtractChannelArray(4, audio_file).astype(int), channel_4) is None

# pyspek.analysis.pcm.GenerateTimeArray()

def test_GenerateTimeArray_1_channel():
    samples = miniaudio.array.array("b", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    audio_file = miniaudio.DecodedSoundFile("test", 1, 1000, miniaudio.SampleFormat.SIGNED16, samples)

    time = numpy.array([0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017, 0.018, 0.019])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.GenerateTimeArray(audio_file), time) is None

def test_GenerateTimeArray_2_channels():
    samples = miniaudio.array.array("b", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    audio_file = miniaudio.DecodedSoundFile("test", 2, 1000, miniaudio.SampleFormat.SIGNED16, samples)

    time = numpy.array([0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.GenerateTimeArray(audio_file), time) is None

def test_GenerateTimeArray_3_channels():
    samples = miniaudio.array.array("b", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    audio_file = miniaudio.DecodedSoundFile("test", 3, 1000, miniaudio.SampleFormat.SIGNED16, samples)

    time = numpy.array([0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.GenerateTimeArray(audio_file), time) is None

def test_GenerateTimeArray_4_channels():
    samples = miniaudio.array.array("b", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    audio_file = miniaudio.DecodedSoundFile("test", 4, 1000, miniaudio.SampleFormat.SIGNED16, samples)

    time = numpy.array([0, 0.001, 0.002, 0.003, 0.004])

    assert numpy.testing.assert_equal(pyspek.analysis.pcm.GenerateTimeArray(audio_file), time) is None
