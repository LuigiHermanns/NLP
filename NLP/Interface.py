import customtkinter
import tkinter
from NLP import *

def basic_analysis(text,bloco_saida):

    text = remove_special_characters(text)
    text = replace_characters_with_accents(text)
    text = to_lowercase(text)

    tokens = tokenize_text(text)

    liwc_res = parsing_tokens(tokens)

    resp_dict = liwc_couting(liwc_res)
    
    total = resp_dict["word_count"]
    ofensivas = resp_dict["swear_count"]
    ansiosas = resp_dict["anx_count"]
    positivo = resp_dict["posemo%"]
    negativo =  resp_dict["negemo%"]

    label2.configure(text=f'Total de palavras: {total}\nPalavras ofensivas: {ofensivas}\nPalavras ansiosas: {ansiosas}\nTom geral positivo: {positivo:.2f}%\nTom geral negativo: {negativo:.2f}%')


# system, light and dark
customtkinter.set_appearance_mode("dark")

# dark-blue, blue and green
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Consulta de Texto")
root.geometry("500x800")

# create a window
frame = customtkinter.CTkFrame(root)
frame.pack(pady = 20,padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="Análise de Emoção", font=("Roboto", 24))
label.pack(pady=10,padx=12)

label_placeholder = customtkinter.CTkLabel(frame, text="Digite seu texto:", font=("Roboto", 16))
label_placeholder.pack(pady=10,padx=12)

text1 = customtkinter.CTkTextbox(frame, font=("Roboto", 14))
text1.configure(width=200, height=250)
text1.pack(pady=20,padx=30)

button2 = customtkinter.CTkButton(frame, text="Analisar", font=("Roboto", 14), command=lambda :basic_analysis(text1.get("1.0",'end-1c'),label2))
button2.pack(pady=20,padx=30)

label2 = customtkinter.CTkLabel(frame, text="", font=("Roboto", 24))
label2.pack(pady=10,padx=12)






root.mainloop()
