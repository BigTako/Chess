from Pieces_class import Piece

MAIN_MAP =  [["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"]]

map_copy = [["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"]]

phantom = Piece("ph")

Wr1, Wh1, Wb1  = Piece("Wr"), Piece("Wh"), Piece("Wb")
Wk, Wq = Piece("Wk"), Piece("Wq")
Wr2, Wh2, Wb2  = Piece("Wr"), Piece("Wh"), Piece("Wb")
Wp1 = Piece("Wp")
Wp2 = Piece("Wp")
Wp3 = Piece("Wp")
Wp4 = Piece("Wp")
Wp5 = Piece("Wp")
Wp6 = Piece("Wp")
Wp7 = Piece("Wp")
Wp8 = Piece("Wp")

Br1, Bh1, Bb1  = Piece("Br"), Piece("Bh"), Piece("Bb")
Bk, Bq = Piece("Bk"), Piece("Bq")
Br2, Bh2, Bb2  = Piece("Br"), Piece("Bh"), Piece("Bb")
Bp1 = Piece("Bp")
Bp2 = Piece("Bp")
Bp3 = Piece("Bp")
Bp4 = Piece("Bp")
Bp5 = Piece("Bp")
Bp6 = Piece("Bp")
Bp7 = Piece("Bp")
Bp8 = Piece("Bp")

blacks = [Br1, Bh1, Bb1, Bk, Bq, Bb2, Bh2, Br2, Bp1, Bp2, Bp3, Bp4, Bp5, Bp6, Bp7, Bp8]
whites = [Wr1, Wh1, Wb1, Wk, Wq, Wb2, Wh2, Wr2, Wp1, Wp2, Wp3, Wp4, Wp5, Wp6, Wp7, Wp8]
full = blacks + whites
kings = [Wk, Bk]

FIGURES_MAP =[[Br1, Bh1, Bb1, Bk, Bq, Bb2, Bh2, Br2],
              [Bp1, Bp2, Bp3, Bp4, Bp5, Bp6, Bp7, Bp8],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [Wp1, Wp2, Wp3, Wp4, Wp5, Wp6, Wp7, Wp8],
              [Wr1, Wh1, Wb1, Wk, Wq, Wb2, Wh2, Wr2]]

MARKED  =  [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]






