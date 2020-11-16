import pygame
import sys
import random
from charactergraphics import CharacterGraphics
from ghostgraphics import GhostGraphics
from ghost import Ghost
from player import Player

pygame.init()
win_dim = (1440, 810)
win = pygame.display.set_mode(win_dim)

def flip_image(image):
    return pygame.transform.flip(image, True, False)

bg = pygame.image.load('game_background_1.png')

profile_pic = pygame.image.load('Knight/knightpic.png')





spell_projectile = [pygame.image.load('Wraith_01/Spell/spell1.png'), pygame.image.load('Wraith_01/Spell/spell2.png'), pygame.image.load('Wraith_01/Spell/spell3.png')]



def draw_hitbox(char):
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0], char.hitbox_co[1]), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1]))
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0], char.hitbox_co[1]), (char.hitbox_co[0], char.hitbox_co[1] + char.hitbox_dim[1]))
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0], char.hitbox_co[1] + char.hitbox_dim[1]), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1] + char.hitbox_dim[1]))
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1]), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1] + char.hitbox_dim[1])) 

def redraw_screen():
    win.blit(bg, (0,-100))
    pygame.draw.rect(win, (28, 40, 36), (100, 600, win_dim[0] - 200, 50))
    player_graphics.draw()
    ghost_graphics.draw()
    draw_hitbox(player)
    draw_hitbox(ghost)
    draw_player_health()
    pygame.display.update()

def draw_player_health():
    health_label = font.render('HEALTH', 1, (128,124,108))
    pygame.draw.circle(win, (144,103,49), (80, 80), 40)
    pygame.draw.circle(win, (156,149,140), (80, 80), 37)
    win.blit(profile_pic, (62,60))
    pygame.draw.rect(win, (255,0,0), (140, 80, 200, 10))
    pygame.draw.rect(win, (0,128,0), (140, 80, 200 - (5 * (50 - player.health)), 10))
    win.blit(health_label, (140, 60))


def quit():
    pass
#main loop
run = True
clock = pygame.time.Clock()
player = Player(400, 490, 129, 129)
ghost = Ghost(250, 520, 130, 105)
player_graphics = CharacterGraphics(player, win)
ghost_graphics = GhostGraphics(ghost, win)
projectiles = []
font = pygame.font.SysFont('Comic Sans Ms', 15)


while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ghost.health -= 1
        player.health -= 1
        player.is_jump = True
    if keys[pygame.K_SPACE]:
        player.attacking = True
    elif keys[pygame.K_RIGHT]:
        player.left = False
        player.right = True
        player.is_standing = False
    elif keys[pygame.K_LEFT]:
        player.left = True
        player.right = False
        player.is_standing = False
    else:
        player.is_standing = True
        player.walk_count = 0

    if player.hitbox_co[1] < ghost.hitbox_co[1] + ghost.hitbox_dim[1] and player.hitbox_co[1] + player.hitbox_dim[1] > ghost.hitbox_co[1]:
            if player.hitbox_co[0] + player.hitbox_dim[0] > ghost.hitbox_co[0] and player.hitbox_co[0] < ghost.hitbox_co[0] + ghost.hitbox_dim[0]:
                player.reduce_health()

    for p in projectiles:
        p.move()

    ghost.update(player)
    if ghost.dead_count == 14:
        ghost.visible = False
    player.move()

    
        

    redraw_screen()
    