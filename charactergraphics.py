import pygame

def flip_image(image):
    return pygame.transform.flip(image, True, False)

class CharacterGraphics:
    
    def __init__(self, player, win):
        self.player = player
        self.win = win
        self.walk_right = [pygame.image.load('Knight/Walk/walk1.png'), pygame.image.load('Knight/Walk/walk2.png'), pygame.image.load('Knight/Walk/walk3.png'), pygame.image.load('Knight/Walk/walk4.png'), pygame.image.load('Knight/Walk/walk5.png'),pygame.image.load('Knight/Walk/walk6.png')]
        self.walk_left = [flip_image(self.walk_right[0]), flip_image(self.walk_right[1]), flip_image(self.walk_right[2]), flip_image(self.walk_right[3]), flip_image(self.walk_right[4]), flip_image(self.walk_right[5])]
        self.attack_right = [pygame.image.load('Knight/Attack/attack0.png'), pygame.image.load('Knight/Attack/attack1.png'), pygame.image.load('Knight/Attack/attack2.png'), pygame.image.load('Knight/Attack/attack3.png'), pygame.image.load('Knight/Attack/attack4.png')]
        self.attack_left = [flip_image(self.attack_right[0]), flip_image(self.attack_right[1]), flip_image(self.attack_right[2]), flip_image(self.attack_right[3]), flip_image(self.attack_right[4])]
        self.jump_right = [pygame.image.load('Knight/Jump/jump1.png'), pygame.image.load('Knight/Jump/jump2.png'), pygame.image.load('Knight/Jump/jump3.png'), pygame.image.load('Knight/Jump/jump4.png'), pygame.image.load('Knight/Jump/jump5.png'), pygame.image.load('Knight/Jump/jump6.png'), pygame.image.load('Knight/Jump/jump7.png')]
        self.jump_left = [flip_image(self.jump_right[0]), flip_image(self.jump_right[1]), flip_image(self.jump_right[2]), flip_image(self.jump_right[3]), flip_image(self.jump_right[4]), flip_image(self.jump_right[5]), flip_image(self.jump_right[6]), ]
    
    def draw(self):
        if self.player.visible:
            
            if self.player.attacking:
                if self.player.attack_count == 5:
                    self.player.attack_count = 0
                    self.player.attacking = False
                if self.player.right: 
                    self.win.blit(self.attack_right[self.player.attack_count], (self.player.x, self.player.y))
                elif self.player.left:
                    self.win.blit(self.attack_left[self.player.attack_count], (self.player.x - 34, self.player.y))
                self.player.attack_count += 1

            elif self.player.is_jump:
                if self.player.right:
                    self.win.blit(self.jump_right[self.player.jump_count // 3], (self.player.x, self.player.y))
                elif self.player.left:
                    self.win.blit(self.jump_left[self.player.jump_count // 3], (self.player.x - 34, self.player.y))
            else:
                if not self.player.is_standing:   
                    if self.player.left:
                        self.win.blit(self.walk_left[self.player.walk_count // 3], (self.player.x - 34, self.player.y))
                    elif self.player.right:
                        self.win.blit(self.walk_right[self.player.walk_count // 3], (self.player.x, self.player.y))
            
                else:
                    if self.player.left:
                        self.win.blit(self.walk_left[0], (self.player.x - 34, self.player.y))
                    if self.player.right:
                        self.win.blit(self.walk_right[0], (self.player.x, self.player.y))