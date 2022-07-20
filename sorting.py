from decimal import MIN_EMIN
import pygame
import random
pygame.init()

class DrawInformation:
    # board setup
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        # 
        self.width = width
        self.height = height

        # get and display the surface
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        # function which sets the list 
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # setting width and height of each block in our display
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()
        
def create_starting_list(n, min_val, max_val):
    # generate a starting
    lst = []

    for _ in range (n):
        val = random.randint(min_val,max_val)
        lst.append(val)
    
    return lst

def main():
    # main function which runs the program 
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = create_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    
    # creating loop which runs the program at 60 frames per second
    while run:
        clock.tick(60)

        draw(draw_info)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            # allows you to quit the program
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
