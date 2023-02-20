import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice rate
engine.setProperty('rate', 150)

# Set voice volume
engine.setProperty('volume', 0.7)

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to process voice input
def process_voice_input():
    # Create a speech recognition object
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't get that. Please say that again.")
        return None
    return query.lower()

# Define a function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")

# Define a function to process user input and generate a response
def generate_response(user_input):
    if 'wikipedia' in user_input:
        speak('Searching Wikipedia...')
        user_input = user_input.replace("wikipedia", "")
        results = wikipedia.summary(user_input, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'time' in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'hello' in user_input:
        speak("Hi there!")
    elif 'bye' in user_input:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand. Please try again.")

# Greet the user
greet()

# Continuously process user input and generate a response
while True:
    user_input = process_voice_input()
    if user_input:
        generate_response(user_input)


# output
# PS E:\Mahak\PVGCOET\internship\codeClause> python ass3.py     
# Listening...
# Recognizing...
# result2:
# {   'alternative': [   {   'confidence': 0.85044426,
#                            'transcript': 'to my name hello open the Wikipedia'},
#                        {'transcript': 'my name hello open the Wikipedia'}],
#     'final': True}
# User said: to my name hello open the Wikipedia

# Listening...
# Recognizing...
# result2:
# {   'alternative': [   {   'confidence': 0.88687533,
#                            'transcript': "timing time what's the time"},
#                        {'transcript': "timing what's the time"}],
#     'final': True}
# User said: timing time what's the time

# Listening...
# Recognizing...
# result2:
# {   'alternative': [   {   'confidence': 0.88687539,
#                            'transcript': 'hello are you there'}],
#     'final': True}
# User said: hello are you there

# Listening...
# Recognizing...
# result2:
# {   'alternative': [   {   'confidence': 0.83843315,
#                            'transcript': 'goodbye bye-bye'},
#                        {'transcript': 'good bye bye-bye'},
#                        {'transcript': 'goodbye bye-bye bye'},
#                        {'transcript': 'goodbye bye'},
#                        {'transcript': 'goodbye bye bye'}],
#     'final': True}
# User said: goodbye bye-bye