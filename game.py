import pygame, sys, random
import pygame.locals as G_G
import pygame.event as G_E

pygame.init()

width = 420
height = 300
_caption = 'تا ... کد'
windowColor = (0, 20, 50)
WallColor = (230, 220, 240)
PlayerColor = (255, 100, 150)
EndColor = (255, 160, 20)
first_win = False

#اندازه صفحه برنامه
window = pygame.display.set_mode((width, height))

#تیتر برنامه
pygame.display.set_caption(_caption)

#آیکون برنامه
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)

#تصویر دیجیکالا
digikala = pygame.image.load('digikala.png')

class Player(object):

    def __init__(self):
        #خانه شروع بازیکن
        self.rect = pygame.Rect(25, 260, 10, 10)

    def move(self,dx,dy):
        if dx != 0:
            self.move_(dx,0)
        if dy != 0:
            self.move_(0,dy)

    def move_(self,dx,dy):
        #مقدار حرکت بازیکن
        self.rect.x += dx
        self.rect.y += dy

        #لود کردن موزیک برای برخورد با دیوار
        pygame.mixer.music.load('beeb.mp3')

        # برخورد با دیوار ها
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                    #self.rect = pygame.Rect(25, 260, 10, 10)
                    pygame.mixer.music.play(0, 0.0)
                if dx < 0:
                    self.rect.left = wall.rect.right
                    self.rect = pygame.Rect(25, 260, 10, 10)
                    pygame.mixer.music.play(0, 0.0)
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    self.rect = pygame.Rect(25, 260, 10, 10)
                    pygame.mixer.music.play(0, 0.0)
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    self.rect = pygame.Rect(25, 260, 10, 10)
                    pygame.mixer.music.play(0, 0.0)


#کلاس ساخت دیوارها
class Wall(object):

    def __init__(self,pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0],pos[1],20,20)

walls = []
level1 = [
    "HHHHHHHHHHHHHHHHHHHHH",
    "H                   H",
    "H H HHHHHHHHHHHHHHH H",
    "H H H         H   H H",
    "H H H HHHHHHHHH H H H",
    "H H H         H H H H",
    "H H HHHHHHHHH H H H H",
    "H H H       H H H H H",
    "H H H       H H H H H",
    "H H H       H H H H H",
    "H HHHHHHHHHHH H H H H",
    "H             H H H H",
    "H HHHHHHHHHHHHH H H H",
    "H           H   H   H",
    "HHHHHHHHHHHHHGHHHHHHH",
]
level2 = [
    "HHHHHHHHHHHHHHHHHHHHH",
    "H                   H",
    "H H HHHHHHHHH HHHHH H",
    "H H H         H   H H",
    "H H H HHHHHHHHH H H H",
    "H H H         H H H H",
    "H H HHHHHHHHH H H H H",
    "H H H       H H H H H",
    "H H H       H H H H H",
    "H H H       H H H H H",
    "H HHHHHHHHHHH H H H H",
    "H H           H H H H",
    "H H HHHHHHHHHHHHH H H",
    "H H             H   H",
    "HHHHHHHHHHHHHGHHHHHHH",
]

#ساخت دیوار ها و هدف
def CreateMap(level):
    x = y = 0
    global end_rect
    for row in level:
        for col in row:
            if col == "H":
                Wall((x,y))
            if col == "G":
                end_rect = pygame.Rect(x,y,20,20)
            x += 20
        y += 20
        x = 0


player = Player()
CreateMap(level1)

#کاهش سرعت برنامه
s = pygame.time.Clock()

while True:

    #سرعت اجرای برنامه
    s.tick(15)

    # رنگ پس زمینه برنامه
    window.fill(windowColor)

    #نمایش تصویر دیجیکالا
    window.blit(digikala, (100, 130))

    #دستور خاتمه برنامه
    for event in G_E.get():
        if event.type == G_G.QUIT:
            pygame.quit()
            sys.exit()

    #دستورات حرکت بازیکن با کلید ها
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-5,0)
    if key[pygame.K_RIGHT]:
        player.move(5,0)
    if key[pygame.K_UP]:
        player.move(0,-5)
    if key[pygame.K_DOWN]:
        player.move(0,5)

    #رسیدن به هدف
    if player.rect.colliderect(end_rect):
        walls = []
        player = Player()
        CreateMap(level2)
        if first_win:
            pygame.quit()
            sys.exit()
        first_win = True



    #رنگ دیوار ها و بازیکن و هدف
    for wall in walls:
        pygame.draw.rect(window, WallColor, wall.rect)

    pygame.draw.rect(window, PlayerColor, player.rect)
    pygame.draw.rect(window, EndColor, end_rect)

    #رنگ آمیزی هدف
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    EndColor = (R, G, B)

    pygame.display.update()