from translate import Translator
import assemblyai
import time
from gtts import gTTS
import os

aai = assemblyai.Client(token='bbc8f48274684b24944a9ed0ec6056b7')

transcript = aai.transcribe(filename='example.txt')
transcript = aai.transcribe(filename='Intro.mp3')

while transcript.status != 'completed':
    transcript = transcript.get()

text = transcript.text
print("English: " + text)
print("\n")

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


def backTran( fName, lang ):
	fiName = "Translated/" + fName + ".txt"
	f = open("Translated/German.txt", "r")

	tts = gTTS(text=f.read(), lang='de')
	tts.save("german.mp3")
	os.system("german.mp3")


# translator= Translator(From_lang="autodetect", to_lang="Chinese")
# translation = translator.translate(text)
# print("Chinese: " + translation)

