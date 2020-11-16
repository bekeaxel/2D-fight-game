import pygame


def flip_image(image):
    return pygame.transform.flip(image, True, False)


class GhostGraphics:
    def __init__(self, ghost, win):
        self.ghost = ghost
        self.win = win
        self.walk_right = [pygame.image.load('Wraith_01/PNG Sequences/Walking/walking1.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking2.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking3.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking4.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking5.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking6.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking7.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking8.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking9.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking10.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking11.png'), pygame.image.load('Wraith_01/PNG Sequences/Walking/walking12.png')]
        self.walk_left = [flip_image(self.walk_right[0]), flip_image(self.walk_right[1]), flip_image(self.walk_right[2]), flip_image(self.walk_right[3]), flip_image(self.walk_right[4]), flip_image(self.walk_right[5]), flip_image(self.walk_right[6]), flip_image(self.walk_right[7]), flip_image(self.walk_right[8]), flip_image(self.walk_right[9]), flip_image(self.walk_right[10]), flip_image(self.walk_right[11])]
        self.dying_right = [pygame.image.load('Wraith_01/PNG Sequences/Dying/dying1.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying2.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying3.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying4.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying5.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying6.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying7.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying8.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying9.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying10.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying11.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying12.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying13.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying14.png'), pygame.image.load('Wraith_01/PNG Sequences/Dying/dying15.png')]
        self.dying_left = [flip_image(self.dying_right[0]), flip_image(self.dying_right[1]), flip_image(self.dying_right[2]), flip_image(self.dying_right[3]), flip_image(self.dying_right[4]), flip_image(self.dying_right[5]), flip_image(self.dying_right[6]), flip_image(self.dying_right[7]), flip_image(self.dying_right[8]), flip_image(self.dying_right[9]), flip_image(self.dying_right[10]), flip_image(self.dying_right[11]), flip_image(self.dying_right[12]), flip_image(self.dying_right[13]), flip_image(self.dying_right[14])]


    def draw(self):
        if self.ghost.visible:
            if self.ghost.is_dead:
                if self.ghost.right:
                    self.win.blit(self.dying_right[self.ghost.dead_count], (self.ghost.x, self.ghost.y))
                elif self.ghost.left:
                    self.win.blit(self.dying_left[self.ghost.dead_count], (self.ghost.x, self.ghost.y))
                self.ghost.dead_count += 1

            elif self.ghost.attack:
                if self.ghost.attack_count == 3:
                    pass
            else:    
                if self.ghost.walk_count >= 36:
                    self.ghost.walk_count = 0
                if self.ghost.right:
                    self.win.blit(self.walk_right[self.ghost.walk_count // 3], (self.ghost.x, self.ghost.y))
                elif self.ghost.left:
                    self.win.blit(self.walk_left[self.ghost.walk_count // 3], (self.ghost.x, self.ghost.y))
            
            pygame.draw.rect(self.win, (255,0,0), (self.ghost.x + 5, self.ghost.y - 10, self.ghost.width - 5, 10))
            pygame.draw.rect(self.win, (0,128,0), (self.ghost.x + 5, self.ghost.y - 10, 50 - (5 * (10 - self.ghost.health)), 10))



