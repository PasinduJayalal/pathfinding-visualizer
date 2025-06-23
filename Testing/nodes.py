import pygame

class GraphAlgoGUI:
    def __init__(self):
        pygame.init()
        self.size = 500
        self.row = 20
        self.mode = "wall"
        self.start_pos = None
        self.end_pos = None
        self.text_font = pygame.font.SysFont("Arial", 20, bold=True, italic=True)
        self.grid = [["empty" for _ in range(self.row)] for _ in range(self.row)]
        self.windows = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Graph Algorithm")
        
        play = True
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
            self.draw_grid()
            self.mouse_events()
            self.key_events()
            self.display("Hold 1 and left click for Start Node", self.text_font, (0, 0, 0), 10, 10)
            self.display("Hold 2 and left click for End Node", self.text_font, (0, 0, 0), 10, 20)
            self.display_mode()
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
                color = (255, 255, 255)
                if self.grid[row][col] == "wall":
                    color = (0, 0, 0) 
                elif self.grid[row][col] == "start":
                    color = (0, 255, 0)
                elif self.grid[row][col] == "end":
                    color = (255, 0, 0)
                pygame.draw.rect(self.windows, color, (col * self.cube, row * self.cube, self.cube, self.cube))
    
    # def mouse_events(self):
    #     mousebutton = pygame.mouse.get_pressed()
    #     pos = pygame.mouse.get_pos()
    #     col = pos[0] // self.cube
    #     row = pos[1] // self.cube
    #     # print(f"Row: {row}, Col: {col}")
    #     if row < self.row and col < self.row:
    #         if mousebutton[0]:
    #             if self.mode == "wall":
    #                 self.grid[row][col] = "wall"
    #             elif self.mode == "start":
    #                 self.grid[row][col] = "start"
    #             elif self.mode == "end":
    #                 self.grid[row][col] = "end"
    #         elif mousebutton[2]:
    #             self.grid[row][col] = "empty"
    
    
    def mouse_events(self):
        mousebutton = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        col = pos[0] // self.cube
        row = pos[1] // self.cube
        # print(f"Row: {row}, Col: {col}")
        if row < self.row and col < self.row:
            if mousebutton[0]:
                if self.mode == "wall":
                    self.grid[row][col] = "wall"
                elif self.mode == "start":
                    if self.start_pos:
                        old_row, old_col = self.start_pos
                        self.grid[old_row][old_col] = "empty"
                    self.grid[row][col] = "start"
                    self.start_pos = (row, col)
                    self.mode = "wall"  
                elif self.mode == "end":
                    if self.end_pos:
                        old_row, old_col = self.end_pos
                        self.grid[old_row][old_col] = "empty"
                    self.grid[row][col] = "end"
                    self.end_pos = (row, col)
                    self.mode = "wall"
            elif mousebutton[2]:
                self.grid[row][col] = "empty"
                if self.start_pos == (row, col):
                    self.start_pos = None
                if self.end_pos == (row, col):
                    self.end_pos = None
    
    # def key_events(self):
    #     keys = pygame.key.get_pressed()
    #     pos = pygame.mouse.get_pos()
    #     col = pos[0] // self.cube
    #     row = pos[1] // self.cube
    #     if keys[pygame.K_1]:
    #         print("Start node selected")
    #         if row < self.row and col < self.row:
    #             self.grid[row][col] = "start"
    #     if keys[pygame.K_2]:
    #         print("End node selected")
    #         if row < self.row and col < self.row:
    #             self.grid[row][col] = "end"
    
    def key_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.mode = "start"
        elif keys[pygame.K_2]:
           self.mode = "end"
        else:
            self.mode = "wall"
    
    def display(self, text, font, color, x, y):
        img = font.render(text, True, color)
        self.windows.blit(img, (x, y))
    
    def display_mode(self):
        mode = f"Mode: {self.mode.capitalize()}"
        colour = (0, 0, 0)
        mode_surface = self.text_font.render(mode, True, colour)
        self.windows.blit(mode_surface , (10, 30))
    
        
if __name__ == "__main__":
    GraphAlgoGUI()