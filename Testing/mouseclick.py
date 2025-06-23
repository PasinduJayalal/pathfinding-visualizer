import pygame

# https://www.youtube.com/watch?v=YbouZ2X8fGk
def main():
    size = 500
    
    windows = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Grid Algorithm")
    
    play = True

    while play:
        
        # print(pygame.mouse.get_pressed())
        # if pygame.mouse.get_pressed()[0] == True:
        #     print("Left Mouse Down")
        # if pygame.mouse.get_pressed()[2] == True:
        #     print("Right Mouse Down")
        pos = pygame.mouse.get_pos()
        print(pos)
        # col = pos[0] // 25
        # row = pos[1] // 25
        # print(f"Row: {row}, Col: {col}")
        
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print(event)
            # if event.type == pygame.MOUSEBUTTONUP:
            #     print("Mouse Up")
            if event.type == pygame.QUIT:
                play = False
                
    pygame.quit()
    
    
if __name__ == "__main__":
    main()