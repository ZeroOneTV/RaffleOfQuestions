from tkinter import *
import random
import tkinter

class Application:
    def __init__(self, master=None):
        self.fonteGlobal = ("Arial", "18","bold")
        self.fonteCONSTglobal = ("Arial", "12")
        self.master = master
        self.question = str
        self.answer = str

        self.ROOT = Frame(master)
        self.ROOT.pack()

        self.WidgetConstPergunta = Frame()
        self.WidgetConstPergunta.pack(side=TOP,anchor=W)

        self.WidgetConstResposta = Frame()
        self.WidgetConstResposta.pack(side=TOP,anchor=W)

        self.WidgetButton = Frame()
        self.WidgetButton.pack(pady=15,side=BOTTOM,anchor=S)

        self.perguntas = self.carregarPerguntas()
        self.respostas = self.carregarRespostas()
        self.dictQuestAndAnswer = self.transformarEmDict(perguntas=self.perguntas,respostas=self.respostas)

        self.CONSTpergunta = Label(self.WidgetConstPergunta, text="PERGUNTA:",bg='white')
        self.CONSTpergunta.config(font=self.fonteCONSTglobal,pady=15,padx=10)
        self.CONSTpergunta.pack(side=tkinter.LEFT)

        self.CONSTresposta = Label(self.WidgetConstResposta, text="RESPOSTA:")
        self.CONSTresposta.config(font=self.fonteCONSTglobal,pady=70,padx=10)
        self.CONSTresposta.pack(side=tkinter.LEFT)

        self.pergunta = Label(self.WidgetConstPergunta, text="Aqui será exibido as perguntas :)")
        self.pergunta.config(anchor=W,justify=LEFT,font=self.fonteGlobal,wraplength=500)
        self.pergunta.pack(side=tkinter.LEFT)

        self.resposta = Label(self.WidgetConstResposta, text="Aqui será exibido as respostas :)")
        self.resposta.config(font=self.fonteGlobal,wraplength=500)
        self.resposta.pack(side=tkinter.LEFT)

        self.criarNovaPR = Button(self.WidgetButton,text="Começar",)
        self.criarNovaPR.config(width=15,height=1,font=self.fonteCONSTglobal,command=self.mudarTexto)
        self.criarNovaPR.pack()

    def mudarTexto(self):
        if (self.criarNovaPR["text"] == "Começar"):
            self.question, self.answer = self.randomizarPerguntas()
            self.pergunta.config(text=self.question)
            self.resposta.config(text="")
            self.criarNovaPR.config(text="Exibir resposta")

        elif(self.criarNovaPR["text"] == "Exibir resposta"):
            self.resposta.config(text=self.answer)
            self.criarNovaPR.config(text="Próxima pergunta")

        elif(self.criarNovaPR["text"] == "Próxima pergunta"):
            self.question, self.answer = self.randomizarPerguntas()
            if((self.question == 0) and (self.answer == 0)):
                self.pergunta.config(text='Acabou as perguntas :D')
                self.resposta.config(
                    text="""
                    Tentei fazer um programa simples, 
                    mas que ajudasse a ficar mais interativo o sorteio.
                    Espero que tenham gostado!
                    Valeu falou \o/
                    """
                    )
                self.criarNovaPR.config(text="Acabou as perguntas :D",state=DISABLED,command=tkinter.END)
            else:
                self.pergunta.config(text=self.question)
                self.resposta.config(text="")
                self.criarNovaPR.config(text="Exibir resposta")
    
    def randomizarPerguntas(self):
        if(len(self.dictQuestAndAnswer) != 0):
            question, answer = random.choice(list(self.dictQuestAndAnswer.items()))
            del self.dictQuestAndAnswer[question]
            return question, answer
        else:
            return 0, 0

    def carregarPerguntas(self):
        perguntas = []
        with open('Perguntas.txt','r',encoding = 'utf-8') as perguntasSorteio:
            for line in perguntasSorteio:
                text = line.replace("\n","")
                perguntas.append(text)
        perguntasSorteio.close()
        return perguntas

    def carregarRespostas(self):
        respostas = []
        with open('Respostas.txt','r',encoding = 'utf-8') as respostasSorteio:
            for line in respostasSorteio:
                text = line.replace("\n","")
                respostas.append(text)
        respostasSorteio.close()
        return respostas

    def transformarEmDict(self,perguntas:list,respostas:list):
        dictionary = {}
        for i in range(len(perguntas)):
            dictionary[perguntas[i]] = respostas[i]   
        return dictionary

if __name__ == '__main__':
    root = Tk()
    root.geometry("900x700")
    root.resizable(FALSE,FALSE)
    Application(master=root)
    root.mainloop()

# perguntas = []
# respostas = []

# with open('Perguntas.txt','r',encoding = 'utf-8') as perguntasSorteio:
#     for line in perguntasSorteio:
#         text = line.replace("\n","")
#         perguntas.append(text)
# perguntasSorteio.close()

# with open('Respostas.txt','r',encoding = 'utf-8') as respostasSorteio:
#     for line in respostasSorteio:
#         text = line.replace("\n","")
#         respostas.append(text)
# respostasSorteio.close()

# dicQ = {}

# for i in range(len(perguntas)):
#     dicQ[perguntas[i]] = respostas[i]

# while(len(dicQ) != 0):
#     question, answer = random.choice(list(dicQ.items()))
#     perguntas.remove(question)
#     respostas.remove(answer)
#     del dicQ[question]
#     print("{}".format(question))
#     input()
#     print("{}".format(answer))
#     input()
#     os.system('cls')
# print("Todas as perguntas foram realizadas :D")  
# print("Fim do programa")
# input()