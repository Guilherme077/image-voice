from imagevoice.encode import encodeMessage
from imagevoice.decode import decodeFromImage
import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox

img_path = ''

def selectFile():
    global img_path
    file_path = filedialog.askopenfilename(title="Abrir imagem PNG - ImageVoice", filetypes=[("png", "*.png")])
    if file_path:
        label.configure(text=f"Imagem Selecionada: {file_path}")
        img_path = file_path

def encodeBtn():
    encodeMessage(messageToEncode.get(), img_path,'nout.png')
    messagebox.showinfo("Concluído", "A mensagem foi gravada na imagem e salva como out.png. O arquivo de imagem original NÃO foi alterado.", icon='info')

def decodeBtn():
    messageDecoded = decodeFromImage(img_path)
    messagebox.showinfo("Mensagem Decodificada", messageDecoded)

ctk.set_appearance_mode('system')
window = ctk.CTk()
window.title('ImageVoice GUI')
window.geometry('700x500')

button = ctk.CTkButton(window, text="Escolher Imagem", command=selectFile)
button.pack(pady=20)

label = ctk.CTkLabel(window,text='Nenhuma imagem selecionada!')
label.pack(pady=30)
messageToEncode = ctk.CTkEntry(window, placeholder_text='Mensagem')
messageToEncode.pack(pady=10)
ctk.CTkButton(window,text='Inserir mensagem',command=encodeBtn,font=("Arial", 20),fg_color="Green").pack(pady=20)
ctk.CTkButton(window,text='Ler mensagem',command=decodeBtn,font=("Arial", 20),fg_color="Green").pack(pady=30)


window.mainloop()