#https://www.youtube.com/watch?v=ndtFoWWBAoE
import pygame
class Font:
    def __init__(self):
        pygame.font.init()
        self.size = 500
        self.row = 20
        self.text_font = pygame.font.SysFont("Arial", 36, bold=True, italic=True)
        self.windows = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Font Display")
        running = True
        while running:
            self.windows.fill((255, 255, 255))
            self.display("Hello World", self.text_font, (0, 0, 0), 50, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            pygame.display.update()
        pygame.quit()
       
    def display(self, text, font, color,x,y):
        img = font.render(text, True, color)
        self.windows.blit(img, (x, y))


if __name__ == "__main__":
    font = Font()