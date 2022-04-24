import speech_recognition as sr

class Microfone:
    def __init__(self,frase="",idiomafala=""):
        self.frase =frase
        self.idiomafala = idiomafala
        pass

    def ouvirMicro(self):
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)
            try:
                #Passa o audio para o reconhecedor de padroes do speech_recognition
                self.frase = microfone.recognize_google(audio,language=self.idiomafala)
                print(self.frase)
            except:
                pass

#min = Microfone()
#min.ouvirMicro()