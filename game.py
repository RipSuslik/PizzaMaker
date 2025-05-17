from dataclasses import dataclass
import pygame

pygame.init()

@dataclass
class Object:
    image: any
    pos: tuple[int,int]  
    selected: bool
    under_mouse: bool
    key: str
                                                              
@dataclass
class Input:
    mouse_pos = (0,0)
    running = True
    mouse_down = False 
    pressed_key = None 

def update_input(input):
    events = pygame.event.get() #сохраняем в евентс события из pygame
    for current_event in events:
        if current_event.type == pygame.QUIT:
            input.running = False
        elif current_event.type == pygame.MOUSEMOTION:
            input.mouse_pos = pygame.mouse.get_pos()        
        elif current_event.type == pygame.MOUSEBUTTONDOWN:
            input.mouse_down = True
        elif current_event.type == pygame.MOUSEBUTTONUP:
            input.mouse_down = False
        elif current_event.type == pygame.KEYDOWN:
            input.pressed_key = current_event.key

def set_selected(game_objects, input): 
    for obj in game_objects:    
        obj.selected = False

    for obj in game_objects:
        if input.pressed_key == obj.key:
            obj.selected = True

def move_selected_object(game_objects, input):
    if input.mouse_down: 
        for obj in game_objects:    
            if obj.selected: 
                obj.pos = input.mouse_pos

def set_under_mouse(game_objects, input):
    for obj in game_objects:
        obj.under_mouse = False
        if (input.mouse_pos[0] > obj.pos[0]
            and input.mouse_pos[1] > obj.pos[1]
            and input.mouse_pos[0] < obj.pos[0] + obj.image.get_width()
            and input.mouse_pos[1] < obj.pos[1] + obj.image.get_height()):
            obj.under_mouse = True

def draw_all_objects(game_objects, screen):
    for obj in game_objects:
        screen.blit(obj.image, obj.pos)
        
def draw_icon(game_objects, screen):
    icon = None 
    for obj in game_objects:
        if obj.selected:
            icon = pygame.transform.scale(obj.image,(100,100))

    if icon != None:
        screen.blit(icon, (50,50,100,100))
    pygame.draw.rect(screen,(255,255,0),(50,50,100,100),3)

def draw_rect(game_objects, screen):
    for obj in game_objects:
        if obj.under_mouse:
            pygame.draw.rect(
                screen,
                (245,52,134),
                (obj.pos[0],
                obj.pos[1],
                obj.image.get_width(),
                obj.image.get_height()),
                3)

def run_game():
    game_objects = [
        Object(pygame.image.load('mikser.png'),(450,550), False, False, ""), 
        Object(pygame.image.load('pizza.png'),(500,50), False, False, pygame.K_1),
        Object(pygame.image.load('cheeese.png'),(15,0), False, False, pygame.K_2),
        Object(pygame.image.load('cheese.png'),(0,300), False, False, pygame.K_3),
        Object(pygame.image.load('tomatoes.png'),(30,600), False, False, pygame.K_4)
    ]

    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("PizzaMaker")

    input = Input()

    while input.running:
        update_input(input) 
        
                # если нажата клавиша мыши то выбираем объект под ней
        #обрабатываем информацию

        set_under_mouse(game_objects, input)

        set_selected(game_objects, input)

        move_selected_object(game_objects, input)                                        

        #совершаем действия с игрой (картинками (пока что))
        screen.fill((255, 255, 255))  # Clear background

        draw_all_objects(game_objects, screen)
        
        draw_icon(game_objects, screen)

        draw_rect(game_objects, screen)

        pygame.display.flip()  # Update display
    pygame.quit()

run_game()