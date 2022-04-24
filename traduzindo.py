from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

from requests import delete

class MeuTradutor:
    def __init__(self,fala="",idioma="",traduzido="") :
        self.textoTraduza=fala
        self.idioma=idioma
        self.traduzido = traduzido
        self.sisteminha = os.path.abspath(os.path.dirname(__file__))

    def  traduz(self):
        #pip install googletrans==4.0.0-rc1  https://py-googletrans.readthedocs.io/en/latest/
        
        translator = Translator()
       
        self.traduzido = translator.translate(self.textoTraduza, dest=self.idioma).text

        #print(self.traduzido)

        voz = gTTS(self.traduzido, lang=self.idioma)
        voz.save("./arquivos/voz.mp3")
        falar = self.sisteminha + "\\arquivos\\voz.mp3"
        playsound(falar)

        os.remove(falar)

'''ola = MeuTradutor()
ola.textoTraduza="Bonito e gostoso"
ola.idioma='en'
ola.traduz()'''