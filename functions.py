import pygame.draw
import sys, os
from settings import bs, WHITE, YELLOW, GREEN, GRAY, LIGHT_BLUE, RED, menu_space, BLACK
from board import FIGURES_MAP, MAIN_MAP, MARKED, map_copy, Wk, Bk, full
import pygame
import tkinter as ttk

def apply_sprite(win, x, y, fig):
    """This function is responsible for displaying pieces sprites"""
    path = "sprites/" + fig + ".png"
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (img.get_width() // 1, img.get_height() // 1))
    img_rect = img.get_rect(center=(x + (bs // 2), y + (bs // 2)))
    win.blit(img, img_rect)

def main_show_cycle(w):
    """This function is responsible for drawing board cells a
    and contains sprites showing cycle."""
    cells = []
    color = None
    for i, row in enumerate(MAIN_MAP):
        for q, element in enumerate(row):
            x, y = transform_to_coords(i, q)
            if element == "W": # if cells have to be white
                color = WHITE
            elif element == "B": # if cells have to be black
                color = BLACK
            elif element == "G": # if cells have to be gray
                color = GRAY
            elif element == "R": # if cells have to be red
                color = RED
            elif element == "Y": # if cells have to be yellow
                color = YELLOW
            elif element == "S":
                color = LIGHT_BLUE

            cell = pygame.Rect(x, y, bs, bs)
            pygame.draw.rect(w, color, [cell.x, cell.y, cell.w, cell.h])
            cells.append(cell)

            if MARKED[i][q] == 1:
                r, c = transform_to_coords(i, q)
                r += menu_space // 4
                c += menu_space // 4
                pygame.draw.circle(w, GREEN, [r, c],10)

            if (figure := FIGURES_MAP[i][q]) != ".":
                apply_sprite(w, cell.x, cell.y, figure.name)
            else:
                continue
    return cells

def update():
    """Just returns board cells colors to origin view(black / white)"""
    for i, row in enumerate(map_copy):
        for j, element in enumerate(row):
            MAIN_MAP[i][j] = element
            MARKED[i][j] = 0

def define_rect(rects):
    """This function helps to define in which cell in field cursor is and return it's coordinates"""
    result = 0
    mouse_pos = pygame.mouse.get_pos() # where is mouse now
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
    for rect in rects:
        column, row = rect.x // bs - 1, rect.y // bs - 1
        if rect.colliderect(mouse_rect): # if mouse is on some rect
            result = [row, column] # append coordinates of this rect to list
    return result

def color_cell(color, cell):
    r, c = cell[0], cell[1]
    MAIN_MAP[r][c] = color

def define_figure(arr):
    """defines what figures is situated at these coords."""
    r, c = arr[0], arr[1]
    figure = FIGURES_MAP[r][c]
    return figure

def transform_to_coords(r, c):
    x = c*bs + menu_space // 2
    y = r*bs + menu_space // 2
    return (x, y)

def check_move(cell1, cell2): # optimal points cell , cell to move to
    """Checks if user moves in right way"""
    r, c = cell2[0], cell2[1]
    for l in cell1:
        if l[0] == r and l[1] == c:
            return True
    return False

def check_shah(through):
    """Checks if the king is under shah or not, if yes king can't
    move to shah сell, takes no arguments"""
    king_pos = [Wk.pos] + [Bk.pos]
    for p in full:
        if through:
            kills = p.find_kills(p.find_moves()[2])
        else:
            kills = p.find_kills(p.find_moves()[0])
        for k in kills:
            if k in king_pos :
                f = FIGURES_MAP[k[0]][k[1]]
                if f.name[0] != p.name[0]:
                    color_cell("Y", k)
                    return True, p.name[0]
    return False, 0

def check_itersection(a, b, all_moves):
    """ a - king moves, b - list of opponents figures"""
    alls = []
    at = set(tuple(i) for i in a)
    ac = list(at)
    try:
        for p in b:
            if p.name[1] == "p":
                r, c = p.pos[0], p.pos[1]
                points = []
                if p.name[0] == "B":
                    points = [[r + 1, c - 1], [r + 1, c + 1]]
                elif p.name[0] == "W":
                    points = [[r - 1, c - 1], [r - 1, c + 1]]
                if points[0] in a:
                    alls.append(points[0])
                if points[1] in a:
                    alls.append(points[1])
            else:
                p = p.find_moves()[1]
                pt = set(tuple(i) for i in p)
                d = list(at.intersection(pt))
                for i in d:
                    alls.append(i)
        if all_moves:
            alls = list(set(tuple(i) for i in alls))
            for pnt in alls:
                ac.remove(pnt)
            return ac
        else:
            return alls
    except Exception as e:
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

def popupmsg(msg):
    popup = ttk.Tk()
    NORM_FONT = ("Helvetica", 12)
    popup.wm_title("Congratulations!")
    popup.geometry("250x90")
    popup.geometry("+600+400")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    if msg == "Black wins!" or msg == "White wins!":
        quit()














