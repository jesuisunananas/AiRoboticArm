import speech_recognition as sr

def speech_recog():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        #print(type(r.recognize_google(audio)))
        print("Google thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)
)

def main():
	end_condition = input("Would you like to speak?")
	if end_condition != "no":
		speech_recog()

if __name__ == "__main__":
	main()

"""
try:
    print("Whisper thinks you said " + r.recognize_whisper(audio, language="english"))
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Whisper")
"""
