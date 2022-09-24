from tkinter import*
from random import choice


def randomize():
    lengthPassword = e.get()
    e.delete(0, END)
    for i in range(int(lengthPassword)):
        e.insert(0, choice(alphabet))
def resetAll():
    e.delete(0, END)



root = Tk()
root.title('Генератор паролей')
root.geometry('500x400')
root.resizable(width=False, height=False)
root['bg'] = '#CCCCFF'
root.iconbitmap('logo.ico')

alphabet = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A',
            'B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z','_','-','.','@']



text1 = Label(text='Введите длину пароля:', font='Verdana 15', fg='#990066')
text1.place(relx=0.5, y=40, anchor=CENTER)

e = Entry(root, font='Verdana 13', fg='#34C924')
e.place(relx=0.5, y=100, anchor=CENTER)


btn1 = Button(root, text='Сгенерировать пароль', font=('Verdana', 12, 'bold'), command=randomize)
btn1.place(relx=0.5, y=200, anchor=CENTER)


btnReset = Button(root, text='Очистить форму', font=('Verdana', 12, 'bold'), command=resetAll)
btnReset.place(relx=0.5, y=300, anchor=CENTER)
root.mainloop()




