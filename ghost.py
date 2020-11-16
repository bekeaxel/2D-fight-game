

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
        self.visible = True

    def move(self):
        if self.left:
            if self.x < 200:
                self.left = False 
                self.right = True
            self.x -= self.walk_vel
            self.hitbox_co = (self.x + 42, self.hitbox_co[1])

        if self.right:
            if self.x > 1440 - 200:
                self.right = False
                self.left = True
            self.x += self.walk_vel
            self.hitbox_co = (self.x + 42, self.hitbox_co[1])
        self.walk_count += 1

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
        if self.visible:
            if not self.is_dead:       
                self.face_player(player)
                self.move()
            if self.health <= 0:
                self.attack = False
                self.is_dead = True
