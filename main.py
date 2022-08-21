# Random Password GeneratorV0.1 by Hao
import random
import string
from tkinter import *


class Gui_class():

    def __init__(self, init_window):
        self.init_window = init_window
    # 生成界面
    def generate_ui(self):
        self.init_window.title("密码生成器V0.1")
        self.init_window.geometry("550x300")
        self.pwd_label = Label(self.init_window, text='密码显示: ')
        self.pwd_gen = Entry(self.init_window,width=35)
        self.gen_button = Button(self.init_window, text='生成密码',
                                 command=lambda: self.gen_pas(), height=2)
        self.clear_btn = Button(self.init_window, text='清空',
                                command=lambda: self.clear_pas(), height=2)

        self.pwd_label.grid(row=0, column=0)
        self.pwd_gen.grid(row=0, column=1)
        self.gen_button.grid(row=1, column=0, padx=20,pady=20, sticky='S')
        self.clear_btn.grid(row=1, column=1, pady=20,padx=20, sticky='S')

    # 生成密码
    def gen_pas(self):
        # 字母+符号+数字
        chars = string.ascii_letters + string.punctuation + string.digits
        pwd = ""
        pwd_len = random.randint(8,16)
        for i in range(pwd_len):
            pwd += random.choice(chars)
        print("生成的密码是" + pwd)
        self.pwd_gen.delete(0, END)
        self.pwd_gen.insert(0, pwd)
    # 清空密码
    def clear_pas(self):
        self.pwd_gen.delete(0, END)




if __name__ == '__main__':
    new_window = Tk()
    generator = Gui_class(new_window)
    generator.generate_ui()
    new_window.mainloop()



