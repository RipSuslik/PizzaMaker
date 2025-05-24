from dataclasses import dataclass
import pygame

pygame.init()

@dataclass
class Coordinate:
    x: int
    y: int 

@dataclass
class Object:
    image: any
    pos: Coordinate  
    selected: bool
    under_mouse: bool
    key: str
    mouse_offset = Coordinate(0, 0)


@dataclass
class Input:
    mouse_pos = Coordinate(0, 0)
    running = True
    mouse_down = False 
    pressed_key = None

def create_coordinate(tuple):
    return Coordinate(tuple[0], tuple[1])

def add_coordinate(c1, c2):
    return Coordinate(c1.x + c2.x, c1.y + c2.y)

def substract_coordinate(c1, c2):
    return Coordinate(c1.x - c2.x, c1.y - c2.y)

def create_tuple(coord):
    return (coord.x, coord.y)

def update_input(input):
    events = pygame.event.get() #сохраняем в евентс события из pygame
    for current_event in events:
        if current_event.type == pygame.QUIT:
            input.running = False
        elif current_event.type == pygame.MOUSEMOTION:
            input.mouse_pos = create_coordinate(pygame.mouse.get_pos())        
        elif current_event.type == pygame.MOUSEBUTTONDOWN:
            input.mouse_down = True
        elif current_event.type == pygame.MOUSEBUTTONUP:
            input.mouse_down = False
        elif current_event.type == pygame.KEYDOWN:
            input.pressed_key = current_event.key

def set_selected(game_objects, input): 
    for obj in game_objects:
        if not input.mouse_down:
            obj.selected = False
        elif obj.under_mouse:
            if not obj.selected:
                obj.mouse_offset = substract_coordinate(input.mouse_pos, obj.pos)
            obj.selected = True        
            

def move_selected_object(game_objects, input):
    if input.mouse_down: 
        for obj in game_objects:    
            if obj.selected: 
                obj.pos = substract_coordinate(input.mouse_pos, obj.mouse_offset)

def set_under_mouse(game_objects, input):
    for obj in game_objects:
        obj.under_mouse = False
        if (input.mouse_pos.x > obj.pos.x
            and input.mouse_pos.y > obj.pos.y
            and input.mouse_pos.x < obj.pos.x + obj.image.get_width()
            and input.mouse_pos.y < obj.pos.y + obj.image.get_height()):
            obj.under_mouse = True

def draw_all_objects(game_objects, screen):
    for obj in game_objects:
        screen.blit(obj.image, create_tuple(obj.pos))
        
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
                (obj.pos.x,
                obj.pos.y,
                obj.image.get_width(),
                obj.image.get_height()),
                3)

def run_game():
    game_objects = [
        Object(pygame.image.load('mikser.png'), Coordinate(450, 550), False, False, ""), 
        Object(pygame.image.load('pizza.png'), Coordinate(500, 50), False, False, pygame.K_1),
        Object(pygame.image.load('cheeese.png'), Coordinate(15, 0), False, False, pygame.K_2),
        Object(pygame.image.load('cheese.png'), Coordinate(0, 300), False, False, pygame.K_3),
        Object(pygame.image.load('tomatoes.png'), Coordinate(30, 600), False, False, pygame.K_4)
    ]

    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("PizzaMaker")

    input = Input()

    while input.running:
        update_input(input) 
        
        #обрабатываем информацию

        set_under_mouse(game_objects, input)

        set_selected(game_objects, input)

        move_selected_object(game_objects, input)                                        

        #рисуем кадр
        screen.fill((255, 255, 255))  # Clear background

        draw_all_objects(game_objects, screen)
        
        draw_icon(game_objects, screen)

        draw_rect(game_objects, screen)

        pygame.display.flip()  # Update display
    pygame.quit()

run_game()