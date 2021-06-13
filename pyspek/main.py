import matplotlib.pyplot
import miniaudio
import numpy
import pyspek.dsp.core.audio
import pyspek.dsp.io
import pyspek.analysis.spectrum_analyzer
import scipy.fft

audio_file_path = "resources/music.wav"
#audio_file_path = "resources/sound.wav"
audio_file = miniaudio.decode_file(audio_file_path) # converts to 16 bits signed samples if not specify!! (even using WAVs)

audio_data = pyspek.dsp.core.audio.Data(16, 44100, pyspek.dsp.io.decode_file(audio_file))




'''

def PlotAmplitudeVsTime(DecodedSoundFile: miniaudio.DecodedSoundFile):
    number_of_channels = DecodedSoundFile.nchannels
    multichannel = pyspek.analysis.pcm.MultichannelArray(DecodedSoundFile)
    time = pyspek.analysis.pcm.GenerateTimeArray(DecodedSoundFile)
    matplotlib.pyplot.figure()
    for channel in range(1, number_of_channels + 1):
        matplotlib.pyplot.subplot(number_of_channels, 1, channel)
        matplotlib.pyplot.plot(time, multichannel[channel-1])
    matplotlib.pyplot.show()

def PlotAmplitudeVsFrequency(DecodedSoundFile: miniaudio.DecodedSoundFile):
    y1_axis = pyspek.analysis.pcm.ExtractChannelArray(1, DecodedSoundFile)
    y2_axis = pyspek.analysis.pcm.ExtractChannelArray(2, DecodedSoundFile)

    start_time = 5 # seconds
    sample_rate = DecodedSoundFile.sample_rate
    bit_depth = DecodedSoundFile.sample_width * 8
    start = sample_rate * start_time
    buffer_size = 2**16 # 4096
    end = start + buffer_size

    # select only a portion of samples to buffering
    y1_axis = y1_axis[start:end]
    y2_axis = y2_axis[start:end]
    x_fft = scipy.fft.rfftfreq(buffer_size, 1 / sample_rate)
    y1_fft = scipy.fft.rfft(y1_axis, buffer_size) / buffer_size
    y1_fft = numpy.absolute(y1_fft)
    y2_fft = scipy.fft.rfft(y2_axis, buffer_size) / buffer_size
    y2_fft = numpy.absolute(y2_fft)

    matplotlib.pyplot.figure()

    matplotlib.pyplot.subplot(2, 1, 1*1)
    matplotlib.pyplot.xscale("log")
    matplotlib.pyplot.xlim(20, 20000)
    matplotlib.pyplot.ylim(-96, 0)
    matplotlib.pyplot.plot(x_fft, pyspek.analysis.spectrum_analyzer.dBFS(y1_fft, bit_depth))

    matplotlib.pyplot.subplot(2, 1, 2*1)
    matplotlib.pyplot.xscale("log")
    matplotlib.pyplot.xlim(20, 20000)
    matplotlib.pyplot.ylim(-96, 0)
    matplotlib.pyplot.plot(x_fft, pyspek.analysis.spectrum_analyzer.dBFS(y2_fft, bit_depth))

    #matplotlib.pyplot.subplots()[1].pcolormesh(numpy.array((y1_axis, y2_axis)))
    matplotlib.pyplot.show()

def PlotSpectrogram(DecodedSoundFile: miniaudio.DecodedSoundFile):
    multichannel = pyspek.analysis.pcm.MultichannelArray(DecodedSoundFile)

    matplotlib.pyplot.figure()
    matplotlib.pyplot.subplots()[1].pcolormesh(multichannel)
    matplotlib.pyplot.show()



time = pyspek.analysis.pcm.GenerateTimeArray(audio_file)
mono = pyspek.analysis.pcm.ConvertToMono(audio_file)

sample_rate = audio_file.sample_rate
#half_sample_rate = int(sample_rate/2)
bit_depth = audio_file.sample_width * 8
buffer_size = 1024
number_of_buffer_divisions = int(numpy.ceil(audio_file.num_frames / buffer_size))

frequencies = scipy.fft.rfftfreq(buffer_size, 1/sample_rate)
spectrum = numpy.zeros(shape = (number_of_buffer_divisions, frequencies.size))

for division in range(0, number_of_buffer_divisions):
    spectrum[division] = pyspek.analysis.spectrum_analyzer.dBFS(numpy.absolute(scipy.fft.rfft(mono[buffer_size*division:buffer_size*(division+1)], buffer_size) / buffer_size), bit_depth)

matplotlib.pyplot.figure()
matplotlib.pyplot.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, wspace = 0, hspace = 0)
matplotlib.pyplot.subplot(2, 1, 1)
matplotlib.pyplot.margins(0)
matplotlib.pyplot.plot(time, mono)
matplotlib.pyplot.subplot(2, 1, 2)
matplotlib.pyplot.set_cmap("turbo")
#matplotlib.pyplot.yscale("log")
matplotlib.pyplot.pcolormesh(numpy.transpose(spectrum))
#matplotlib.pyplot.colorbar()
matplotlib.pyplot.show()

'''