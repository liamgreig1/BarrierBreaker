from translate import Translator
import assemblyai
import time
from gtts import gTTS
import os

#key for API
aai = assemblyai.Client(token='bbc8f48274684b24944a9ed0ec6056b7')

#Temp Text file
transcript = aai.transcribe(filename='example.txt')
#Audio File to be translated 
transcript = aai.transcribe(filename='Mum.mp3')

#takes audio from mp3 file and converts to text 
while transcript.status != 'completed':
    transcript = transcript.get()

#adds text to text variable
text = transcript.text

#prints the text
print("English: " + text)
print("\n")

#To Translate text from english to other language
def tran( toTran, lang ):
	translator= Translator(From_lang="autodetect", to_lang=lang)
	translation = translator.translate(toTran)
	print(lang+": "+translation)
	print("\n")
	transName = "Translated/" + lang + ".txt"
	print(transName)
	with open(transName, "w") as text_file:
		text_file.write(translation)
	return;

tran(text, "hu")
tran(text, "pt")
tran(text, "de")



#def backTran( fName, lang ):
#fiName = "Translated/" + fName + ".txt"
#calls text file to be read out by the computer 
fiName = "Translated/de.txt"
f = open(fiName, "r")

tts = gTTS(text=f.read(), lang='de')
tts.save("german.mp3")
os.system("german.mp3")


# translator= Translator(From_lang="autodetect", to_lang="Chinese")
# translation = translator.translate(text)
# print("Chinese: " + translation)

