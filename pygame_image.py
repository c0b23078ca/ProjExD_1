import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_ing = pg.image.load("fig/3.png")
    kk_ing = pg.transform.flip(kk_ing, True, False)
    kk_rct = kk_ing.get_rect() #こうかとんRectの抽出
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img2, [-x+4800, 0])
        key_list = pg.key.get_pressed() # 全キーの押した状態を取得
        a = -1
        b = 0
        if key_list[pg.K_UP]:
            b = -1
        if key_list[pg.K_DOWN]:
            b = +1
        if key_list[pg.K_LEFT]:
            a = -2
        if key_list[pg.K_RIGHT]:
            a = +2        
        kk_rct.move_ip((a, b))
        # if key_list[pg.K_UP]:
        #     kk_rct.move_ip(0, -1)
        # if key_list[pg.K_DOWN]:
        #     kk_rct.move_ip(0, +1)
        # if key_list[pg.K_LEFT]:
        #     kk_rct.move_ip(-1, 0)
        # if key_list[pg.K_RIGHT]:
        #     kk_rct.move_ip(+2, 0)
        # else:
        #     kk_rct.move_ip(-1, 0)
        screen.blit(kk_ing, kk_rct) #kk_imgをkk_rectの設定にしたがって貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()