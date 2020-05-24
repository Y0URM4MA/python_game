import pygame


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.p_rect = None
        self.speed = 16
        self.rect_arr = [self.rect]

    def draw(self, win):
        try:
            pygame.draw.rect(win, self.color, self.p_rect)
        except:
            pass
        pygame.draw.rect(win, (0, 0, 0), self.rect)

    def move(self, player):
        keys = pygame.key.get_pressed()

        def movement_rect(playerr, x, y):
            try:
                boolean = True
                for rect in playerr.rect_arr:
                    if rect[0] == x and rect[1] == y:
                        boolean = False
                return boolean
            except AttributeError:
                print("Error movement")
                return False

        if keys[pygame.K_LEFT]:
            self.p_rect = self.rect
            self.x = (self.x - self.speed) if self.x > 0 and movement_rect(player, self.x - self.speed,
                                                                           self.y) else self.x

        elif keys[pygame.K_RIGHT]:
            self.p_rect = self.rect
            self.x = (self.x + self.speed) if self.x < 786 and movement_rect(player, self.x + self.speed,
                                                                             self.y) else self.x

        elif keys[pygame.K_UP]:
            self.p_rect = self.rect
            self.y = (self.y - self.speed) if self.y > 0 and movement_rect(player, self.x,
                                                                           self.y - self.speed) else self.y

        elif keys[pygame.K_DOWN]:
            self.p_rect = self.rect
            self.y = (self.y + self.speed) if self.y < 592 and movement_rect(player, self.x,
                                                                             self.y + self.speed) else self.y

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        boolean = True
        for r in self.rect_arr:
            if self.rect[0] == r[0] and self.rect[1] == r[1]:
                boolean = False
        if boolean:
            self.rect_arr.append(self.rect)

