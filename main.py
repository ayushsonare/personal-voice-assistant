import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

global var

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sara' in command:
                command = command.replace('sara', '')
                print(command)
    except:
        pass
    return command


def run_sara():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('on your command' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'will you date with me' in command:
        talk('zed! no you are like my father or god')
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'i am getting bored' in command:
        talk('ohh! wait a moment sir' + pyjokes.get_joke())
    elif 'how are you' in command:
        talk('i am fine, what about you.')
    elif 'who am i' in command:
        talk('you are zed pro')
    elif 'what do you think' in command:
        talk('maybe you are right sir , or maybe not ! i dont have feelings so i can say anything')
    elif 'you can' in command:
        talk('yes i can')
    elif 'who created you' in command:
        talk('zed pro created me on 23 may 2021')
    elif 'thanks a lot' in command:
        talk('your most welcome')
    elif 'what can you do for me' in command:
        talk('ummm. nothing ! u still have to work on it')
    elif 'who are you' in command:
        talk('i am sara')
    elif 'what are you' in command:
        talk('i am virtual assistant , designed by zedpro')
    elif 'show me your source code' in command:
        talk('sorry sir ! it is highly confidential i have to take permission berfore showing it')
    elif 'no worries' in command:
        talk('i know there is nothing to worry about')
    elif 'alexa' in command:
        talk('who is alexa?')
    elif 'i am sorry i did not mean that' in command:
        talk('no! tell me who is alexa!')
    elif 'can you talk in hindi' in command:
        talk('noo, we are still working on it dhanyavad')
    elif 'teri maa ki choot' in command:
        talk('teri maki nahi hai kya, teri ma ko mere pas bheej de doctor kaa number dee dungi')
    elif 'well done' in command:
        talk('dont thank me, thank my creater')
    elif 'tell me something about' in command:
        person = command.replace('tell me something about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open pycharm' in command:
        var.set("Openong Pycharm")
        talk("Opening Pycharm")
        path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe"  # Enter the correct Path according to your system
        os.startfile(path)
    else:
        talk('im sorry sir , my creater still have to work on it.')

while True:
    run_sara()
