import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

def main():
    clock = pg.time.Clock()          #時間計測用オブジェクト
    index = 0
    pg.display.set_caption("逃げろこうかとん")          #タイトルバーに文字表示
    screen = pg.display.set_mode((1600,900))           #1600x900のウィンドウ作成
    screen_rect = screen.get_rect()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    screen.blit(bgimg_sfc, bgimg_rect)
    #タイトル画面の背景
    t_bgimg_sfc = pg.image.load("fig/sky14.png")
    t_bgimg_sfc = pg.transform.rotozoom(t_bgimg_sfc, 0, 0.84) #サイズ変更
    t_bgimg_rect = t_bgimg_sfc.get_rect()
    screen.blit(t_bgimg_sfc, t_bgimg_rect)
    #ハードモードの背景
    h_bgimg_sfc = pg.image.load("fig/hiru.jpeg")
    h_bgimg_rect = h_bgimg_sfc.get_rect()
    screen.blit(h_bgimg_sfc, h_bgimg_rect)

    #練習3 こうかとん
    koukaton = pg.image.load("fig/6.png")
    koukaton = pg.transform.rotozoom(koukaton, 0, 2.0) #サイズ変更
    koukaton_rect = koukaton.get_rect()                #Rect
    koukaton_rect.center = 900, 400

    #練習5 爆弾1
    bmimg = pg.Surface((20,20))
    bmimg.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg, (255, 0, 0), (10, 10), 10)
    bmimg_rect = bmimg.get_rect()
    bmimg_rect.centerx = random.randint(0, screen_rect.width)
    bmimg_rect.centery = random.randint(0, screen_rect.height)
    vx, vy = +1, +1 #練習6a

     #練習5 爆弾2
    bmimg1 = pg.Surface((20,20))
    bmimg1.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg1, (255, 0, 0), (10, 10), 10)
    bmimg1_rect = bmimg1.get_rect()
    bmimg1_rect.centerx = random.randint(0, screen_rect.width)
    bmimg1_rect.centery = random.randint(0, screen_rect.height)
    vx1, vy1 = +1, +1 #練習6a

     #練習5 爆弾3
    bmimg2 = pg.Surface((20,20))
    bmimg2.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg2, (255, 0, 0), (10, 10), 10)
    bmimg2_rect = bmimg2.get_rect()
    bmimg2_rect.centerx = random.randint(0, screen_rect.width)
    bmimg2_rect.centery = random.randint(0, screen_rect.height)
    vx2, vy2 = +1, +1 #練習6a

    

    while True:
        screen.blit(t_bgimg_sfc, t_bgimg_rect)
        font = pg.font.Font(None,70)
        txt = font.render("Select Level and push the button",True, "BLUE")
        screen.blit(txt,[400,600])
        font = pg.font.Font(None,80)
        txt = font.render("1:easy 2: nomal 3:hard",True, "YELLOW")
        screen.blit(txt,[500,700])
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_states = pg.key.get_pressed() 
        pg.display.update()
#レベル1
        if key_states[pg.K_1] == True:
            while True:
                screen.blit(bgimg_sfc, bgimg_rect)
                #練習2
                for event in pg.event.get():
                    if event.type == pg.QUIT: return
                #練習4
                key_states = pg.key.get_pressed() # 辞書
                if key_states[pg.K_UP]    == True: koukaton_rect.centery -= 1
                if key_states[pg.K_DOWN]  == True: koukaton_rect.centery += 1
                if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx -= 1
                if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx += 1
                #練習7
                if check_bound(koukaton_rect,screen_rect) != (1, 1): #領域外だったら
                    if key_states[pg.K_UP]    == True: koukaton_rect.centery += 1
                    if key_states[pg.K_DOWN]  == True: koukaton_rect.centery -= 1
                    if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx += 1
                    if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx -= 1
                screen.blit(koukaton, koukaton_rect)
                #練習6
                bmimg_rect.move_ip(vx, vy)
                #練習5 爆弾
                screen.blit(bmimg, bmimg_rect)
                #練習7
                yoko, tate = check_bound(bmimg_rect,screen_rect)
                vx *= yoko
                vy *= tate

                #練習8
                if koukaton_rect.colliderect(bmimg_rect):
                    tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
                    return

                pg.display.update()
                clock.tick(1000)
#レベル2  
        elif key_states[pg.K_2] == True:
            while True:
                screen.blit(bgimg_sfc, bgimg_rect)
                #練習2
                for event in pg.event.get():
                    if event.type == pg.QUIT: return
                #練習4
                key_states = pg.key.get_pressed() # 辞書
                if key_states[pg.K_UP]    == True: koukaton_rect.centery -= 1
                if key_states[pg.K_DOWN]  == True: koukaton_rect.centery += 1
                if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx -= 1
                if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx += 1
                #練習7
                if check_bound(koukaton_rect,screen_rect) != (1, 1): #領域外だったら
                    if key_states[pg.K_UP]    == True: koukaton_rect.centery += 1
                    if key_states[pg.K_DOWN]  == True: koukaton_rect.centery -= 1
                    if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx += 1
                    if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx -= 1
                screen.blit(koukaton, koukaton_rect)
                #練習6
                bmimg_rect.move_ip(vx, vy)
                bmimg1_rect.move_ip(vx1, vy1)
                #練習5 爆弾
                screen.blit(bmimg, bmimg_rect)
                screen.blit(bmimg1, bmimg1_rect)
                #練習7
                yoko, tate = check_bound(bmimg_rect,screen_rect)
                yoko1, tate1 = check_bound(bmimg1_rect,screen_rect)
                vx *= yoko
                vy *= tate
                vx1 *= yoko1
                vy1 *= tate1

                #練習8
                if koukaton_rect.colliderect(bmimg_rect):
                    tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
                    return
                elif koukaton_rect.colliderect(bmimg1_rect):
                    tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
                    return

                pg.display.update()
                clock.tick(1000)
#レベル3
        elif key_states[pg.K_3] == True:
            while True:
                screen.blit(h_bgimg_sfc, h_bgimg_rect)
                #練習2
                for event in pg.event.get():
                    if event.type == pg.QUIT: return
                #練習4
                key_states = pg.key.get_pressed() # 辞書
                if key_states[pg.K_UP]    == True: koukaton_rect.centery -= 1
                if key_states[pg.K_DOWN]  == True: koukaton_rect.centery += 1
                if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx -= 1
                if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx += 1
                #練習7
                if check_bound(koukaton_rect,screen_rect) != (1, 1): #領域外だったら
                    if key_states[pg.K_UP]    == True: koukaton_rect.centery += 1
                    if key_states[pg.K_DOWN]  == True: koukaton_rect.centery -= 1
                    if key_states[pg.K_LEFT]  == True: koukaton_rect.centerx += 1
                    if key_states[pg.K_RIGHT] == True: koukaton_rect.centerx -= 1
                screen.blit(koukaton, koukaton_rect)
                #練習6
                bmimg_rect.move_ip(vx, vy)
                bmimg1_rect.move_ip(vx1, vy1)
                bmimg2_rect.move_ip(vx2, vy2)
                #練習5 爆弾
                screen.blit(bmimg, bmimg_rect)
                screen.blit(bmimg1, bmimg1_rect)
                screen.blit(bmimg2, bmimg2_rect)
                #練習7
                yoko, tate = check_bound(bmimg_rect,screen_rect)
                yoko1, tate1 = check_bound(bmimg1_rect,screen_rect)
                yoko2, tate2 = check_bound(bmimg2_rect,screen_rect)
                vx *= yoko
                vy *= tate
                vx1 *= yoko1
                vy1 *= tate1
                vx2 *= yoko2
                vy2 *= tate2

                #練習8
                if koukaton_rect.colliderect(bmimg_rect):
                    tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
                    return
                elif koukaton_rect.colliderect(bmimg1_rect):
                    tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
                    return
                elif koukaton_rect.colliderect(bmimg2_rect):
                    tkm.showwarning("お前が殺した","こうかとんは死にました。あなたのせいで。")
                    return

                pg.display.update()
                clock.tick(1000)

def check_bound(rect, scr_rect):
    yoko,tate = +1, +1
    '''
    [1]rect:こうかとん or 爆弾のRect
    [2]scr_rect:スクリーンのRect
    '''
    if rect.left < scr_rect.left or scr_rect.right < rect.right:
        yoko = -1
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom:
        tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()    #モジュールを初期化する
    main()
    pg.quit()    #モジュールの初期化を解除する
    sys.exit()   #プログラムを終了する