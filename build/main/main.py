import pygame
import sys, os
from settings import dh, dw
from classes import Player
import functions
import board

pygame.init()
win = pygame.display.set_mode((dw, dh))
pygame.display.set_caption('Chess')
icon = pygame.image.load('sprites/Bh.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

p1 = Player("W", board.whites, True)
p2 = Player("B", board.blacks, False)
players = [p1, p2]

running = True
while running:
    clock.tick(30)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            quit()

    rl = functions.main_show_cycle(win)
    l_clicked = pygame.mouse.get_pressed(num_buttons=3)[0]
    r_clicked = pygame.mouse.get_pressed(num_buttons=3)[2]

    for r, row in enumerate(board.FIGURES_MAP):
        for c, element in enumerate(row):
            if element != ".":
                element.pos = [r, c]

    tutorial = pygame.font.Font(None, 36)
    text = tutorial.render("Right MB --> select; Left MB --> put;", True, (255, 255, 255))
    win.blit(text, (120, 20))
    try:
        global figure, move_points, victims
        if r_clicked:
            functions.update() # return map to primal state
            d = functions.define_rect(rl) # determine which cell to select
            figure = functions.define_figure(d) # figures is standing on that cell
            if figure.name == "Wk":
                # king = "Wk"
                km = board.Wk.find_moves()[0]
                move_points = functions.check_itersection(km, board.blacks, True)  # check an opportunity of potential shah
            elif figure.name == "Bk":
                king = "Bk"
                km = board.Bk.find_moves()[0]
                move_points = functions.check_itersection(km, board.whites, True)  # check an opportunity of potential shah
            else:
                move_points = figure.find_moves()[0] # list of points to move to
        # functions.potential_shah(figure)
            victims = figure.find_kills(move_points) # pieces available to kill
            player = None
            if p1.access and figure.name[0] == "W":
                player = p1
            elif p2.access and figure.name[0] == "B":
                player = p2

            player.select(d)
            for p in move_points:
                if (board.FIGURES_MAP[p[0]][p[1]] == "."):
                    board.MARKED[p[0]][p[1]] = 1  # if move field is empty
            for v in victims:
                vk = board.FIGURES_MAP[v[0]][v[1]]
                board.MAIN_MAP[v[0]][v[1]] = "R"
                # figures available to kill

        elif l_clicked:
            d = functions.define_rect(rl)
            av = functions.check_move(move_points, d)  # check if player moves to optimal cell
            player = None
            if p1.access and figure.name[0] == "W":
                player = p1
            elif p2.access and figure.name[0] == "B":
                player = p2
            inx = players.index(player)
            if av or len(victims) > 0:
                player.move(figure, d, players[inx - 1])
                functions.update()
            else:
                print("You can't move there!")

        shah = functions.check_shah(False)[1]
        bkm = board.Bk.find_moves()[0]
        wkm = board.Wk.find_moves()[0]
        wking_moves = functions.check_itersection(wkm, board.blacks, True)
        bking_moves = functions.check_itersection(bkm, board.whites, True)
        if shah == "B" and len(wking_moves) == 0:  # who set the shah
            functions.popupmsg("Black wins!")
        if shah == "W" and len(bking_moves) == 0:
            functions.popupmsg("White wins!")
    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    pygame.display.update()
    win.fill((0, 0, 0))

