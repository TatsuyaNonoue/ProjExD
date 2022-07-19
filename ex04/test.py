import pygame as pg
import sys

def main():
    clock = pg.time.Clock()          #時間計測用オブジェクト

    pg.display.set_caption("試作型pygame") #タイトルバーに文字表示
    screen = pg.display.set_mode((800,600))         #800x600のウィンドウ作成

    tori_img = pg.image.load("fig/6.png")              #Surface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0) #Surface
    tori_rect = tori_img.get_rect()                    #Rect
    tori_rect.center = 900, 400
    screen.blit(tori_img, tori_rect) #tori_image Surfaceをtori_rectに従って貼り付ける。
    
    clock.tick(0.2) #1秒間に0.2フレーム　→　5秒で1FPS

if __name__ == "__main__":
    pg.init()    #モジュールを初期化する
    main()
    pg.quit()    #モジュールの初期化を解除する
    sys.exit()   #プログラムを終了する