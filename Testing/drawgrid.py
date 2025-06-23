import pygame


class GridGUI:
    def __init__(self):
        pygame.init()
        self.size = 500
        self.row = 20
        self.grid = [["empty" for _ in range(self.row)] for _ in range(self.row)]
        self.windows = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Grid Algorithm")
        
        play = True
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
            self.draw_grid()
            self.mouse_events()
            pygame.display.update()
        pygame.quit()
    
    def draw_grid(self):
        self.windows.fill((255, 255, 255))
        self.cube = self.size // self.row
        self.draw_walls()
        for i in range(self.row):
            x = i * self.cube
            y = i * self.cube
            pygame.draw.line(self.windows, (0, 0, 0), (x, 0), (x, self.size))
            pygame.draw.line(self.windows, (0, 0, 0), (0, y), (self.size, y))
        
    def draw_walls(self):
        for row in range(self.row):
            for col in range(self.row):
                if self.grid[row][col] == "wall":
                    pygame.draw.rect(self.windows, (0, 0, 0), (col * self.cube, row * self.cube, self.cube, self.cube))

    
    def mouse_events(self):
        mousebutton = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        col = pos[0] // self.cube
        row = pos[1] // self.cube
        # print(f"Row: {row}, Col: {col}")
        if row < self.row and col < self.row:
            if mousebutton[0]:
                self.grid[row][col] = "wall"
            elif mousebutton[2]:
                self.grid[row][col] = "empty"
        
        

if __name__ == "__main__":
    GridGUI()