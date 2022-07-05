import pygame as pg
import sys

def main():
    clock = pg.time.Clock()          #時間計測用オブジェクト

    pg.display.set_caption("逃げろこうかとん")          #タイトルバーに文字表示
    screen = pg.display.set_mode((1600,900))           #800x600のウィンドウ作成
    screen_rect = screen.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    screen.blit(bgimg_sfc, bgimg_rect)

    koukaton = pg.image.load("fig/6.png")
    koukaton = pg.transform.rotozoom(koukaton, 0, 2.0) #サイズ変更
    koukaton_rect = koukaton.get_rect()                #Rect
    koukaton_rect.center = 900, 400
    

    while True:
        screen.blit(bgimg_sfc, bgimg_rect)
        screen.blit(koukaton, koukaton_rect)
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()    #モジュールを初期化する
    main()
    pg.quit()    #モジュールの初期化を解除する
    sys.exit()   #プログラムを終了する