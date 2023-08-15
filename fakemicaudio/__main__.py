from io import BytesIO
import sounddevice
import soundfile
import pydub
import sys

try:
    path = sys.argv[1]
except IndexError:
    raise Exception("the path is not provided") from None

file: pydub.AudioSegment = pydub.AudioSegment.from_file(path)
wav_file = BytesIO()
file.export(wav_file, format="wav")
wav_file.seek(0)
numpy_file, samplerate = soundfile.read(wav_file)
sounddevice.rec(numpy_file, samplerate=samplerate, channels=2)
sounddevice.wait()
