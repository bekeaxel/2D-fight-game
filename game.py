import pygame, sys, random
pygame.init()
win_dim = (1440, 810)
win = pygame.display.set_mode(win_dim)

def flip_image(image):
    return pygame.transform.flip(image, True, False)

bg = pygame.image.load('game_background_1.png')

walk_right = [pygame.image.load('Knight/Walk/walk1.png'), pygame.image.load('Knight/Walk/walk2.png'), pygame.image.load('Knight/Walk/walk3.png'), pygame.image.load('Knight/Walk/walk4.png'), pygame.image.load('Knight/Walk/walk5.png'),pygame.image.load('Knight/Walk/walk6.png')]
walk_left = [flip_image(walk_right[0]), flip_image(walk_right[1]), flip_image(walk_right[2]), flip_image(walk_right[3]), flip_image(walk_right[4]), flip_image(walk_right[5])]
attack_right = [pygame.image.load('Knight/Attack/attack0.png'), pygame.image.load('Knight/Attack/attack1.png'), pygame.image.load('Knight/Attack/attack2.png'), pygame.image.load('Knight/Attack/attack3.png'), pygame.image.load('Knight/Attack/attack4.png')]
attack_left = [flip_image(attack_right[0]), flip_image(attack_right[1]), flip_image(attack_right[2]), flip_image(attack_right[3]), flip_image(attack_right[4])]
jump_right = [pygame.image.load('Knight/Jump/jump1.png'), pygame.image.load('Knight/Jump/jump2.png'), pygame.image.load('Knight/Jump/jump3.png'), pygame.image.load('Knight/Jump/jump4.png'), pygame.image.load('Knight/Jump/jump5.png'), pygame.image.load('Knight/Jump/jump6.png'), pygame.image.load('Knight/Jump/jump7.png')]
jump_left = [flip_image(jump_right[0]), flip_image(jump_right[1]), flip_image(jump_right[2]), flip_image(jump_right[3]), flip_image(jump_right[4]), flip_image(jump_right[5]), flip_image(jump_right[6]), ]

ghost1_walk_right = [pygame.image.load('Wraith_01/PNG Sequences/Walking/walking1.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking2.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking3.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking4.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking5.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking6.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking7.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking8.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking9.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking10.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking11.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking12.png')]
ghost1_walk_left = [flip_image(ghost1_walk_right[0]), flip_image(ghost1_walk_right[1]), flip_image(ghost1_walk_right[2]), flip_image(ghost1_walk_right[3]), flip_image(ghost1_walk_right[4]), flip_image(ghost1_walk_right[5]), flip_image(ghost1_walk_right[6]), flip_image(ghost1_walk_right[7]), flip_image(ghost1_walk_right[8]), flip_image(ghost1_walk_right[9]), flip_image(ghost1_walk_right[10]), flip_image(ghost1_walk_right[11])]
ghost1_dying_right = [pygame.image.load('Wraith_01/PNG Sequences/Dying/dying1.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying2.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying3.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying4.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying5.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying6.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying7.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying8.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying9.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying10.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying11.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying12.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying13.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying14.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying15.png')]
ghost1_dying_left = [flip_image(ghost1_dying_right[0]), flip_image(ghost1_dying_right[1]), flip_image(ghost1_dying_right[2]), flip_image(ghost1_dying_right[3]), flip_image(ghost1_dying_right[4]), flip_image(ghost1_dying_right[5]), flip_image(ghost1_dying_right[6]), flip_image(ghost1_dying_right[7]), flip_image(ghost1_dying_right[8]), flip_image(ghost1_dying_right[9]), flip_image(ghost1_dying_right[10]), flip_image(ghost1_dying_right[11]), flip_image(ghost1_dying_right[12]), flip_image(ghost1_dying_right[13]), flip_image(ghost1_dying_right[14])]
spell_projectile = [pygame.image.load('Wraith_01/Spell/spell1.png'), pygame.image.load('Wraith_01/Spell/spell2.png'), pygame.image.load('Wraith_01/Spell/spell3.png')]


class Player:
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.walk_count = 0
        self.jump_velocity = 9
        self.jump_count = 0
        self.left = False
        self.right = True
        self.is_jump = False
        self.is_standing = True 
        self.hitbox_co = (self.x + 25, self.y + 63)
        self.hitbox_dim = (39, 48)
        self.health = 100
        self.attacking = False
        self.attack_count = 0

    def jump(self):
        print(self.jump_count)
        if self.jump_velocity >= -9:
            self.jump_count += 1
            self.y -= 0.5 * (self.jump_velocity * abs(self.jump_velocity))
            self.hitbox_co = (self.hitbox_co[0], self.y + 63)
            self.jump_velocity -= 1
        else:
            self.is_jump = False
            self.jump_count = 0
            self.jump_velocity = 9

    def move(self):
        if self.is_jump:
            self.jump()
        if not self.is_standing:
            if self.left:
                if not self.x < -25:
                    self.x -= self.vel
                    self.hitbox_co = (self.x + 30, self.hitbox_co[1])
                    self.walk_count += 1
            elif self.right:
                if not self.x + self.width >= win_dim[0] - 34:
                    self.x += self.vel
                    self.hitbox_co = (self.x + 25, self.hitbox_co[1])
                    self.walk_count += 1
            
    def draw(self):
        #print("x: " + str(self.x) + ", y: " + str(self.y))
        if self.walk_count >= 18:
            self.walk_count = 0

        if self.attacking:
            if self.attack_count == 5:
                self.attack_count = 0
                self.attacking = False
            if self.right:
                win.blit(attack_right[self.attack_count], (self.x, self.y))
            elif self.left:
                win.blit(attack_left[self.attack_count], (self.x - 34, self.y))
            self.attack_count += 1
        elif self.is_jump:
            if self.right:
                win.blit(jump_right[self.jump_count // 3], (self.x, self.y))
            elif self.left:
                win.blit(jump_left[self.jump_count // 3], (self.x - 34, self.y))
        else:
            if not self.is_standing:   
                if self.left:
                    win.blit(walk_left[self.walk_count // 3], (self.x - 34, self.y))
                elif self.right:
                    win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
        
            else:
                if self.left:
                    win.blit(walk_left[0], (self.x - 34, self.y))
                if self.right:
                    win.blit(walk_right[0], (self.x, self.y))

   

    def reduce_health(self):
        pass       

    def hit(self):
        pass

class Ghost:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk_vel = 4
        self.left = True
        self.right = False
        self.walk_count = 0
        self.hitbox_co = (self.x + 42, self.y + 15)
        self.hitbox_dim = (44, 65)
        self.attack = False
        self.attack_count = 0
        self.health = 20
        self.is_dead = False
        self.dead_count = 0

    def move(self):
        if self.left:
            if self.x < 200:
                self.left = False 
                self.right = True
            self.x -= self.walk_vel
            self.hitbox_co = (self.x + 42, self.hitbox_co[1])

        if self.right:
            if self.x > win_dim[0] - 200:
                self.right = False
                self.left = True
            self.x += self.walk_vel
            self.hitbox_co = (self.x + 42, self.hitbox_co[1])
        self.walk_count += 1

    def draw(self):
        if self.is_dead:
            if self.right:
                win.blit(ghost1_dying_right[self.dead_count], (self.x, self.y))
            elif self.left:
                win.blit(ghost1_dying_left[self.dead_count], (self.x, self.y))
            self.dead_count += 1

        elif self.attack:
            if self.attack_count == 3:
                 pass
        else:    
            if self.walk_count >= 36:
                self.walk_count = 0
            if self.right:
                win.blit(ghost1_walk_right[self.walk_count // 3], (self.x, self.y))
            elif self.left:
                win.blit(ghost1_walk_left[self.walk_count // 3], (self.x, self.y))
        
        pygame.draw.rect(win, (255,0,0), (self.x + 5, self.y - 10, self.width - 5, 10))
        pygame.draw.rect(win, (0,128,0), (self.x + 5, self.y - 10, 50 - (5 * (10 - self.health)), 10))
        
    def face_player(self, player):
        if player.x - 120 > self.x:
            self.left = False
            self.right = True
        elif player.x < self.x - 150:
            self.left = True
            self.right = False
              
    def shoot(self):
        pass

    def update(self, player):
        if not self.is_dead:       
            self.face_player(player)
            self.move()
        if random.randint(1, 50) == 10:
            self.attack = True
        if self.health <= 0:
            self.attack = False
            self.is_dead = True

class Projectile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
       # self.width =    
    def move(self):
        pass



def draw_hitbox(char):
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0], char.hitbox_co[1]), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1]))
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0], char.hitbox_co[1]), (char.hitbox_co[0], char.hitbox_co[1] + char.hitbox_dim[1]))
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0], char.hitbox_co[1] + char.hitbox_dim[1]), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1] + char.hitbox_dim[1]))
        pygame.draw.line(win, (255,255,255), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1]), (char.hitbox_co[0] + char.hitbox_dim[0], char.hitbox_co[1] + char.hitbox_dim[1])) 

def redraw_screen():
    win.blit(bg, (0,-100))
    pygame.draw.rect(win, (28, 40, 36), (100, 600, win_dim[0] - 200, 50))
    player.draw()
    ghost.draw()
    draw_hitbox(player)
    draw_hitbox(ghost)
    pygame.display.update()

def quit():
    pass
#main loop
run = True
clock = pygame.time.Clock()
player = Player(400, 490, 129, 129)
ghost = Ghost(250, 520, 130, 105)
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

    ghost.update(player)
    player.move()

    
        

    redraw_screen()
    