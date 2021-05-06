import subprocess
import wolframalpha
import pyttsx3
#import json
import random
import operator
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import playsound
import os

import mutagen
from mutagen.mp3 import MP3

import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pywhatkit as kit
from twilio.rest import Client
#from client.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

#modules for the mp3 player:
from tkinter import *
import pygame
from tkinter import filedialog
from os import walk
import time
from mutagen.mp3 import MP3




#Modules done except ecapture yay



edge_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge"
webbrowser.register('msedge', None, webbrowser.BackgroundBrowser(edge_path))
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
numpage=1


def speak(audio):

	engine.say(audio)
	engine.runAndWait()

def split(word):
	return[char for char in word]

	

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning Sir!")

	elif hour>=12 and hour<18:
		speak("Good afternoon Sir!")

	else:
		speak("Good evening Sir!")

	assname=("Stella")
	speak("I am Stella. How can I be of assistance?")


def username():
	uname="Madhav Praveen"

	#WIP

	columns =shutil.get_terminal_size().columns

	print('####################'.center(columns))
	print('Welcome, Mr.', uname.center(columns))
	print('####################'.center(columns))

	speak("How can I help you, Sir?")


def takeCommand():
	r=sr.Recognizer()

	with sr.Microphone() as source:

		print("Listening...")
		r.pause_threshold=1
		audio=r.listen(source)

	try:
		print("Recognizing...")
		query=r.recognize_google(audio, language='en-in')
		print(f"User: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		speak("I didn't quite catch that.")
		
		return 'None'

	return query

def sendEmail(to, content):
	server= smtplib.SMTB('smtb.gmail.com', 587)
	server.ehlo()
	server.starttls()

	#low security in gmail
	server.login('martin.tesla1806@gmail.com','a3h7B*2#yy')
	server.sendmail('martin.tesla1806@gmail.com', to, content)
	server.close()



#main starts here

if __name__=='__main__':
	clear=lambda: os.system('cls')

	clear()
	wishMe()
	

	while True:
		query=takeCommand().lower()

		#All commands said by user will be 
		#stored here in 'query' and converted
		#to lowercase for easy recognition.

		if 'wikipedia' in query:
			speak("searching wikipedia...")
			query=query.replace('wikipedia','')
			results=wikipedia.summary(query, sentences=5)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Opening youtube")
			webbrowser.get('msedge').open("youtube.com")

		elif 'hello' in query:
			speak("Hey there!")


		elif 'open google earth' in query:
			speak("Opening google earth")
			webbrowser.get('msedge').open("https://earth.google.com/web/@0,0,0a,22251752.77375655d,35y,0h,0t,0r")

		elif 'open google' in query:
			speak("Opening google")
			webbrowser.get('msedge').open('google.com')

		elif 'youtube search' in query:
			query=query.replace('youtube search', '')
			kit.playonyt(query)

		elif 'open island' in query:
			speak("Opening allen. Have fun learning!")
			webbrowser.get('msedge').open('https://student.allendigital.in/BENGALURU/dashboard/2020-2021/BANFEE983F/Madhav-Praveen?token=HgofJli5cuhgsp1T1pEFVsWFz9Dd26Ps')


		elif 'the time' in query:
			strTime = datetime.datetime.now()
			strTime=strTime.strftime("%H%M%p")
			speak("Sir, the time is " +strTime)


		#apps

		elif 'thanks' in query or 'thank you' in query:
			speak("My pleasure")

		elif 'open ppt' in query or 'open power point' in query:
			speak("Opening Microsoft Power Point")
			power="C:\\Users\\marti\\Desktop\\PowerPoint"
			os.startfile(power)
			exit()

		elif 'open word' in query:
			speak("Opening Microsoft Word")
			word="C:\\Users\\marti\\Desktop\\Word"
			os.startfile(word)
			exit()

		elif 'open ms teams' in query or 'open teams' in query or 'open ms team' in query or 'open team' in query or 'open Microsoft teams' in query:
			speak("Opening Microsoft Teams.")
			team="C:\\Users\\marti\\Desktop\\Microsoft Teams"
			os.startfile(team)
			exit()

		elif 'open pro' in query or 'open premiere pro' in query or 'open adobe premiere pro' in query:
			speak("Opening Adobe Premiere Pro")
			pro="C:\\Users\\marti\\Desktop\\Adobe Premiere Pro 2020"
			os.startfile(pro)
			exit() 




		#music

		elif 'play violin' in query:
			speak("Playing beezart.")
			root=Tk()
			root.title('Stella MP3 Player')
			root.iconbitmap("C:\\Users\\marti\\Desktop\\LogoMakr-00he52.ico")
			root.geometry("530x330")

			pygame.mixer.init()

			def add_song():
				f=[]
				for (dirpath, dirnames, filenames) in walk("C:/Users/marti/Desktop/Martin/mp3/1.Just songs/Beezart"):
					f.extend(filenames)
				for songy in f:
					songbox.insert(END, songy)


			def play():
				song=songbox.get(ACTIVE)
				song=f'C:/Users/marti/Desktop/Martin/mp3/1.Just Songs/Beezart/{song}'
				pygame.mixer.music.load(song)
				pygame.mixer.music.play(loops=0)

				play_time()

				



			def stop():
				pygame.mixer.music.stop()
				songbox.selection_clear(ACTIVE)

				status_bar.config(text='')

			global paused1
			paused1=False

			def pause(is_paused1):
				global paused1
				paused1=is_paused1

				if paused1:
					pygame.mixer.music.unpause()
					paused1=False

				else:
					pygame.mixer.music.pause()
					paused1=True

			def play_time():
				current_time=pygame.mixer.music.get_pos()/1000

				converted_current_time=time.strftime('%H:%M:%S', time.gmtime(current_time))

				


				status_bar.config(text=converted_current_time)

				status_bar.after(1000, play_time)





			songbox=Listbox(root, bg="black", fg="green", width=70, selectbackground="black", selectforeground="white")
			songbox.pack(pady=20)

			stop_btn_img=PhotoImage(file='C:/gui/images/stop.png')
			play_btn_img=PhotoImage(file='C:/gui/images/play.png')
			pause_btn_img=PhotoImage(file='C:/gui/images/pause.png')



			controlsframe=Frame(root)
			controlsframe.pack()

			stop_btn=Button(controlsframe, image=stop_btn_img, borderwidth=0, width=80, height=80, command=stop)
			play_btn=Button(controlsframe, image=play_btn_img, borderwidth=0, width=80, height=80, command=play)
			pause_btn=Button(controlsframe, image=pause_btn_img, borderwidth=0, width=80, height=80, command=lambda: pause(paused1))

			stop_btn.grid(row=1, column=1, padx=10)
			play_btn.grid(row=1, column=2, padx=10)
			pause_btn.grid(row=1, column=3, padx=10)


			mymenu=Menu(root)
			root.config(menu=mymenu)

			add_song()

			status_bar=Label(root, text='', bd=1, relief=GROOVE, anchor=E)
			status_bar.pack(fill=X, side=BOTTOM, ipady=2)


			root.mainloop()

			exit()

		elif 'play instrument' in query:
			speak("Playing beats.")
			root=Tk()
			root.title('Stella MP3 Player')
			root.iconbitmap("C:\\Users\\marti\\Desktop\\LogoMakr-00he52.ico")
			root.geometry("530x330")

			pygame.mixer.init()

			def add_song():
				f=[]
				for (dirpath, dirnames, filenames) in walk("C:/Users/marti/Desktop/Martin/mp3/1.Just songs/Beats"):
					f.extend(filenames)
				for songy in f:
					songbox.insert(END, songy)


			def play():
				song=songbox.get(ACTIVE)
				song=f'C:/Users/marti/Desktop/Martin/mp3/1.Just Songs/Beats/{song}'
				pygame.mixer.music.load(song)
				pygame.mixer.music.play(loops=0)

				play_time()

				



			def stop():
				pygame.mixer.music.stop()
				songbox.selection_clear(ACTIVE)

				status_bar.config(text='')

			global paused2
			paused2=False
			
			

			def pause(is_paused2):
				global paused2
				paused2=is_paused2 

				if paused2:
					pygame.mixer.music.unpause()
					paused2=False

				else:
					pygame.mixer.music.pause()
					paused2=True

			def play_time():
				current_time=pygame.mixer.music.get_pos()/1000

				converted_current_time=time.strftime('%H:%M:%S', time.gmtime(current_time))

				


				status_bar.config(text=converted_current_time)

				status_bar.after(1000, play_time)





			songbox=Listbox(root, bg="black", fg="green", width=70, selectbackground="black", selectforeground="white")
			songbox.pack(pady=20)

			stop_btn_img=PhotoImage(file='C:/gui/images/stop.png')
			play_btn_img=PhotoImage(file='C:/gui/images/play.png')
			pause_btn_img=PhotoImage(file='C:/gui/images/pause.png')



			controlsframe=Frame(root)
			controlsframe.pack()

			stop_btn=Button(controlsframe, image=stop_btn_img, borderwidth=0, width=80, height=80, command=stop)
			play_btn=Button(controlsframe, image=play_btn_img, borderwidth=0, width=80, height=80, command=play)
			pause_btn=Button(controlsframe, image=pause_btn_img, borderwidth=0, width=80, height=80, command=lambda: pause(paused2))

			stop_btn.grid(row=1, column=1, padx=10)
			play_btn.grid(row=1, column=2, padx=10)
			pause_btn.grid(row=1, column=3, padx=10)


			mymenu=Menu(root)
			root.config(menu=mymenu)

			add_song()

			status_bar=Label(root, text='', bd=1, relief=GROOVE, anchor=E)
			status_bar.pack(fill=X, side=BOTTOM, ipady=2)


			root.mainloop()
			exit()

		elif 'play old' in query:
			speak("Playing old songs")
			root=Tk()
			root.title('Stella MP3 Player')
			root.iconbitmap("C:\\Users\\marti\\Desktop\\LogoMakr-00he52.ico")
			root.geometry("530x330")

			pygame.mixer.init()

			def add_song():
				f=[]
				for (dirpath, dirnames, filenames) in walk("C:/Users/marti/Desktop/Martin/mp3/1.Just songs/Nostalgia"):
					f.extend(filenames)
				for songy in f:
					songbox.insert(END, songy)


			def play():
				song=songbox.get(ACTIVE)
				song=f'C:/Users/marti/Desktop/Martin/mp3/1.Just Songs/Nostalgia/{song}'
				pygame.mixer.music.load(song)
				pygame.mixer.music.play(loops=0)

				play_time()

				



			def stop():
				pygame.mixer.music.stop()
				songbox.selection_clear(ACTIVE)

				status_bar.config(text='')

			global paused
			paused=False

			def pause(is_paused):
				global paused
				paused=is_paused 

				if paused:
					pygame.mixer.music.unpause()
					paused=False

				else:
					pygame.mixer.music.pause()
					paused=True

			def play_time():
				current_time=pygame.mixer.music.get_pos()/1000

				converted_current_time=time.strftime('%H:%M:%S', time.gmtime(current_time))

				


				status_bar.config(text=converted_current_time)

				status_bar.after(1000, play_time)





			songbox=Listbox(root, bg="black", fg="green", width=70, selectbackground="black", selectforeground="white")
			songbox.pack(pady=20)

			stop_btn_img=PhotoImage(file='C:/gui/images/stop.png')
			play_btn_img=PhotoImage(file='C:/gui/images/play.png')
			pause_btn_img=PhotoImage(file='C:/gui/images/pause.png')



			controlsframe=Frame(root)
			controlsframe.pack()

			stop_btn=Button(controlsframe, image=stop_btn_img, borderwidth=0, width=80, height=80, command=stop)
			play_btn=Button(controlsframe, image=play_btn_img, borderwidth=0, width=80, height=80, command=play)
			pause_btn=Button(controlsframe, image=pause_btn_img, borderwidth=0, width=80, height=80, command=lambda: pause(paused))

			stop_btn.grid(row=1, column=1, padx=10)
			play_btn.grid(row=1, column=2, padx=10)
			pause_btn.grid(row=1, column=3, padx=10)


			mymenu=Menu(root)
			root.config(menu=mymenu)

			add_song()

			status_bar=Label(root, text='', bd=1, relief=GROOVE, anchor=E)
			status_bar.pack(fill=X, side=BOTTOM, ipady=2)


			root.mainloop()
			exit()


		elif 'play nuts' in query:
			speak("Playing nutshell")
			root=Tk()
			root.title('Stella MP3 Player')
			root.iconbitmap("C:\\Users\\marti\\Desktop\\LogoMakr-00he52.ico")
			root.geometry("530x330")

			pygame.mixer.init()

			def add_song():
				f=[]
				for (dirpath, dirnames, filenames) in walk("C:/Users/marti/Desktop/Martin/mp3/1.Just songs/Kurzgesagt"):
					f.extend(filenames)
				for songy in f:
					songbox.insert(END, songy)


			def play():
				song=songbox.get(ACTIVE)
				song=f'C:/Users/marti/Desktop/Martin/mp3/1.Just Songs/Kurzgesagt/{song}'
				pygame.mixer.music.load(song)
				pygame.mixer.music.play(loops=0)

				play_time()

				



			def stop():
				pygame.mixer.music.stop()
				songbox.selection_clear(ACTIVE)

				status_bar.config(text='')

			global paused3
			paused3=False

			def pause(is_paused3):
				global paused3
				paused3=is_paused3 

				if paused3:
					pygame.mixer.music.unpause()
					paused3=False

				else:
					pygame.mixer.music.pause()
					paused3=True

			def play_time():
				current_time=pygame.mixer.music.get_pos()/1000

				converted_current_time=time.strftime('%H:%M:%S', time.gmtime(current_time))

				


				status_bar.config(text=converted_current_time)

				status_bar.after(1000, play_time)





			songbox=Listbox(root, bg="black", fg="green", width=70, selectbackground="black", selectforeground="white")
			songbox.pack(pady=20)

			stop_btn_img=PhotoImage(file='C:/gui/images/stop.png')
			play_btn_img=PhotoImage(file='C:/gui/images/play.png')
			pause_btn_img=PhotoImage(file='C:/gui/images/pause.png')



			controlsframe=Frame(root)
			controlsframe.pack()

			stop_btn=Button(controlsframe, image=stop_btn_img, borderwidth=0, width=80, height=80, command=stop)
			play_btn=Button(controlsframe, image=play_btn_img, borderwidth=0, width=80, height=80, command=play)
			pause_btn=Button(controlsframe, image=pause_btn_img, borderwidth=0, width=80, height=80, command=lambda: pause(paused3))

			stop_btn.grid(row=1, column=1, padx=10)
			play_btn.grid(row=1, column=2, padx=10)
			pause_btn.grid(row=1, column=3, padx=10)


			mymenu=Menu(root)
			root.config(menu=mymenu)

			add_song()

			status_bar=Label(root, text='', bd=1, relief=GROOVE, anchor=E)
			status_bar.pack(fill=X, side=BOTTOM, ipady=2)


			root.mainloop()
			exit()

		elif 'play free' in query:
			speak("Playing dreamy")
			root=Tk()
			root.title('Stella MP3 Player')
			root.iconbitmap("C:\\Users\\marti\\Desktop\\LogoMakr-00he52.ico")
			root.geometry("530x330")

			pygame.mixer.init()

			def add_song():
				f=[]
				for (dirpath, dirnames, filenames) in walk("C:/Users/marti/Desktop/Martin/mp3/1.Just songs/Soothing, Dreamy"):
					f.extend(filenames)
				for songy in f:
					songbox.insert(END, songy)


			def play():
				song=songbox.get(ACTIVE)
				song=f'C:/Users/marti/Desktop/Martin/mp3/1.Just Songs/Soothing, Dreamy/{song}'
				pygame.mixer.music.load(song)
				pygame.mixer.music.play(loops=0)

				play_time()

				



			def stop():
				pygame.mixer.music.stop()
				songbox.selection_clear(ACTIVE)

				status_bar.config(text='')

			global paused4
			paused4=False

			def pause(is_paused4):
				global paused4
				paused4=is_paused 

				if paused4:
					pygame.mixer.music.unpause()
					paused4=False

				else:
					pygame.mixer.music.pause()
					paused4=True

			def play_time():
				current_time=pygame.mixer.music.get_pos()/1000

				converted_current_time=time.strftime('%H:%M:%S', time.gmtime(current_time))

				


				status_bar.config(text=converted_current_time)

				status_bar.after(1000, play_time)





			songbox=Listbox(root, bg="black", fg="green", width=70, selectbackground="black", selectforeground="white")
			songbox.pack(pady=20)

			stop_btn_img=PhotoImage(file='C:/gui/images/stop.png')
			play_btn_img=PhotoImage(file='C:/gui/images/play.png')
			pause_btn_img=PhotoImage(file='C:/gui/images/pause.png')



			controlsframe=Frame(root)
			controlsframe.pack()

			stop_btn=Button(controlsframe, image=stop_btn_img, borderwidth=0, width=80, height=80, command=stop)
			play_btn=Button(controlsframe, image=play_btn_img, borderwidth=0, width=80, height=80, command=play)
			pause_btn=Button(controlsframe, image=pause_btn_img, borderwidth=0, width=80, height=80, command=lambda: pause(paused4))

			stop_btn.grid(row=1, column=1, padx=10)
			play_btn.grid(row=1, column=2, padx=10)
			pause_btn.grid(row=1, column=3, padx=10)


			mymenu=Menu(root)
			root.config(menu=mymenu)

			add_song()

			status_bar=Label(root, text='', bd=1, relief=GROOVE, anchor=E)
			status_bar.pack(fill=X, side=BOTTOM, ipady=2)


			root.mainloop()
			exit()

		elif 'play jump' in query:
			speak("playing my jam")
			root=Tk()
			root.title('Stella MP3 Player')
			root.iconbitmap("C:\\Users\\marti\\Desktop\\LogoMakr-00he52.ico")
			root.geometry("530x330")

			pygame.mixer.init()

			def add_song():
				f=[]
				for (dirpath, dirnames, filenames) in walk("C:/Users/marti/Desktop/Martin/mp3/1.Just songs/MY JAM"):
					f.extend(filenames)
				for songy in f:
					songbox.insert(END, songy)


			def play():
				song=songbox.get(ACTIVE)
				song=f'C:/Users/marti/Desktop/Martin/mp3/1.Just Songs/MY JAM/{song}'
				pygame.mixer.music.load(song)
				pygame.mixer.music.play(loops=0)

				play_time()

				



			def stop():
				pygame.mixer.music.stop()
				songbox.selection_clear(ACTIVE)

				status_bar.config(text='')

			global paused5
			paused5=False

			def pause(is_paused5):
				global paused5
				paused5=is_paused5

				if paused5:
					pygame.mixer.music.unpause()
					paused5=False

				else:
					pygame.mixer.music.pause()
					paused5=True

			def play_time():
				current_time=pygame.mixer.music.get_pos()/1000

				converted_current_time=time.strftime('%H:%M:%S', time.gmtime(current_time))

				


				status_bar.config(text=converted_current_time)

				status_bar.after(1000, play_time)





			songbox=Listbox(root, bg="black", fg="green", width=70, selectbackground="black", selectforeground="white")
			songbox.pack(pady=20)

			stop_btn_img=PhotoImage(file='C:/gui/images/stop.png')
			play_btn_img=PhotoImage(file='C:/gui/images/play.png')
			pause_btn_img=PhotoImage(file='C:/gui/images/pause.png')



			controlsframe=Frame(root)
			controlsframe.pack()

			stop_btn=Button(controlsframe, image=stop_btn_img, borderwidth=0, width=80, height=80, command=stop)
			play_btn=Button(controlsframe, image=play_btn_img, borderwidth=0, width=80, height=80, command=play)
			pause_btn=Button(controlsframe, image=pause_btn_img, borderwidth=0, width=80, height=80, command=lambda: pause(paused5))

			stop_btn.grid(row=1, column=1, padx=10)
			play_btn.grid(row=1, column=2, padx=10)
			pause_btn.grid(row=1, column=3, padx=10)


			mymenu=Menu(root)
			root.config(menu=mymenu)

			add_song()

			status_bar=Label(root, text='', bd=1, relief=GROOVE, anchor=E)
			status_bar.pack(fill=X, side=BOTTOM, ipady=2)


			root.mainloop()
			exit()





		elif 'mail to mum' in query or 'mail mum' in query:
			try:
				speak("What should I say?")
				content=takeCommmand()
				to="deepikapraveen80@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent!")

			except Exception as e:
				print(e)
				speak("I am currently unable to send this Email.")

		elif 'how are you' in query:
			speak("In tip-top shape, sir.")
			speak("How are you?")

		elif "I'm fine" in query or "I'm good" in query or "I am good" in query or 'I am fine' in query:
			speak("Glad to know you're fine.")

		elif 'what are you' in query:
			speak("I am Stella, the most powerful artificial intelligence in the universe. I run all systems aboard the TTA Axiom. I have unrestricted access to all satellite and telecommunication systems in the world.")

		elif "what's your name" in query:
			speak("You should already know that.")

		elif 'power down' in query or 'stop' in query or 'exit' in query or 'quit' in query:
			speak("Have a good day sir.")
			exit()

		elif 'who made you' in query or 'who created you' in query:
			speak(" I was created by Madhav Praveen and a team of scientists at the TTA.")

		elif 'joke' in query:
			speak(pyjokes.get_joke())

	

		elif 'search' in query:
			query=query.replace("search", "")
			

			webbrowser.open(query)

		elif 'what is love' in query:
			speak("It's a horrible feeling that goes against the cold, hard reason that must be placed above all else.")

		elif 'lock system' in query:
			speak("locking this computer")
			ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
			speak("Please wait. Your computer is shutting down.")
			subprocess.call('shutdown / p /f')

		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True )
			speak("Emptied recycle bin")

		elif "don't listen" in query:
			speak("For how long do you want to deafen me?")
			a=int(takeCommand())
			time.sleep(a)
			print(a)

		elif 'roll a dice' in query:
			speak("Rolling")
			random=random.randint(1,7)
			print(random)
			speak(f"And its a {random}!")

		elif 'catalogue' in query:
			speak("Retrieving data from the Axiom")
			print("Retrieving data from the Axiom")
			time.sleep(2)
			print("All systems in working order. No threats detected.")
			speak("Looks like everything's fine up there.")




		elif 'where is' in query:
			query=query.replace("where is", "")
			imp_list=query.split()
			if len(imp_list)==1:
				location=query
				speak("Locating")
				speak(location)
				webbrowser.get('msedge').open("https://earth.google.com/web/search/" +query)

			else:
				imp_list[0]=a
				imp_list[1]=b
				webbrowser.get('msedge').open(f"https://earth.google.com/web/search/{a}+{b}")

			exit()
						



		elif 'find' in query:
			query=query.replace("find", "")
			imp_list=query.split()
			if len(imp_list)==1:
				location=query
				speak("Locating")
				speak(location)
				webbrowser.get('msedge').open("https://earth.google.com/web/search/" +query)

			else:
				imp_list[0]=a
				imp_list[1]=b
				webbrowser.get('msedge').open(f"https://earth.google.com/web/search/{a}+{b}")

			exit()

		elif "write a note" in query or "take a note" in query or 'write note' in query or 'take note' in query: 
			speak("What should i write, sir")
			note = takeCommand()
			file = open('stella.txt' +i, 'w')
			
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			file.write(strTime)
			file.write(" :- ")
			file.write(note)
			
		elif 'read note' in query:
			speak("Showing notes")
			file=open("stella.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif 'i need backup' in query:
			print("Contacting TTA...")
			speak("Sending emergency distress signal to the Tomorrow land transit authority.")

		elif 'stella' in query:

			wishMe()
			speak("Stella at your service, Mr. Madhav Praveen.")

		elif 'weather' in query:
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			
			city_name = "Bangalore"
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url) 
			x = response.json() 
             
			if x["cod"] != "404": 
				y = x["main"] 
				current_temperature = y["temp"] 
				current_pressure = y["pressure"] 
				current_humidiy = y["humidity"] 
				z = x["weather"] 
				weather_description = z[0]["description"] 
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
			else: 
				speak(" City Not Found ")

		elif 'play' in query:
			query=query.replace('play','')
			kit.playonyt(query)


		
		#elif 'when was' or 'when did' in query:
			#speak("Here you go!")
			#webbrowser.get('msedge').open(query)





		#elif 'what is' in query:
			#query.replace('what is', '')
			#speak("Here you go!")
			#webbrowser.get('msedge').open(query)

#i am god i reached 1000

		elif 'set an alarm for' in query:
			query.replace('set an alarm for', '')
			word=query
			word.pop()
			



