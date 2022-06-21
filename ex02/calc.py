import tkinter as tk
import tkinter.messagebox as tkm
import random
def button_click(event):
    btn = event.widget
    num = btn["text"] #クリックされたボタンの文字
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END, res)

    elif num == "fill": #メッセージボックスを入力した数字で埋める。
        eqn2 = entry.get()
        res2 = int(eqn2)*9*12345679 
        entry.delete(0,tk.END)
        entry.insert(tk.END, res2)

    elif num == "rand": #ランダムに生成
        ketasu = int(entry.get())
        hoge = random.randint(1,10**ketasu)    
        entry.delete(0,tk.END)
        entry.insert(tk.END, hoge)

    elif num =="RSA":#p=19,q=31,秘密鍵d=13,公開鍵e=7,n=589でRSA暗号化する。
        ango = entry.get()
        ango2 = int(ango)**7
        ango3 = ango2%589
        entry.delete(0,tk.END)
        entry.insert(tk.END, f"RSA:{ango3}")
    
    elif num == "2進": #入力された値を二進数に変換する。
        nisin = int(entry.get())
        nisin2 = format(nisin,"b")
        entry.delete(0,tk.END)
        entry.insert(tk.END, nisin2)
    
    elif num == "8進": #入力された値を二進数に変換する。
        hatisin = int(entry.get())
        hatisin2 = format(hatisin,"o")
        entry.delete(0,tk.END)
        entry.insert(tk.END, hatisin2)
    
    elif num == "16進": #入力された値を二進数に変換する。
        jurokusin = int(entry.get())
        jurokusin2 = format(jurokusin,"x")
        entry.delete(0,tk.END)
        entry.insert(tk.END, jurokusin2)


    elif num == "Del":
        entry.delete(0,tk.END)
    else:
    #tkm.showinfo("",f"{num}のボタンが押されました。")
        entry.insert(tk.END, f"{num}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電話レンジ(仮)")
    #root.geometry("300x750")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0,column=0,columnspan=3)

    r ,c = 1, 0 # r:行番号 , c:列番号
    for i, num in enumerate([i for i in range(9,-1,-1)]+["+"]+["-"]+["*"]+["/"]+["="]+["fill"]+["rand"]+["RSA"]+["2進"]+["8進"]+["16進"]+["Del"]):
        button = tk.Button(root,
                           text=f"{num}",
                           width=4,
                           height=1,
                           font=("Times New Roman",30)
                           )  #()の中は改行できる！
        button.bind("<1>",button_click)
        button.grid(row=r, column=c,columnspan=1)
        c += 1
        if(i+1) % 5 == 0:
            r+=1
            c = 0
            
    root.mainloop()
