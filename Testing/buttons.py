#https://www.youtube.com/watch?v=G8MYGDf_9ho
import pygame
import buttons2

pygame.init()
size = 500
windows = pygame.display.set_mode((size, size))
pygame.display.set_caption("Button Display")

start_img = pygame.image.load("start.png").convert_alpha()
end_img = pygame.image.load("end.png").convert_alpha()
 
        
start_btn = buttons2.Button(10, 50, start_img,0.5)
end_btn = buttons2.Button(250, 50, end_img,0.5)  

running = True

while running:
    windows.fill((255, 255, 255))
    if start_btn.draw(windows):
        print("Start button clicked")
    if end_btn.draw(windows):
        print("End button clicked")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()



    
