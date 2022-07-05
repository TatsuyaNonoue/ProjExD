import pygame as pg
import sys

def main():
    clock = pg.time.Clock()          #時間計測用オブジェクト

    pg.display.set_caption("逃げろこうかとん") #タイトルバーに文字表示
    screen = pg.display.set_mode((1600,900))         #800x600のウィンドウ作成

if __name__ == "__main__":
    pg.init()    #モジュールを初期化する
    main()
    pg.quit()    #モジュールの初期化を解除する
    sys.exit()   #プログラムを終了する