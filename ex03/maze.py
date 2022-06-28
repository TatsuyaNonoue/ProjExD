from calendar import leapdays
import tkinter as tk

def key_down(event):
    global key
    key = event.keysym #keysym→押されたキーの値を取得

def key_up(event):
    global key
    key = ""

def main_proc():    #()の中にeventを入れるのはバインドするときのみ。
    global cx, cy #keyはglobal変数だが書き換えてないので宣言しなくてよい。
    el = {  #キー：押されているキーkey/値：移動量リスト
        ""     :[0, 0], 
        "Up"   :[0, -20],
        "Down" :[0, +20],
        "Left" :[-20, 0],
        "Right":[+20, 0],
        }
    cx, cy = cx+el[key][0], cy+el[key][1]
# if文の場合
    #if key == "Up": cy -= 20
    #if key == "Down": cy += 20
    #if key == "Left": cx -= 20
    #if key == "Right": cx -= 20
    canvas.coords("tori", cx, cy)
    root.after(50,main_proc)


if __name__ == "__main__":
    root = tk.Tk() #ウィンドウを作成
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    tori = tk.PhotoImage(file="fig/2.png")
    cx, cy= 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()
    root.mainloop()
