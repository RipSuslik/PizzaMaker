from dataclasses import dataclass
import pygame

pygame.init()

@dataclass
class Object:
    image: any
    pos: tuple[int,int]  
    selected: bool
    under_mouse: bool
"""
images_names = ['mikser.png','pizza.png','cheeese.png','cheese.png','tomatoes.png']
images = []
i=0
while (i<5):
    name = images_names[i]
    image = pygame.image.load(name)
    images.append(image)
    i=i+1
""" 
objects = [
    Object(pygame.image.load('mikser.png'),(450,550), False, False),
    Object(pygame.image.load('pizza.png'),(500,50), False, False),
    Object(pygame.image.load('cheeese.png'),(15,0), False, False),
    Object(pygame.image.load('cheese.png'),(0,300), False, False),
    Object(pygame.image.load('tomatoes.png'),(30,600), False, False)
]

"""mikser_image = pygame.image.load('mikser.png')
pizza_image = pygame.image.load('pizza.png')
cheeese_image = pygame.image.load('cheeese.png')
cheese_image = pygame.image.load('cheese.png')
tomatoes_image = pygame.image.load('tomatoes.png')
"""
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("PizzaMaker")

mouse_x, mouse_y = 0, 0
"""pizza_x, pizza_y = 500, 0
cheeese_x, cheeese_y = 15, 0
cheese_x, cheese_y = 0, 300 
tomatoes_x, tomatoes_y = 30, 600"""
running = True
mouse_down = False

"""pizza_under_mouse = False

pizza_selected = False
cheeese_selected = False
cheese_selected = False
tomatoes_selected = False"""

while running: 
    #получаем информацию с помощью get() от pygame
    events = pygame.event.get() #сохраняем в евентс события из pygame
    for current_event in events:
        if current_event.type == pygame.QUIT:
            running = False
        elif current_event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            objects[1].under_mouse = False
            if mouse_x > objects[1].pos[0] and mouse_y > objects[1].pos[1] and mouse_x < objects[1].pos[0] + objects[1].image.get_width() and mouse_y < objects[1].pos[1] + objects[1].image.get_height():
                objects[1].under_mouse = True    
        elif current_event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif current_event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif current_event.type == pygame.KEYDOWN:
            
            pizza_selected = False
            cheeese_selected = False
            cheese_selected = False
            tomatoes_selected = False

            if current_event.key == pygame.K_1:
                pizza_selected = True
            elif current_event.key == pygame.K_2:
                cheeese_selected = True
            elif current_event.key == pygame.K_3:
                cheese_selected = True
            elif current_event.key == pygame.K_4:
                tomatoes_selected = True

     
            # если нажата клавиша мыши то выбираем объект под ней
    #обрабатываем информацию 

    """if mouse_down: ToDo
        if pizza_selected: 
            pizza_x, pizza_y = mouse_x, mouse_y
        if cheeese_selected:
            cheeese_x, cheeese_y = mouse_x, mouse_y
        if cheese_selected:
            cheese_x, cheese_y = mouse_x, mouse_y
        if tomatoes_selected:
            tomatoes_x, tomatoes_y = mouse_x, mouse_y"""

    #совершаем действия с игрой (картинками (пока что))
    screen.fill((255, 255, 255))  # Clear background

    for obj in objects:
        screen.blit(obj.image, obj.pos)


    """screen.blit(objects[0].image, objects[0].pos)  # Draw mikser image     
    screen.blit(objects[1].image, objects[1].pos)  # Draw pizza image     
    screen.blit(objects[2].image, objects[2].pos)  # Draw cheeese image     
    screen.blit(objects[3].image, objects[3].pos)  # Draw cheese image
    screen.blit(objects[4].image, objects[4].pos)  # Draw tomatoes image"""

    icon = None
    if objects[1].selected:
        icon = pygame.transform.scale(objects[1].image,(100,100)) 
    if objects[2].selected:
        icon = pygame.transform.scale(objects[2].image,(100,100)) 
    if objects[3].selected:
        icon = pygame.transform.scale(objects[3].image,(100,100)) 
    if objects[4].selected:
        icon = pygame.transform.scale(objects[4].image,(100,100)) 

    if icon != None:
        screen.blit(icon, (50,50,100,100))
    pygame.draw.rect(screen,(255,255,0),(50,50,100,100),3)

    if objects[1].under_mouse:
        pygame.draw.rect(
            screen,
            (245,52,134),
            (objects[1].pos[0],
             objects[1].pos[1],
             objects[1].image.get_width(),
             objects[1].image.get_height()),
            3)

    pygame.display.flip()  # Update display
pygame.quit()

