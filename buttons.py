import pygame
class Button:
    def __init__(self, x, y, image, scale):
        # Get original width and height of the image
        width = image.get_width()
        height = image.get_height()
        
        # State to track if the button was clicked
        self.clicked = False
        
        # Scale the image to the specified scale factor
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        
        # Create a rect object for positioning and click detection
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y) # Set top-left corner position   

    def draw(self, surface):
        # Get the current position of the mouse
        pos = pygame.mouse.get_pos()
        
        # Boolean to check if the button was actively clicked
        active = False
        
        # Check if the mouse is over the button and if the left button is pressed
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True # Prevents multiple rapid triggers
                active = True # Signal that the button is activated
                
        # Reset the click state when the mouse button is released        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # Draw the button image on the given surface
        surface.blit(self.image, (self.rect.x, self.rect.y))   
        
        # Return whether the button was clicked
        return active