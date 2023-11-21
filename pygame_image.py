import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2=pg.transform.flip(bg_img, True, False)
    kk_img2 = pg.image.load("ex01/fig/3.png")
    kk_img2 =pg.transform.flip(kk_img2, True, False)
    kk_img3=[kk_img2]
    suuti=[2,4,6,8,10,12,10,8,6,4,2]
    for i in suuti:
        kk_img3.append(pg.transform.rotozoom(kk_img2, i, 1.0))
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x=tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(kk_img3[int(tmr%(len(suuti)*8)/8)],[300,200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()