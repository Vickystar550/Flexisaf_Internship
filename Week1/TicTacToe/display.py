class Board:
    def __init__(self):
        self.placeholder_00 = "?"
        self.placeholder_01 = "?"
        self.placeholder_02 = "?"
        self.placeholder_10 = "?"
        self.placeholder_11 = "?"
        self.placeholder_12 = "?"
        self.placeholder_20 = "?"
        self.placeholder_21 = "?"
        self.placeholder_22 = "?"

        self.game_map = {
                (0, 0): self.placeholder_00,
                (0, 1): self.placeholder_01,
                (0, 2): self.placeholder_02,
                (1, 0): self.placeholder_10,
                (1, 1): self.placeholder_11,
                (1, 2): self.placeholder_12,
                (2, 0): self.placeholder_20,
                (2, 1): self.placeholder_21,
                (2, 2): self.placeholder_22
            }

        self.board = f"""
        \t\t\t\t ---------------
        \t\t\t\t| {self.placeholder_00}  |  {self.placeholder_01}  |  {self.placeholder_02} |
        \t\t\t\t|----|-----|----|
        \t\t\t\t| {self.placeholder_10}  |  {self.placeholder_11}  |  {self.placeholder_12} |
        \t\t\t\t|----|-----|----|
        \t\t\t\t| {self.placeholder_20}  |  {self.placeholder_21}  |  {self.placeholder_22} |
        \t\t\t\t ---------------
        """

        self.hint_board = f"""
        (1)  |  (2)  |  (3)
             |       |
        (4)  |  (5)  |  (6)
             |       |
        (7)  |  (8)  |  (9)
        """