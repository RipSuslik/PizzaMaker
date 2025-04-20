import pygame

pygame.init()

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
mikser_image = pygame.image.load('mikser.png')
pizza_image = pygame.image.load('pizza.png')
cheeese_image = pygame.image.load('cheeese.png')
cheese_image = pygame.image.load('cheese.png')
tomatoes_image = pygame.image.load('tomatoes.png')

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("PizzaMaker")

mouse_x, mouse_y = 0, 0
pizza_x, pizza_y = 100, 700
cheeese_x, cheeese_y = 150, 700
cheese_x, cheese_y = 450, 700
tomatoes_x, tomatoes_y = 1050, 700
running = True
mouse_down = False

pizza_selected = False
cheeese_selected = False
cheese_selected = False
tomatoes_selected = False

while running: 
    #получаем информацию с помощью get() от pygame
    events = pygame.event.get() #сохраняем в евентс события из pygame
    for current_event in events:
        if current_event.type == pygame.QUIT:
            running = False
        elif current_event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
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

            """ elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow pressed")
            elif event.key == pygame.K_SPACE:
                print("Spacebar pressed")
            else:
                print(f"Key {event.key} pressed")"""

    #обрабатываем информацию 
    if mouse_down:
        if pizza_selected: 
            pizza_x, pizza_y = mouse_x, mouse_y
        if cheeese_selected:
            cheeese_x, cheeese_y = mouse_x, mouse_y
        if cheese_selected:
            cheese_x, cheese_y = mouse_x, mouse_y
        if tomatoes_selected:
            tomatoes_x, tomatoes_y = mouse_x, mouse_y

    #совершаем действия с игрой (картинками (пока что))
    screen.fill((255, 255, 255))  # Clear background

    screen.blit(mikser_image, (450, 550))  # Draw mikser image     
    screen.blit(pizza_image, (pizza_x, pizza_y))  # Draw pizza image     
    screen.blit(cheeese_image, (cheeese_x, cheeese_y))  # Draw cheeese image     
    screen.blit(cheese_image, (cheese_x, cheese_y))  # Draw cheese image
    screen.blit(tomatoes_image, (tomatoes_x, tomatoes_y))  # Draw tomatoes image

    pygame.display.flip()  # Update display
pygame.quit()

