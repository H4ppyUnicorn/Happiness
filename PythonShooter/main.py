from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((700,500))

display.set_caption("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
background = transform.scale(image.load('galaxy.jpg'), (700,500))
hero = transform.scale(image.load('rocket.png'), (100,100))
enemy = transform.scale(image.load('ufo.png'), (100,100))