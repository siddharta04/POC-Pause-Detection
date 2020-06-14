from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_wav("file5.wav")

chunks = split_on_silence(sound,min_silence_len=500, silence_thresh=-16) 

for i, chunks in enumerate(chunks):
    chunks.export("D:/internship/LibriSpeech.chyunk{0}.wav".format(i),format="wav")
    print("pause detected")