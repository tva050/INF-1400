""" 
This is made mostly for fun, so alot (almost everything) of the code is from:
https://github.com/baraltech/Menu-System-PyGame/blob/551c6f3262cdb0d91b0803fa4a1beb8136c90bc1/main.py#L40
"""

class Bottom:
    """ 
    This class is used to create buttons for the game.
    
    ...
    
    Attributes:
    ----------
    image : pygame.Surface
        The image of the button
    rect : pygame.Rect
        The rectangle of the button
    screen : pygame.Surface
        The screen the button is drawn on
    
    
    Methods:
    -------
    draw()
        Draws the button on the screen
    update()
        Updates the button
    check_for_input()
        Checks if the button is clicked
    """
    def __init__(self, image, pos):
        """ 
        Constructs all the necessary attributes for the button object.
        
        Parameters
        ----------
            image : str
                The image of the button
            pos : tuple
                The position of the button
        """
        self.image = image
        
        self.x = pos[0]
        self.y = pos[1] 
        
        self.rect = self.image.get_rect(center = (self.x, self.y))
        
    def draw(self, screen):
        """ 
        Draws the button on the screen.
        
        Parameters
        ----------
            screen : pygame.Surface
                The screen the button is drawn on
        """
        screen.blit(self.image, self.rect)
            
    def check_for_input(self, position):
        """
        Checks if the button is clicked.
    
        Parameters
        ----------
            position : tuple
                The position of the mouse
        """
        # Check if the mouse is over the button and if it is clicked then return True else return False 
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False
        
    
