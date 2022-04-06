from pygame import *
from random import randint
mixer.init()
fire = mixer.Sound('Splat.ogg')
 
font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 36)
win = font1.render('You Win!', True, (255, 255, 255))
lose = font1.render('You Lose!', True, (180, 0, 0))

lost = 0
score = 0
hp = 3

img_back = 'galaxy.jpg'
img_hero = 'gun.png'
img_bullet = 'sweat.png'
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x<win_width-80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 50, 50, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width-80)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 700
win_height = 500
display.set_caption('Among us drip')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
player = Player(img_hero, 250, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(5):
   monster = Enemy("Evil.png", randint(80, win_width-80), -40, 80, 70, randint(1, 5))
   monsters.add(monster)
bullets = sprite.Group()

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                player.fire()

    if not finish:
        window.blit(background, (0,0))

        text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        text_win = font2.render("Счёт: " + str(score), 1, (255, 255, 255))
        window.blit(text_win, (10, 10))

        text_hp = font1.render("Здоровье: ", 1, (255, 255, 255))
        window.blit(text_hp, (10, 90))
        
        healthpoints = font1.render(str(hp), 1, (255, 0, 0))
        window.blit(healthpoints, (150, 90))

        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for c in sprites_list:
            score += 1
            monster = Enemy("Evil.png", randint(80, win_width-80), -40, 80, 70, randint(1, 5))
            monsters.add(monster)

        sus_list = sprite.spritecollide(player, monsters, True)
        for c in sus_list:
            if hp > 1:
                hp -= 1
                monster = Enemy("Evil.png", randint(80, win_width-80), -40, 80, 70, randint(1, 5))
                monsters.add(monster)
            else:
                finish = True
                window.blit(lose, (300, 220)) 

        if lost >= 3:
            finish = True
            window.blit(lose, (300, 220))

        if score >= 100:
            finish = True
            window.blit(win, (300, 220))

        player.reset()
        player.update()
    
        monsters.draw(window)
        monsters.update()

        bullets.draw(window)
        bullets.update()

        display.update()
    time.delay(50)