import pygame
import buttons2
from algorithms import Algorithm

class Main:
    def __init__(self):
        pygame.init()
        self.grid_width = 500
        self.grid_height = 500
        self.panel_width = 200
        self.bottom_panel_height = 100
        
        self.mode = "wall"
        self.start_pos = None
        self.end_pos = None
        self.path = set()
        self.visited = set()
        
        self.row = 20
        self.grid = [["empty" for _ in range(self.row)] for _ in range(self.row)]
        self.text_font = pygame.font.SysFont("Arial", 30)
        self.text_font_bottompanel = pygame.font.SysFont("Arial", 20)
        
        self.size_total_width = self.grid_width + self.panel_width
        self.size_total_height = self.grid_height + self.bottom_panel_height
        self.windows = pygame.display.set_mode((self.size_total_width, self.size_total_height))
        
        self.dfs_img = pygame.image.load("dfs.png").convert_alpha()
        self.bfs_img = pygame.image.load("bfs.png").convert_alpha()
        self.dijkstras_img = pygame.image.load("dijkstras.png").convert_alpha()
        self.a_star_img = pygame.image.load("Astar.png").convert_alpha()
        self.clear_img = pygame.image.load("clear.png").convert_alpha()
        self.dfs_btn = buttons2.Button(self.grid_width + 25, 60, self.dfs_img,0.4)
        self.bfs_btn = buttons2.Button(self.grid_width + 25, 100, self.bfs_img,0.4)
        self.dijkstras_btn = buttons2.Button(self.grid_width + 25, 140, self.dijkstras_img,0.4)
        self.a_star_btn = buttons2.Button(self.grid_width + 25, 180, self.a_star_img,0.4)
        self.clear_btn = buttons2.Button(self.grid_width + 25, 280, self.clear_img,0.4)
        
        self.message = ""
        # self.start_img = pygame.image.load("start.png").convert_alpha()
        # self.end_img = pygame.image.load("end.png").convert_alpha()
        # self.start_btn = buttons2.Button(self.grid_width + 25, 60, self.start_img,0.4)
        # self.end_btn = buttons2.Button(self.grid_width + 25, 100, self.end_img,0.4)
        
        pygame.display.set_caption("GUI Demo")
        
        running = True
        while running:
            self.windows.fill((255, 255, 255))
            self.draw_side_panel()
            self.draw_bottom_panel()
            self.draw_grid()
            self.mouse_events()
            self.key_events()
            self.display_mode()
            if self.dfs_btn.draw(self.windows):
                # print("DFS button clicked")
                if self.start_pos and self.end_pos:
                    algo = Algorithm("DFS")
                    result = algo.dfs(self.grid, self.start_pos, self.end_pos, draw_function=lambda: self.redraw())
                    # print(result)
                    self.draw_path(result)
                else:
                    # print("Please set start and end nodes before running DFS.")
                    # self.display("Please set start and end nodes before running DFS.", self.text_font, (255, 0, 0), 10, self.grid_height + 80)
                    self.message = "Please set start and end nodes before running DFS."
            elif self.bfs_btn.draw(self.windows):
                # print("BFS button clicked")
                if self.start_pos and self.end_pos:
                    algo = Algorithm("BFS")
                    path,visited = algo.bfs(self.grid, self.start_pos, self.end_pos , lambda : self.redraw())
                    # print(result)
                    self.draw_visited(visited)
                    self.draw_path(path)
                else:
                    # print("Please set start and end nodes before running BFS.")
                    # self.display("Please set start and end nodes before running BFS.", self.text_font, (255, 0, 0), 10, self.grid_height + 80)
                    self.message = "Please set start and end nodes before running BFS."
            elif self.dijkstras_btn.draw(self.windows):
                # print("Dijkstras button clicked")
                if self.start_pos and self.end_pos:
                    algo = Algorithm("Dijkstra's")
                    path,visited = algo.dijkstra(self.grid, self.start_pos, self.end_pos, lambda : self.redraw())
                    # print(result)
                    self.draw_visited(visited)
                    self.draw_path(path)
                else:
                    # print("Please set start and end nodes before running Dijkstra's.")
                    # self.display("Please set start and end nodes before running Dijkstra's.", self.text_font, (255, 0, 0), 10, self.grid_height + 80)
                    self.message = "Please set start and end nodes before running Dijkstra's."
            elif self.a_star_btn.draw(self.windows):
                # print("A* button clicked")
                if self.start_pos and self.end_pos:
                    algo = Algorithm("A*")
                    path,visited = algo.a_star(self.grid, self.start_pos, self.end_pos, lambda : self.redraw())
                    # print(result)
                    self.draw_visited(visited)
                    self.draw_path(path)
                else:
                    # print("Please set start and end nodes before running A*.")
                    # self.display("Please set start and end nodes before running A*.", self.text_font, (255, 0, 0), 10, self.grid_height + 80)
                    self.message = "Please set start and end nodes before running A*."
                    
            elif self.clear_btn.draw(self.windows):
                # print("Clear button clicked")
                self.grid = [["empty" for _ in range(self.row)] for _ in range(self.row)]
                self.start_pos = None
                self.end_pos = None
                self.path = None
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()
    
    def draw_grid(self):
        self.cube = self.grid_width // self.row
        self.draw_walls()
        for i in range(self.row):
            x = i * self.cube
            y = i * self.cube
            pygame.draw.line(self.windows, (0, 0, 0), (x, 0), (x, self.grid_width))
            pygame.draw.line(self.windows, (0, 0, 0), (0, y), (self.grid_width, y))
    
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
                elif self.grid[row][col] == "path":
                    color = (0, 0, 255)
                elif self.grid[row][col] == "visited":
                    color = (255, 255, 0)
                pygame.draw.rect(self.windows, color, (col * self.cube, row * self.cube, self.cube, self.cube))
                
    def draw_path(self, path):
        # if self.path:
        #     for pos in self.path:
        #         row, col = pos
        #         if self.grid[row][col] == "path":
        #             self.grid[row][col] = "empty"
        self.path = path
        for pos in self.path:
            row, col = pos
            if (row, col) != self.start_pos and (row, col) != self.end_pos:
                self.grid[row][col] = "path"  
                # self.draw_grid()
                # pygame.display.update()
                #pygame.draw.rect(self.windows, (0, 0, 255), (col * self.cube, row * self.cube, self.cube, self.cube))
                self.redraw()
                
    def draw_visited(self, visited):
        # if self.visited:
        #     for pos in self.visited:
        #         row, col = pos
        #         if self.grid[row][col] == "visited":
        #             self.grid[row][col] = "empty"
        self.visited = visited
        for pos in visited:
            row, col = pos
            if (row, col) != self.start_pos and (row, col) != self.end_pos:
                self.grid[row][col] = "visited"
                # self.draw_grid()
                # pygame.display.update()
                self.redraw()
                
    def redraw(self):
        self.draw_grid()
        pygame.display.update()
        pygame.time.delay(5)
                
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
                    
    def key_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.mode = "start"
        elif keys[pygame.K_2]:
           self.mode = "end"
        else:
            self.mode = "wall"
    
    def draw_side_panel(self):
        panel_rect = pygame.Rect(self.grid_width, 0, self.panel_width, self.grid_height)
        pygame.draw.rect(self.windows, (200, 200, 200), panel_rect)
        self.display("Algorithms", self.text_font, (0, 0, 0), self.grid_width + 40, 10)
        
    def draw_bottom_panel(self):
        bottom_panel_rect = pygame.Rect(0, self.grid_height, self.size_total_width, self.bottom_panel_height)
        pygame.draw.rect(self.windows, (200, 200, 200), bottom_panel_rect)
        self.display("Hold 1 and left click for Start Node", self.text_font_bottompanel, (0, 0, 0), 10, self.grid_height + 40)
        self.display("Hold 2 and left click for End Node", self.text_font_bottompanel, (0, 0, 0), 10, self.grid_height + 60)
        
        if self.message:
            self.display(self.message, self.text_font_bottompanel, (255, 0, 0), 280, self.grid_height + 10)
    
    def display(self, text, font, color,x,y):
        img = font.render(text, True, color)
        self.windows.blit(img, (x, y))
        
    def display_mode(self):
        mode = f"Mode: {self.mode.capitalize()}"
        colour = (0, 0, 0)
        mode_surface = self.text_font_bottompanel.render(mode, True, colour)
        self.windows.blit(mode_surface , (10, self.grid_height + 10))

if __name__ == "__main__":
    Main()
    