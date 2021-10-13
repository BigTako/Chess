import board

class Piece:
    def __init__(self, name):
        self.name = name
        self.pos = []
        self.counter = 1
        self.move_access = True

    def check(self, r, c, cells, dir, dir_name, fname ,a):
        moves = [(r - 1, c - 1), (r, c - 1), (r + 1, c - 1), # kings moves
                 (r + 1, c), (r + 1, c + 1), (r, c + 1),
                 (r - 1, c + 1), (r - 1, c)]
        b_steps, r_steps = [(-1, -1), (-1, 1), (1, -1), (1, 1)],[(-1, 0), (1, 0), (0, -1), (0, 1)]
        b_names, r_names = ["ur", "ul", "dr", "dl"], ["up", "down", "left", "right"]
        # bishops directions names, rooks directions names
        if fname == "b" or fname == "r":
            s1, s2 = 0, 0
            if fname == "b":
                for i in range(4):
                    if dir_name == b_names[i]:
                        s1, s2 = b_steps[i][0], b_steps[i][1]
            if fname == "r":
                for i in range(4):
                    if dir_name == r_names[i]:
                        s1, s2 = r_steps[i][0], r_steps[i][1]
            r1, c1 = r, c
            for i in range(dir):
                r += s1
                c += s2
                f = define_figure([r, c])
                if f != ".":
                    if f.name[0] == self.name[0]: # if pieces the same colored
                        break
                    else:
                        cells.append([r, c])
                        break
                else:
                    cells.append([r, c])

            r, c = r1, c1
            for e in range(dir):
                r += s1
                c += s2
                f = define_figure([r, c])
                if f != ".":
                    if f.name[1] == "k" and f.name[0] != self.name[0]:
                        continue
                    else:
                        a.append([r, c])
                        break
                else:
                    a.append([r, c])

        elif fname == "q" or fname == "k":
            for r, c in moves:
                if (7 >= r >= 0) and (7 >= c >= 0):
                    f = define_figure([r, c])
                    a.append([r, c])
                    if f != ".":
                        if f.name[0] == self.name[0]:
                            continue
                    else:
                        cells.append([r, c])
                    cells.append([r, c])
                else:
                    continue
    def find_moves(self):  # available cells to figure to move to
        r, c = self.pos[0], self.pos[1]
        cells = []
        all_cells = []
        if self.name[1] == 'p':  # find moves for pawm figure
            if self.name[0] == "W":
                q = [r - 1, c]
                if define_figure(q) == ".":
                    cells.append(q)
                    all_cells.append(q)
                    if self.counter == 1:
                        if define_figure(q) == ".":
                            q = [r - 2, c]
                            cells.append(q)
                            all_cells.append(q)
            elif self.name[0] == "B":
                q = [r + 1, c]
                if define_figure(q) == ".":
                    cells.append(q)
                    all_cells.append(q)
                    if self.counter == 1:
                        q = [r + 2, c]
                        if define_figure(q) == ".":
                            cells.append(q)
                            all_cells.append(q)
        elif self.name[1] == "h":  # horses
            points = [[r - 2, c + 1], [r - 2, c - 1],  # upper points
                      [r - 1, c - 2], [r - 1, c + 2],
                      [r + 1, c - 2], [r + 2, c - 1],
                      [r + 2, c + 1], [r + 1, c + 2]]  # down points
            for i in points:
                if (7 >= i[0] >= 0) and (7 >= i[1] >= 0):
                    all_cells.append(i)
                    f = board.FIGURES_MAP[i[0]][i[1]]
                    if f == "." or f.name[0] != self.name[0]:
                        cells.append(i)
                else:
                    continue

        if self.name[1] == "b":  # bishops
            ur, dl, dr, ul = min(r, c), (7 - max(r, c)), min((7 - r), c), min((7 - c), r)  # upright
            dirs, names = [ur, dl, dr, ul], ["ur", "dl", "dr", "ul"]
            for i in range(4):
                self.check(r, c, cells, dirs[i], names[i], "b", all_cells)
                r, c = self.pos[0], self.pos[1]

        if self.name[1] == "r": # rooks
            up, down, left, right = r, 7 - r, c, (7 - c)  # movement directions
            dirs, names = [up, down, left, right], ["up", "down", "left", "right"]
            for i in range(4):
                self.check(r, c, cells, dirs[i], names[i], "r", all_cells)
                r, c = self.pos[0], self.pos[1]

        if self.name[1] == "k": # kings
            self.check(r, c, cells, 0, 0, "k", all_cells)

        if self.name[1] == "q": # queens
            ur, dl, dr, ul = min(r, c), (7 - max(r, c)), min((7 - r), c), min((7 - c), r)
            up, down, left, right = r, 7 - r, c, (7 - c)
            self.check(r, c, cells, 0, 0, "k", all_cells)
            names_b, names_r = ["ur", "dl", "dr", "ul"], ["up", "down", "left", "right"]
            dirs_b, dirs_r = [ur, dl, dr, ul], [up, down, left, right]
            for i in range(4):
                self.check(r, c, cells, dirs_r[i], names_r[i], "r", all_cells)
                self.check(r, c, cells, dirs_b[i], names_b[i], "b", all_cells)
                r, c = self.pos[0], self.pos[1]
        return cells, all_cells

    def find_kills(self, opt):
        global f1, f2
        cells = []
        if self.name[1] == "p":
            moves = []
            pos = self.pos
            r, c = pos[0], pos[1]
            if self.name[0] == "W":
                moves = [[r - 1, c - 1], [r - 1, c + 1]]
            if self.name[0] == "B":
                moves = [[r + 1, c - 1], [r + 1, c + 1]]

            for i in moves:
                if 7 >= i[0] >= 0 and 7 >= i[1] >= 0:
                    if board.FIGURES_MAP[i[0]][i[1]] != ".":
                        fc = board.FIGURES_MAP[i[0]][i[1]].name[0]
                        if fc != self.name[0]:
                            cells.append(i)
        else:
            for point in opt:
                try:
                    r, c = point[0], point[1]
                    f = board.FIGURES_MAP[r][c]
                    if f != "." and f.name[0] != self.name[0]:
                        cells.append(point)
                except Exception:
                    continue
        return cells

    def becomeQeen(self, r, c):
        rf, cf = self.pos[0], self.pos[1]
        l, name = 0, 0
        if self.name[0] == "B":
            l, name = board.blacks, "Bq"
        elif self.name[0] == "W":
            l, name = board.whites, "Wq"
        board.FIGURES_MAP[rf][cf] = board.FIGURES_MAP[r][c] = "."
        l.remove(self)
        board.full.remove(self)
        newQueen = Piece(name)
        l.append(newQueen)
        board.full.append(newQueen)
        board.FIGURES_MAP[r][c] = newQueen

def define_figure(arr):  # defines what figures is situated at these coords.
    r, c = arr[0], arr[1]
    figure = board.FIGURES_MAP[r][c]
    return figure


