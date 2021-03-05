import random
import tkinter as tk




       
def zarat11():
    random1 = random.randint(1, 6)
    sayı["text"]=random1
    sayı.pack()



form = tk.Tk()
form.title("Zar Oyunu !")
form.geometry("200x130")
zarat = tk.Button(text="Zar At!",font=50,command = zarat11)
zarat.place(x = 57, y = 80)
form.resizable(False,False)
sayı = tk.Label(text="Gelme",font=100)
label = tk.Label(text="Kenan Tarafından Yapıldı")
label.pack()


form.mainloop
