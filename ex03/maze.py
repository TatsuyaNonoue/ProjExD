import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
def change_photo(event): #ボタンを押したらそのマスだけで画像が変わる。
    global key,tori,mx,my,cx,cy
    key = event.keysym #keysym→押されたキーの値を取得
    #if key == "1":
    #    tori = tk.PhotoImage(file="fig/1.png")
    #    canvas.create_image(cx, cy, image=tori, tag="tori")
    #elif key == "2":
    #    tori = tk.PhotoImage(file="fig/2.png")
    #    canvas.create_image(cx, cy, image=tori, tag="tori")
    #else:
    #    tori = tk.PhotoImage(file="fig/8.png")
    #    canvas.create_image(cx, cy, image=tori, tag="tori")

def key_down(event):
    global key
    key = event.keysym #keysym→押されたキーの値を取得

def key_up(event):
    global key
    key = ""

def main_proc():    #()の中にeventを入れるのはバインドするときのみ。
    global cx, cy, mx, my #keyはglobal変数だが書き換えてないので宣言しなくてよい。
    el = {  #キー：押されているキーkey/値：移動量リスト
         "Up"   :[0, -1],
         "Down" :[0, +1],
         "Left" :[-1, 0],
         "Right":[+1, 0],
         }
    #cx, cy = cx+el[key][0], cy+el[key][1]
    try:
        if maze_bg[my+el[key][1]][mx+el[key][0]] == 0: #もし移動先が床なら
            my, mx = my+el[key][1], mx + el[key][0]
        elif maze_bg[my+el[key][1]][mx+el[key][0]] == 1: #もし移動先が壁なら
            mm.show_maze2(canvas, maze_bg) #canvasにmaze_bgを貼る
            tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
            
    except:
        pass
    # if文の場合
    #if key == "Up": my -= 1
    #if key == "Down": my += 1
    #if key == "Left": mx -= 1
    #if key == "Right": mx += 1
    cx, cy= mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk() #ウィンドウを作成
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(15, 9) #1:壁/0:床を表す二次元リスト
    mm.show_maze(canvas, maze_bg) #canvasにmaze_bgを貼る。

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    tori = tk.PhotoImage(file="fig/8.png")
    mx, my =1, 1
    cx, cy= mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")
    #root.bind("<KeyPress>", change_photo)
    
    main_proc()
    root.mainloop()
