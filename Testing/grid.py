import pygame

# https://www.youtube.com/watch?v=sNVCSGOm_WU

def draw_grid(windows, size, row):
    
    distance = size // row
    x = 0
    y = 0
    
    for i in range(row):
        x = i * distance
        y = i * distance
        
        pygame.draw.line(windows, (0, 0, 0), (x, 0), (x, size)) 
        pygame.draw.line(windows, (0, 0, 0), (0, y), (size, y))
    

def redraw_grid(windows):
    
    global size, row
    windows.fill((255, 255, 255)) 
    
    draw_grid(windows, size, row)
    
    pygame.display.update()
    
    
    



def main():
    
    global size, row
    size = 500
    row = 20
    
    windows = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Grid Algorithm")
    
    play = True
    
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
        redraw_grid(windows)
        
if __name__ == "__main__":
    main()