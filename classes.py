from board import FIGURES_MAP, full
import functions

class Player:
    def __init__(self, color , pieces, access):
        self.color = color
        self.killed = []
        self.access = access
        self.pieces = pieces

    def select(self, cell):
        if self.access:
            functions.color_cell("G", cell)

    def kill(self, f):
        r, c = f[0], f[1]
        figure = FIGURES_MAP[r][c]
        FIGURES_MAP[r][c] = "."
        self.killed.append(figure)
        full.remove(figure)

    def move(self, figure, cell2, opp):
            rf, cf = figure.pos[0], figure.pos[1]
            rt, ct = cell2[0], cell2[1]

            if rf != rt or cf != ct:
                if FIGURES_MAP[rt][ct] != ".":
                    self.kill(cell2)
                if rf != rt or cf != ct:
                    if FIGURES_MAP[rt][ct] != ".":
                        self.kill(cell2)
                    if (figure.name == "Wp" and rt == 0) or (figure.name == "Bp" and rt == 7):
                        figure.becomeQeen(rt, ct)
                    else:
                        FIGURES_MAP[rt][ct], FIGURES_MAP[rf][cf] = FIGURES_MAP[rf][cf], "."
                    self.access = False
                    opp.access = True
                    figure.counter += 1
                functions.update()












