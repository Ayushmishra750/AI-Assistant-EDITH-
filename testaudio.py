import time
import speech_recognition as sr
theadcall = "a"
def callback(recognizer, audio):
    try:
        global theadcall
        theadcall = (recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
stop_listening = r.listen_in_background(m, callback)
# do some unrelated computations for 5 seconds
while True:
    if "hello" in theadcall:
        stop_listening(wait_for_stop=False)
        break


