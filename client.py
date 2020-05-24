import pygame
from network import Network
from player import Player

width = 800
height = 608
win = pygame.display.set_mode((width, height))
win.fill((255, 255, 255))
pygame.display.set_caption("PTC")


def redrawWindow(win, player, player2):
    try:
        player.draw(win)
        player2.draw(win)
    except AttributeError:
        pass
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(15)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move(p2)
        redrawWindow(win, p, p2)


main()
