import pyttsx3
import speech_recognition as sr
import datetime
from time import sleep
import wikipedia
import webbrowser
import os
import requests
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import youtube_dl
from playsound import playsound
from config import CHROME_PROFILE_PATH
from videoTester import call
from chat import chatbot
import keyboard
# from movie_download import download



engine = pyttsx3.init()
voices = engine.getProperty("voices")
# print(voices)
# engine.setProperty("voice",voices[6].id)


def callback(recognizer, audio):
    try:
        global theadcall
        theadcall = (recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    print("I am E.D.I.T.H Sir. Please tell me how may I help you")
    speak("I am Edith  Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        s_musicfile = (
            "/Users/admin/Downloads/E.D.I.T.H(The%20virtual%20assistant)/chime.wav"
        )
        playsound(s_musicfile)
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")

    except:
        print("Say that again please...")
        return "None"
    return query


def takeCommand2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
    except:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    print("initializing Edith")
    speak("initializing Edith ........................facial detection in processing")
    print("facial detection in processing")
    speak("opening cam")
    os.system('python3 facialui.py')
    # value = call()
    # if value != 1:
    #     print("access denied......closing edith")
    #     speak("access denied......closing edith")
    #     exit(0)
    # print("access granted......opening edith")
    # speak("access granted......opening edith")
    wishMe()
    webbrowser = webbrowser.get()
    i = 0
    while True:
        query = takeCommand().lower()
        print(query)
        if "wikipedia" in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("due to some problem i can not preform this action")

        elif "none" in query:
            i = i + 1

        elif "open youtube" in query:

            webbrowser.open("http://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("http://www.google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif "quit" in query or "exit" in query:
            speak("good bye sir")
            break
        elif "facebook" in query:
            file1 = open("ayushemail.txt", "r+")
            file2 = open("ayushpass.txt", "r+")
            usr = file1.readline()
            pwd = file2.readline()
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            driver = webdriver.Chrome(options=options)
            driver.get("https://www.facebook.com/")
            print("Opened facebook")
            speak("opening facebook")
            sleep(1)
            username_box = driver.find_element_by_id("email")
            username_box.send_keys(usr)
            print("Email Id entered")
            speak("Email Id entered")
            sleep(1)

            password_box = driver.find_element_by_xpath('//*[@id="pass"]')
            password_box.send_keys(pwd)
            print("Password entered")
            speak("Password entered")
            sleep(1)

            # login_box = driver.find_element_by_id('loginbutton')
            # login_box.click()

            print("Done")
            speak("login succesfull")

        elif "play" in query:
            query = query.partition(" ")[2]
            for j in search(query, stop=3):
                if "youtube" in j:
                    webbrowser.open(j)
                    speak("got it ... playing" + query + "in youtube")
                    break
        elif "download movie" in query:
            res = query.split(' ', 2)[2]
            download(res)
        elif "download" in query:
            query = query.partition(" ")[2]
            try:
                for j in search(query, stop=3):
                    if "youtube" in j:
                        ydl_opts = {}
                        speak("ok sir download is in progress")
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([j])
                        print("download compleate")
                        speak("download compleate")
                        break
            except:
                print("due to some error i can't download this file")


        elif "screenshot" in query:
            im1 = pyautogui.screenshot()
            im1.save("my_screenshot.png")
            print("Screenshot captured")
            speak("Screenshot captured")

        elif "weather" in query:
            api_address = "http://api.openweathermap.org/data/2.5/weather?appid=465e27551b2b82ddf6728339576cf03c&q="
            print("please enter city name")
            speak("please enter city name")
            city = input("City Name :")
            url = api_address + city
            json_data = requests.get(url).json()
            temp = json_data["main"]["temp"]
            wind_speed = json_data["wind"]["speed"]
            latitude = json_data["coord"]["lat"]
            longitude = json_data["coord"]["lon"]
            description = json_data["weather"][0]["description"]
            print("Temperature : {} degree celcius".format(temp))
            print("Wind Speed : {} m/s".format(wind_speed))
            print("Latitude : {}".format(latitude))
            print("Longitude : {}".format(longitude))
            print("Description : {}".format(description))

        elif "news" in query:

            def NewsFromBBC():
                main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
                open_bbc_page = requests.get(main_url).json()
                article = open_bbc_page["articles"]
                results = []
                for ar in article:
                    results.append(ar["title"])

                for i in range(len(results)):
                    print(i + 1, results[i])
                    speak(results[i])

            NewsFromBBC()

        elif "whatsapp" in query:
            print("whome do you want to send this message")
            speak("whome do you want to send this message")
            contact = input("please enter the name \n")
            print(contact)
            print("what do you want to say")
            speak("what do you want to say")
            text = takeCommand()
            print(text)
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument(CHROME_PROFILE_PATH)
            driver = webdriver.Chrome(options=options)
            driver.get("https://web.whatsapp.com")
            inp_xpath_search = "//*[@id='side']/div[1]/div/label/div/div[2]"
            input_box_search = WebDriverWait(driver, 50).until(
                lambda driver: driver.find_element_by_xpath(inp_xpath_search)
            )
            input_box_search.click()
            time.sleep(2)
            pyperclip.copy(contact)
            input_box_search.send_keys(Keys.SHIFT, Keys.INSERT)
            time.sleep(2)
            selected_contact = driver.find_element_by_xpath(
                "//span[@title='" + contact + "']"
            )
            selected_contact.click()
            inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
            input_box = driver.find_element_by_xpath(inp_xpath)
            time.sleep(2)
            for i in range(1):
                input_box.send_keys(text + Keys.ENTER)
                time.sleep(1)
            print("message successfully sent")
            speak("message successfully sent")
            driver.quit()
        elif "open chrome" in query:
            os.system("open /Applications/Google\ Chrome.app")
            os.system("pkill Chrome")

        else:
            temp1 = chatbot(query)
            print(temp1)
            speak(temp1)
        while True:
            try:
                # text = takeCommand2()
                # if "hello" in text:
                #     query = ''
                #     break
                if keyboard.is_pressed('/'):
                    print('You Pressed A Key!')
                    break
            except:
                break