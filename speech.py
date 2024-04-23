from tkinter import *
import speech_recognition as sr
def recognition_speech():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(audio)
        text_out.config(text="you said:"+text)
    except sr.UnknownValueError:
        text_out.config(text="could not understand audio")
    except sr.RequestError as e:
        text_out.config(text="Error fetching result;{0}".format(e))
root=Tk()
root.title("speechrecognition")
btn=Button(root,text="start speech recognition",command=recognition_speech)
btn.pack()
text_out=Label(root,text="")
text_out.pack()
root.mainloop()
