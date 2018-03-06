from tkinter import *

clicks = 0

def click_button():
    global clicks
    clicks += 1
    buttonText.set("Clicks {}".format(clicks))

root = Tk() #создал окно
root.title("Единый я хочу написать полезные программы на Python") # Задал заголовок главного окна
root.geometry("400x300+300+250") # размер окна и позиционирование на экране

buttonText = StringVar()
buttonText.set("Clicks {}".format(clicks))

btn = Button(textvariable=buttonText,     # Текст кнопки
             background="#555", # Фоновый цвет кнопки
             foreground="#ccc", # Цвет текста
             activebackground="#D3D3D3",# Цвет фона когда кнопка нажата или наведен курсор
             highlightcolor="#555",
             padx="20",         # Отступ надписи от границ кнопки
             pady="8",          # Отсуп по Y
             font="16", command=click_button)         # Создаеться кнопка с тектом
btn.pack() #метод пак делает кнопку видимой

root.mainloop()#бесконечный цикл окна