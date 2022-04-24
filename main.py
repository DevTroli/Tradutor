from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import os
from traduzindo import MeuTradutor
from ouvindo import Microfone



class TelaInicial:
    def __init__(self ):
        self.criarTela()
        
        
    def callbackFunc(self,event):
        LANGUAGES = {
            'af': 'afrikaans',
            'sq': 'albanian',
            'am': 'amharic',
            'ar': 'arabic',
            'hy': 'armenian',
            'az': 'azerbaijani',
            'eu': 'basque',
            'be': 'belarusian',
            'bn': 'bengali',
            'bs': 'bosnian',
            'bg': 'bulgarian',
            'ca': 'catalan',
            'ceb': 'cebuano',
            'ny': 'chichewa',
            'zh-cn': 'chinese (simplified)',
            'zh-tw': 'chinese (traditional)',
            'co': 'corsican',
            'hr': 'croatian',
            'cs': 'czech',
            'da': 'danish',
            'nl': 'dutch',
            'en': 'english',
            'eo': 'esperanto',
            'et': 'estonian',
            'tl': 'filipino',
            'fi': 'finnish',
            'fr': 'french',
            'fy': 'frisian',
            'gl': 'galician',
            'ka': 'georgian',
            'de': 'german',
            'el': 'greek',
            'gu': 'gujarati',
            'ht': 'haitian creole',
            'ha': 'hausa',
            'haw': 'hawaiian',
            'iw': 'hebrew',
            'he': 'hebrew',
            'hi': 'hindi',
            'hmn': 'hmong',
            'hu': 'hungarian',
            'is': 'icelandic',
            'ig': 'igbo',
            'id': 'indonesian',
            'ga': 'irish',
            'it': 'italian',
            'ja': 'japanese',
            'jw': 'javanese',
            'kn': 'kannada',
            'kk': 'kazakh',
            'km': 'khmer',
            'ko': 'korean',
            'ku': 'kurdish (kurmanji)',
            'ky': 'kyrgyz',
            'lo': 'lao',
            'la': 'latin',
            'lv': 'latvian',
            'lt': 'lithuanian',
            'lb': 'luxembourgish',
            'mk': 'macedonian',
            'mg': 'malagasy',
            'ms': 'malay',
            'ml': 'malayalam',
            'mt': 'maltese',
            'mi': 'maori',
            'mr': 'marathi',
            'mn': 'mongolian',
            'my': 'myanmar (burmese)',
            'ne': 'nepali',
            'no': 'norwegian',
            'or': 'odia',
            'ps': 'pashto',
            'fa': 'persian',
            'pl': 'polish',
            'pt': 'portuguese',
            'pa': 'punjabi',
            'ro': 'romanian',
            'ru': 'russian',
            'sm': 'samoan',
            'gd': 'scots gaelic',
            'sr': 'serbian',
            'st': 'sesotho',
            'sn': 'shona',
            'sd': 'sindhi',
            'si': 'sinhala',
            'sk': 'slovak',
            'sl': 'slovenian',
            'so': 'somali',
            'es': 'spanish',
            'su': 'sundanese',
            'sw': 'swahili',
            'sv': 'swedish',
            'tg': 'tajik',
            'ta': 'tamil',
            'te': 'telugu',
            'th': 'thai',
            'tr': 'turkish',
            'uk': 'ukrainian',
            'ur': 'urdu',
            'ug': 'uyghur',
            'uz': 'uzbek',
            'vi': 'vietnamese',
            'cy': 'welsh',
            'xh': 'xhosa',
            'yi': 'yiddish',
            'yo': 'yoruba',
            'zu': 'zulu'}
        
        valorCombo = LANGUAGES[self.comboIdioma.get()].upper()
        self.LblIdioSel.config(text=valorCombo)
        print(valorCombo)
        

    def criarTela(self):
        #criar tela
        self.root = Tk()
        self.root.title('Tradutor Universal')
        self.root.geometry('500x640+100+100')
        self.root['bg']= 'SkyBlue'
        self.root.resizable(width=False, height=False)
        self.root.iconphoto(True, PhotoImage(file=r'.\\arquivos\\mundo.png'))
        linguagem = ('af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn'
        ,'zh-tw','co','hr','cs','da','nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','he','hi'
        ,'hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml'
        ,'mt','mi','mr','mn','my','ne','no','or','ps','fa','pl','pt','pa','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','ug','uz','vi','cy','xh','yi','yo','zu')
        

        #cria botões
        LbfTexto = LabelFrame(self.root,width=20 , text="Texto para Tradução", bg="SkyBlue", fg="DeepSkyBlue")
        LbfTexto.grid(column=0, row=0, padx=20, pady=20)
        LblTraduzir =Label(LbfTexto,bd=8, bg ='SkyBlue',text="Texto:", fg='black',font=('arial',9,'bold'))
        LblTraduzir.grid(column=0, row=0, padx=20, pady=20)
        self.TxtTraduzir = Text(LbfTexto, fg='black',font=('arial',9,'bold'),height=12,width=40)
        self.TxtTraduzir.grid(column=1, row=0, padx=20, pady=20)

        LblIdioma =Label(self.root,bd=8, bg ='SkyBlue',text="Traduzir para: ", fg='black',font=('arial',9,'bold'))
        LblIdioma.place(relx=0.10,rely=0.42)
        self.comboIdioma = ttk.Combobox(self.root)
        self.comboIdioma.place(relx=0.30,rely=0.42)
        self.comboIdioma['values'] = linguagem
        self.comboIdioma.current(21)
        self.comboIdioma.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.LblIdioSel =Label(self.root,bd=8, bg ='DeepSkyBlue',text="ENGLISH", fg='black',font=('arial',9,'bold'))
        self.LblIdioSel.place(relx=0.6,rely=0.42)


        LbfTextoF = LabelFrame(self.root,width=19 , text="Texto Traduzido", bg="SkyBlue", fg="DeepSkyBlue")
        LbfTextoF.grid(column=0, row=2, padx=20, pady=20)
        LblTraduzido =Label(LbfTextoF,bd=8, bg ='SkyBlue',text="Tradução:", fg='black',font=('arial',9,'bold'))
        LblTraduzido.grid(column=0, row=0, padx=20, pady=20)
        self.TxtTraduzido = Text(LbfTextoF, fg='black',font=('arial',9,'bold'),height=12,width=40)
        self.TxtTraduzido.grid(column=1, row=0, padx=20, pady=20)
        
        LblIdiomaF =Label(self.root,bd=8, bg ='SkyBlue',text="Falar em:", fg='black',font=('arial',9,'bold'))
        LblIdiomaF.place(relx=0.10,rely=0.88)
        self.comboIdiomaF = ttk.Combobox(self.root)
        self.comboIdiomaF.place(relx=0.30,rely=0.88)
        self.comboIdiomaF['values'] = linguagem
        self.comboIdiomaF.current(74)

        self.botaoAbre = Button(self.root, text="Digitar", bg ='DeepSkyBlue',width=15,fg='black',font=('arial',9,'bold'),command=self.funcaoTraduzaTexto)
        self.botaoAbre.place(relx=0.10,rely=0.94)
        self.botaosalva = Button(self.root, text="Falar", bg ='DeepSkyBlue',width=15, fg='black',font=('arial',9,'bold'),command=self.funcaoTraduzaVoz)
        self.botaosalva.place(relx=0.60,rely=0.94)

        #self.TesteScale = Scale(self.root)
        #self.TesteScale.place(relx=0.40,rely=0.50)

       
        #ativa a tela
        self.root.mainloop()

    def funcaoTraduzaTexto(self):
            try:
                mensagem =self.TxtTraduzir.get(1.0, 'end')
                
                if len(mensagem) > 1:
                    trad = MeuTradutor()
                    trad.textoTraduza=mensagem
                    trad.idioma=self.comboIdioma.get()
                    trad.traduz()
                    self.TxtTraduzido.insert('end',trad.traduzido)
                    self.root.update()
                else:
                    tkMessageBox.showerror('Texto Vazio', "Favor preencher o texto!")
            except:
                tkMessageBox.showerror('Algo Errado', "Tente novamente!")
        
        

    def funcaoTraduzaVoz(self):
        try:
            mic = Microfone()
            mic.idiomafala = self.comboIdiomaF.get()
            mic.ouvirMicro()
            self.TxtTraduzir.insert('end',mic.frase)
            self.root.update()
            self.funcaoTraduzaTexto()
        except:
                tkMessageBox.showerror('Algo Errado', "Tente novamente!")


    
   
TelaInicial()