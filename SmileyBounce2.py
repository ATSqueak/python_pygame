import pygame # Setup

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550
timer = pygame.time.Clock()
speedx = 6
speedy = 6

while keep_going: # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speedx
    picy += speedy
    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew/2    
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))
    pygame.display.update()
    timer.tick(60)
pygame.quit() # Exit
