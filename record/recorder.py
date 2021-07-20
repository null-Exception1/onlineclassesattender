
def get_devices():
    import pyaudio
    import wave
    global p
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    devices = []
    for i in range (0,numdevices):
        if p.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
            devices.append([p.get_device_info_by_host_api_device_index(0,i).get('name'),i])
        if p.get_device_info_by_host_api_device_index(0,i).get('maxOutputChannels')>0:
            devices.append([p.get_device_info_by_host_api_device_index(0,i).get('name'),i])
    return devices
def select_device(index):
    import pyaudio
    import wave
    global p
    
    devinfo = p.get_device_info_by_index(index)
    return devinfo.get('name')

def record():
    import pyaudio
    import wave
    import keyboard
    global p
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    as_loopback=True,
                    frames_per_buffer=CHUNK)


    frames = []
    i = 0
    while True:
        i += 1
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('e'):
            break
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
