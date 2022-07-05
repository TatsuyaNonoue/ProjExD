import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()          #時間計測用オブジェクト

    pg.display.set_caption("逃げろこうかとん")          #タイトルバーに文字表示
    screen = pg.display.set_mode((1600,900))           #800x600のウィンドウ作成
    screen_rect = screen.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    screen.blit(bgimg_sfc, bgimg_rect)

    #練習3 こうかとん
    koukaton = pg.image.load("fig/6.png")
    koukaton = pg.transform.rotozoom(koukaton, 0, 2.0) #サイズ変更
    koukaton_rect = koukaton.get_rect()                #Rect
    koukaton_rect.center = 900, 400

    #練習5 爆弾
    bmimg = pg.Surface((20,20))
    bmimg.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg, (255, 0, 0), (10, 10), 10)
    bmimg_rect = bmimg.get_rect()
    bmimg_rect.centerx = random.randint(0, screen_rect.width)
    bmimg_rect.centery = random.randint(0, screen_rect.height)

    while True:
        screen.blit(bgimg_sfc, bgimg_rect)
        screen.blit(koukaton, koukaton_rect)
        screen.blit(bmimg, bmimg_rect)
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        pg.display.update()
        clock.tick(1000)

        #練習4
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True: koukaton_rect.centery -= 1
        if key_states[pg.K_DOWN]  == True: koukaton_rect.centery += 1
        if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx -= 1
        if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx += 1
        screen.blit(koukaton, koukaton_rect)
        
        #練習5 爆弾
        screen.blit(bmimg, bmimg_rect)
            

if __name__ == "__main__":
    pg.init()    #モジュールを初期化する
    main()
    pg.quit()    #モジュールの初期化を解除する
    sys.exit()   #プログラムを終了する