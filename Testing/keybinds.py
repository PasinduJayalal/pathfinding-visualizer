import pygame
# https://www.youtube.com/watch?v=Hujzny-gkEk&t=619s
class Main:
    def __init__(self):
        pygame.init()
        self.size = 500
        self.row = 20
        self.windows = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Grid Algorithm")
        
        # running = False
        # sprinting = False
        
        play = True
        # while play:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             play = False
        #         # if event.type == pygame.KEYDOWN:
        #         #     print(f"Key Pressed: {pygame.key.name(event.key)}")
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_a:
        #                 # print("A key pressed")
        #                 running = True
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_LSHIFT:
        #                 # print("LSHIFT key pressed")
        #                 sprinting = True
                        
                        
                        
        #         if event.type == pygame.KEYUP:
        #             if event.key == pygame.K_a:
        #                 # print("A key released")
        #                 running = False
        #         if event.type == pygame.KEYUP:
        #             if event.key == pygame.K_LSHIFT:
        #                 # print("LSHIFT key released")
        #                 sprinting = False
                        
                        
                        
        #     if sprinting == True and running == True:
        #         print("Sprinting...")
        #     elif running == True:
        #         print("Running...")            
        #     pygame.display.update()
        while play:
            
            key = pygame.key.get_pressed()
            if key[pygame.K_a] == True and key[pygame.K_LSHIFT] == True:
                print("Sprinting...")
            elif key[pygame.K_a] == True:
                print("Running...")
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
            pygame.display.update()
            
        pygame.quit()
        

if __name__ == "__main__":
    Main()