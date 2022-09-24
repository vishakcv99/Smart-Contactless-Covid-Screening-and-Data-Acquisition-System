import speech_recognition as sr 
import os
from playsound import playsound
from text_to_speech import live_audio
import datetime
import database
import warning
import some
import capture

#gives a welcome converation
#return our choices
def start():
	os.system("clear")
	first = "To use audio function.. say audio ... To scan your i d ... say  scan"
	live_audio(first)
	primary = recon()
	print("Using audio function")
	return primary
	

#gives access to the functionality
#check for exact length of id 
#returns number
def access(primary):
	print("sad")	

	playsound("start_talk.mp3")
	check = True
	while check == True:
		fin = recon()
		fin = fin.replace(" ","")
		len_fin = len(fin)
		val = False
		if len_fin == 12:
			val = True
			flag = check_fin(fin)
			if flag == True:
				return fin
				check = False
			else:
				print("Try again ... ")
				access(primary)
			check = False

		elif len(fin) != 12:
			num = len(fin)
			print(num)
			if num > 12: 
				warning = f"Try agian ... Your number contains {num} digits"
				live_audio(warning)
				access(primary)
			elif num < 12:
				warning = f"Try again ... Your number contains only {num} digits"
				live_audio(warning)
				access(primary)
			return False

#gives wish by fetching time
def starter():
	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour <12:
		check = "good morning .."
		live_audio(check)

	elif hour >=12 and hour<18:

		check = "good afternoon .."
		live_audio(check)

	else:
		check = "good evening"
		live_audio(check)


#capture audio using google speech recognition
def recon():

	r = sr.Recognizer()
	dest_audio = sr.Microphone()


	with dest_audio as dest:
		r.adjust_for_ambient_noise(dest)
		#r.pause_threshold = 1
		audio = r.listen(dest)


	try:
		fin=r.recognize_google(audio)
		out = str(fin)
		return out

	except sr.UnknownValueError:
		print("google speech recognition failed to process the audio...Try again")
		playsound("google_speech_fail.mp3")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    playsound("server_error.mp3")
	


#check for characters in number
def vallidate_fin(fin):
	for i in fin:
		if fin != int:
			characters_error = "contains characters ..please speak numbers only"
			live_audio(characters_error)
			return False
		else:
			return True

#input is aadhar number and mobile number and returns boolean value
def database_fin_check(fin,mob):
	final = database.aadhar_check_fin(fin,mob)
	if final == True:
		succ = "Your number found in database...verified"
		live_audio(succ)
		return True
	else:
		fail = "We Could not find your number in our database ... Authentication denied "
		live_audio(fail)
		return False


def check_fin(fin):

	checking = "we are checking your number on our database"
	live_audio(checking)
	res = database.aadhar_check(fin)
	check_fin=""
	for number in str(fin): 
		num = number+ " "
		check_fin = check_fin+num
	if res == True:
		out =  "aadhar found in our database"
		live_audio(out)
		final_fin = "your card number is "+ check_fin
		live_audio(final_fin)
		return True
	else :
		final_fin = "we cannot find your i d ... Try again"
		live_audio(final_fin)
		return False


def stand():
	capture.capture()
	fin = some.working("saved_img.jpg")
	os.system("rm saved_img.jpg")	
	if fin :
		fin = fin.replace(" ","")
		#fin = str(fin)
		print(f"aadhaar is {fin}")
		
	elif fin == None:

		print("Try again ")
		warn = "Try again"
		live_audio(warn)
		fin = stand()
	return fin

def update_database_date(i):
	date_now = datetime.date.today()
	datenow = str(date_now)
	print(f"Today is : {date_now}")
	database.update_status(datenow,i)


def main():
	primary = start()
	print(primary)
	if primary == "audio" or primary == "Audio" :
		fin = access(primary)
		if fin == False:
			nice_day="have a nice day ... You are not allowed to go any further "
			live_audio(nice_day)
		else:
			num_in = "Please tell us your mobile number for verification"
			live_audio(num_in)
			num_mob = recon()
			final = database_fin_check(fin,num_mob)
			print(final)
			if final == True:
				update_database_date(fin)
			
			else:
				pass
	elif primary == "scan" or primary == "Scan":
		
		fin = stand()
		access = f"your aadhar scanned ..."
		print(access)
		live_audio(access)
		#fin = fin.replace(" ","")
		fin_id = check_fin(fin)
		print(f"Your aadhar number is {fin}")			
		if fin_id == True:
			update_database_date(fin)


if __name__ == '__main__':
	main()
