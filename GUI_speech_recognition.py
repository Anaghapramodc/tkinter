from tkinter import *
import speech_recognition as sr


def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_output.config(text="You said: " + text)
    except sr.UnknownValueError:
        text_output.config(text="Could not understand audio")
    except sr.RequestError as e:
        text_output.config(text="Error fetching results; {0}".format(e))


# Create the main Tkinter window
root = Tk()
root.title("Speech Recognition")

# Create a button to start speech recognition
button = Button(root, text="Start Speech Recognition", command=recognize_speech)
button.pack()

# Create a label to display recognized text
text_output = Label(root, text="")
text_output.pack()

# Start the Tkinter event loop
root.mainloop()
