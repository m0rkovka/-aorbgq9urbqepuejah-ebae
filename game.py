from pygame import *

class GamePlayer(sprite.Sprite):
    def __init__(self, img, widht, height, x, y, step):
        super().__init__()
        self.image = transform.scale(image.load(img), (widht, height))
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.step = step

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class LeftPlayer(GamePlayer):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.step
        elif keys[K_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.step


window = display.set_mode((700, 500))
background = transform.scale(image.load('stol.png'), (700, 500))
fps = 60
clock = time.Clock()
game = True
player_1 = LeftPlayer('raketka.jpg', 40, 80, 40, 210, 10)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
window.blit(background, (0, 0))
player_1.update()
player_1.reset()
display.update()
clock.tick(fps)