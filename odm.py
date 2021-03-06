from pygame.version import PygameVersion
from modules import datahandler
import pygame
import ctypes


class Button:
    def __init__(self, path):
        self.surface = pygame.image.load(path)
        self.hover = False
    
    def update(self):
        if self.hover == True:
            self.surface.set_alpha(255)
        else:
            self.surface.set_alpha(130)


def main():
    
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0 )

    data = datahandler.DataHandler()

    pygame.init()
    

    surface = pygame.display.set_mode([1280, 720])
    pygame.display.set_caption('Orbital Debris Mapper')
    clock = pygame.time.Clock()
    
    running = True
    grid_on = False
    focus_on = False
    map_on = True
    count = 0

    mousex, mousey = 0, 0

    world_map = pygame.image.load('assets/world map.jpg')
    world_map = pygame.transform.scale(world_map, [1280, 720])

  

    font = pygame.font.SysFont('arial', 14)

    buffer = []

    for object in data.debris_list:
        data.update_location(object)
                  
       


    # MAIN LOOP
    while running:
        
        # DRAW ~~~~~~~~
        surface.fill([0, 0, 0])

        if map_on == True:
            surface.blit(world_map, [0, 0])
        else:
            surface.fill([240, 240, 240])

        # Draw debris
        for object in data.debris_list:
            pygame.draw.circle(surface, [255, 0, 0], [object.x, object.y], 1)
            
        '''for x in range(0, 1280, int(1280/18)):
            pygame.draw.line(surface, [0, 0, 0, 255], [x, 0], [x, 720], 1)
        for x in range(0, 720, int(720/9)):
            pygame.draw.line(surface, [0, 0, 0], [0, x], [1280, x], 1)
        '''

        # Draw abtion bar


        pygame.display.update()

        # UPDATE ~~~~~~~~~~~~
        
        if count == 0:
            for i in range(0, int(len(data.debris_list) / 3)):
                data.update_location(data.debris_list[i])
            count = 1
        
        elif count == 1:
            for i in range(int(len(data.debris_list) / 3), int(2*(int(len(data.debris_list)) / 3))):
                data.update_location(data.debris_list[i])
            count = 2

        else:
            for i in range(int(2*(len(data.debris_list)) / 3), int(len(data.debris_list) - 1)):
                data.update_location(data.debris_list[i])
            count = 0

        # Obtion bar update
        

        # INPUT ~~~~~~~~~~~~~~~~
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        '''mousex, mousey = pygame.mouse.get_pos()
        if mousex >= 500 and mousex <= 700:
            if mousey >= 660 and mousey <= 700:
                togle_map.hover = True
            else:
                togle_map.hover = False
        else:
            togle_map.hover = False
        '''

        print(clock.tick(30))
    exit()
    # END


if __name__ == '__main__':
    main()