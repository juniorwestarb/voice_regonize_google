import speech_recognition as spech
from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
	create = gTTS(audio,lang='pt-br')
	create.save('audios/reconhecimento.mp3')
	print("Você disse isso?")
	playsound('audios/reconhecimento.mp3')


def ouvir():
	microfone = spech.Recognizer()
	with spech.Microphone() as source:
		#Reduz ruído
		microfone.adjust_for_ambient_noise(source)
		print("Diga alguma coisa: ")
		#Armazena o audio
		audio = microfone.listen(source)


	try:
		#Passa o audio para o speech_recognition para aplicação de reconhecimento de padrões
		frase = microfone.recognize_google(audio, language='pt-BR')
		print("Você quiz dizer: " + frase)

	except spech.UnkownValueError:
		print("Não entendi")

	return frase

reconhecimento = ouvir()
cria_audio(reconhecimento)
