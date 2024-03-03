import pygame
import random
import time
from tkinter import *
from tkinter import messagebox
pygame.init()
time3 = pygame.time.Clock()
screen_width, screen_height = 700, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spaceships')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
redlife = 3
yellife = 3
spaceship_red_img = pygame.image.load("Material/spaceship_red.png")
spaceship_red_img = pygame.transform.scale(spaceship_red_img, (40, 90))
spaceship_yellow_img = pygame.image.load("Material/spaceship_yellow.png")
spaceship_yellow_img = pygame.transform.scale(spaceship_yellow_img, (40, 90))
bulletimg = pygame.image.load("Material/bullet.png")
bullet = pygame.transform.scale(bulletimg, (40, 20))
spaceship_red = pygame.Rect(20, 100, 10, 90)
spaceship_yellow = pygame.Rect(650, 200, 10, 90)
redlifes = pygame.font.Font(None, 30)
relliferender = redlifes.render('Жизни: ' + str(redlife), True, RED)

yellifes = pygame.font.Font(None, 30)
yelliferender = yellifes.render('Жизни: ' + str(yellife), True, YELLOW)

background = pygame.image.load("Material/space.png")
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mixer.init()
scoresound = pygame.mixer.Sound("Material/Grenade+1.mp3")
winsound = pygame.mixer.Sound("Material/win.wav")
shootsound = pygame.mixer.Sound("Material/Gun+Silencer.mp3")
keep_going = True
yspeed_yellow = 0
yspeed_red = 0
bulletred = []
bulletyel = []

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yspeed_yellow -= 5
            elif event.key == pygame.K_DOWN:
                yspeed_yellow += 5
            elif event.key == pygame.K_w:
                yspeed_red -= 5
            elif event.key == pygame.K_s:
                yspeed_red += 5
            elif event.key == pygame.K_f:
               bulletred.append([60, spaceship_red.y + 30] )
               shootsound.play()
            elif event.key == pygame.K_l:
               bulletyel.append([620, spaceship_yellow.y + 30])
               shootsound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                yspeed_yellow += 5
            elif event.key == pygame.K_DOWN:
                yspeed_yellow -= 5
            elif event.key == pygame.K_w:
                yspeed_red += 5
            elif event.key == pygame.K_s:
                yspeed_red -= 5
    screen.blit(background, (0, 0))
    for i in bulletred:
        screen.blit(bullet, (i[0], i[1]))
    for i in bulletyel:
        screen.blit(bullet, (i[0], i[1]))
    spaceship_yellow.y += yspeed_yellow
    spaceship_red.y += yspeed_red
    for i in bulletred:
        i[0] += 5
        if i[0] > 700:
           bulletred.remove(i)
    for i in bulletred:
        bullet_x, bullet_y = i[0], i[1]
        if (bullet_x+40 > spaceship_yellow.x and bullet_x < spaceship_yellow.x + 40 and
                bullet_y + 20 > spaceship_yellow.y and bullet_y < spaceship_yellow.y + 90):
                bulletred.remove(i)
                yellife -= 1
                scoresound.play()
                yelliferender = yellifes.render('Жизни: ' + str(yellife), True, GREEN)
    for i in bulletyel:
        i[0] -= 5
        if i[0] < 0:
            bulletyel.remove(i)
    for i in bulletyel:
        bullet_x, bullet_y = i[0], i[1]
        if (bullet_x + 40 > spaceship_red.x and bullet_x < spaceship_red.x + 40 and
                bullet_y + 20 > spaceship_red.y and bullet_y < spaceship_red.y + 90):
            bulletyel.remove(i)
            redlife -= 1
            scoresound.play()
            relliferender = redlifes.render('Жизни: ' + str(redlife), True, RED)
    if redlife == 0:
        window = Tk()
        window.geometry("500x400")
        window.withdraw()
        a = messagebox.askyesno("Перезапуск", "Игра окончена!\nПобедили желтые\nВы хотите перезапустить игру?")
        if a == TRUE:
            bulletred = []
            bulletyel = []
            redlife = 3
            yellife = 3
            yelliferender = yellifes.render('Жизни: ' + str(yellife), True, GREEN)
            relliferender = redlifes.render('Жизни: ' + str(redlife), True, RED)
            window.destroy()
        else:
            window.destroy()
            keep_going = False
        window.mainloop()
    if yellife == 0:
        for i in bulletred:
            bulletred.remove(i)
        for i in bulletyel:
            bulletyel.remove(i)
        window = Tk()
        window.geometry("500x400")
        window.withdraw()
        a = messagebox.askyesno("Перезапуск", "Игра окончена!\nПобедили красные\nВы хотите перезапустить игру?")
        if a == TRUE:
           bulletred = []
           bulletyel = []
           redlife = 3
           yellife = 3
           yelliferender = yellifes.render('Жизни: ' + str(yellife), True, GREEN)
           relliferender = redlifes.render('Жизни: ' + str(redlife), True, RED)
           window.destroy()
        else:
           window.destroy()
           keep_going = False
        window.mainloop()

    time3.tick(60)
    screen.blit(spaceship_red_img, (spaceship_red.x, spaceship_red.y))
    screen.blit(yelliferender,(500, 50))
    screen.blit(relliferender, (100, 50))
    screen.blit(spaceship_yellow_img, (spaceship_yellow.x, spaceship_yellow.y))
    pygame.display.update()
pygame.quit()
