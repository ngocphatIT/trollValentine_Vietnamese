from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time
import pygame
class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("I <3 u")
        self.geometry("200x50")
        self.progressbar=Progressbar(self,orient=HORIZONTAL,length=100)
    def run(self):
        self.withdraw()
        title="I love you 3000"
        self.notify(title,"Sao bạn ấn vào đây dạ?")
        self.notify(title,"Chờ mình 1 tí")
        self.deiconify()
        Label(self,text="Bắt đầu mã hóa thiết bị").pack()
        self.progressbar.pack()
        self.step()
        self.withdraw()
        self.notify(title,"Mã hóa thiết bị thành công!")
        self.notify(title,"Để có thể giải mã...")
        self.notify(title,"Bạn cần trả lời câu hỏi sau bằng tiếng Anh")
        t="no"
        while t!="yes":
            t=messagebox.askquestion(title,"Be my Valentine?")
        self.notify(title,"Ngại quá đi! Tớ cũng thích cậu nữa!")
        self.notify(title,"Trời xanh mây trắng nắng vàng."+"\n"+"Không liên quan lắm nhưng mà thích cậu!")
    def notify(self,title,message):
        messagebox.showinfo(title,message)
    def step(self):
        for i in range (20):
            self.update_idletasks()
            self.progressbar['value']+=20
            time.sleep(0.1)
if __name__ == '__main__':
    pygame.mixer.init()
    pygame.mixer.music.load('P:\Python\music.mp3')
    pygame.mixer.music.play(loops=0)
    App=MainWindow()
    App.run()
    App.mainloop()
    