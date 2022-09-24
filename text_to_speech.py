# Import the required module for text 
# to speech conversion
from gtts import gTTS
#to play an audio file
from playsound import playsound
import os



def live_audio(mytext):
	language = 'en'
	myobj = gTTS(text=mytext, lang=language, slow=False)
	myobj.save("number.mp3")

	playsound("number.mp3")

	os.system("rm number.mp3")



def input_text():

	mytext = input("enter text to play")
	# Language in which you want to convert
	language = 'en'
  
	# Passing the text and language to the engine, 
	# here we have marked slow=False. Which tells 
	# the module that the converted audio should 
	# have a high speed
	myobj = gTTS(text=mytext, lang=language, slow=False)
		  
	output = input("enter file to output(add .mp3 with the name) :")

	myobj.save(output)

	return output
	  
# Playing the converted file


def main():
	check = input("To use text to speech converter type yes !! To skip press any key and enter : ")
	if check == "yes" or check == "Yes" or check == "YES":
		out = input_text()
		playsound(out)

	else:
		pass
if __name__ == '__main__':
	
	main()
	new= "this is aswesome"
	live_audio(new)


#os.system("mpg321 welcome.mp3")


'''
import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

a = "Welcome to the club..."



# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix(c)
'''
