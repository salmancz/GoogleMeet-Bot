## =*=*=* Developed by Salman =*=*=*= ##

# Importing Modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import keyboard
from playsound import playsound
import pyaudio
import wave
import os 
import speech_recognition as sr


# Initializing Bot and Joining Meet
class meet_bot:
	def __init__(self):
		self.bot = webdriver.Chrome("chromedriver.exe") # ChromeDriver PAth

	def login(self,email,pas):
		bot = self.bot
		bot.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
		time.sleep(2)
		email_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
		email_in.send_keys(email)
		next_btn = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
		next_btn.click()
		time.sleep(4)
		pas_in = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
		pas_in.send_keys(pas)
		next1_btn = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
		next1_btn.click()
		time.sleep(1)
  
	# Joining Meet with meet link
	def join(self,meeting_link):
		bot = self.bot
		bot.get(meeting_link)
		bot.get(meeting_link)
		time.sleep(3)
		diss_btn = bot.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
		diss_btn.click()
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)	
		time.sleep(3)
		camera_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
		camera_btn.click()
		time.sleep(1)
		mic_btn =  bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
		mic_btn.click()
		time.sleep(1)
		join_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
		join_btn.click()

# --- Voice Detection and auto attender --
def attendanceBot():
    try:
        j=0
        while True:
            
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = 5


            p = pyaudio.PyAudio()
            WAVE_OUTPUT_FILENAME = str(j)+".wav"
                
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* recording")

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* done recording")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            try:
                filename = WAVE_OUTPUT_FILENAME
                r = sr.Recognizer()
                with sr.AudioFile(filename) as source:
            
                    audio_data = r.record(source)
                    
                    text = r.recognize_google(audio_data)
                    print(text)
                    
                os.remove(WAVE_OUTPUT_FILENAME)
                get_text=text.split()
                target_text=["salman","Salman.","SALMAN.","Salman?","salman.", "Salman", "salma", "SALMA", "Salma", 45, "ROLL NUMBER 45","roll number 45", "44 Present", "44%"]
                print('Taget text achieved')
                for target in get_text:
                    if target in target_text:
                        
                        playsound('C:\\Users\\new\\Desktop\\python-test\\Salman.mp3')# Pre REcorded audio for attendance
                        print('Responding attendance with users audio')
                        continue
            except:
                continue

            j+=1
    except:
        print("Close Everything and run again")


def meetbot():
    obj = meet_bot()
    obj.login("your email","your password")
    link = "https://meet.google.com/frc-jpvg-nac"
    obj.join(link)
    attendanceBot()

# Call the Script
meetbot()