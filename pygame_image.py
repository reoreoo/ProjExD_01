import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.image.load("ex01/fig/3.png")
    bg_img2 =pg.transform.flip(bg_img2, True, False)
    bg_img3= pg.transform.rotozoom(bg_img2, 10, 1.0)
    lst=[bg_img2,bg_img3 ]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        
        screen.blit(bg_img, [0, 0])
        screen.blit(lst[tmr%2],[300,200])
            

        
        
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()