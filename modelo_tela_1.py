from tkinter import*
from tkinter import font
from PIL import ImageTk, Image 


janela = Tk()

#estética 
janela.title('Na trilha da adaptação')
janela.geometry("400x400")
janela.iconbitmap('C:\\Users\\decer\\OneDrive\\Documentos\\plant.ico')
bg=PhotoImage(file= 'C:\\Users\\decer\\OneDrive\\Documentos\\botanica.png') 
my_label = Label(janela,image=bg) 
my_label.place(x=1,y=1,relwidth=1,relheight=1)

tentativa1_jogo= Label (janela, text="Na trilha da adaptação",font=('comic-sans',20), bg='#FFFFFF')
tentativa1_jogo.pack()

#escolhas
botao1= Button(janela,text="Começar",padx=5, pady=5, command= janela.quit) 
texto_botao1= Label(janela, text= '') 
botao1.pack()
#botao2= Button(janela,text="Ambiente xerofitico",padx=5, pady=5, command=janela.quit) 
#botao2.grid(column=10,row=4)
#botao3= Button(janela,text="Ambiente hidrofítico",padx=5, pady=5, command=janela.quit) 
#botao3.grid(column=10,row=7)


janela = mainloop()