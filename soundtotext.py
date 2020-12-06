import speech_recognition

file = "test.wav" # I believe you're just talking nonsense

# initialize recognizer
r = speech_recognition.Recognizer()

# open file

with speech_recognition.AudioFile(file) as src:
    # listen for data / load audio to memory
    audio_data = r.record(src)
    # convert from speech to text
    txt_version = r.recognize_google(audio_data)
    print(txt_version)

