import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("",f"{num}のボタンが押されました。")
    entry.insert(tk.END, f"{num}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電話レンジ(仮)")
    root.geometry("300x600")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0,column=0,columnspan=3)

    r ,c = 1, 0 # r:行番号 , c:列番号
    for i in range(9,-1,-1):
        button = tk.Button(root,
                           text=i,
                           width=4,
                           height=2,
                           font=("Times New Roman",30)
                           )  #()の中は改行できる！
        button.bind("<1>",button_click)
        button.grid(row=r, column=c)
        c += 1
        if(i-1) % 3 == 0:
            r+=1
            c = 0
    root.mainloop()
