


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
        self.health = 50
        self.attacking = False
        self.attack_count = 0
        self.visible = True

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
        if self.walk_count >= 17:
            self.walk_count = 0
        if self.is_jump:
            self.jump()
        if not self.is_standing:
            if self.left:
                if not self.x < -25:
                    self.x -= self.vel
                    self.hitbox_co = (self.x + 30, self.hitbox_co[1])
                    self.walk_count += 1
            elif self.right:
                if not self.x + self.width >= 1440 - 34:
                    self.x += self.vel
                    self.hitbox_co = (self.x + 25, self.hitbox_co[1])
                    self.walk_count += 1
            

    def reduce_health(self):
        self.health -= 1   

    def hit(self):
        pass
