class Board:
    def __init__(self):
        self.grid = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
        ]

    def show(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if j == len(self.grid[0]) - 1:
                    print(self.grid[i][j], end="")
                else:
                    print(self.grid[i][j] + "|", end="")
            print()
            if i < len(self.grid) - 1:
                for j in range(5):
                    print("-", end="")
            print()
