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

pizza_under_mouse = False

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
            pizza_under_mouse = False
            if mouse_x > pizza_x and mouse_y > pizza_y and mouse_x < pizza_x + pizza_image.get_width() and mouse_y < pizza_y + pizza_image.get_height():
                pizza_under_mouse = True    
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

    icon = None
    if pizza_selected:
        icon = pygame.transform.scale(pizza_image,(100,100)) 
    if cheeese_selected:
        icon = pygame.transform.scale(cheeese_image,(100,100)) 
    if cheese_selected:
        icon = pygame.transform.scale(cheese_image,(100,100)) 
    if tomatoes_selected:
        icon = pygame.transform.scale(tomatoes_image,(100,100)) 

    if icon != None:
        screen.blit(icon, (50,50,100,100))
    pygame.draw.rect(screen,(255,255,0),(50,50,100,100),3)

    if pizza_under_mouse:
        pygame.draw.rect(screen,(245,52,134),(pizza_x,pizza_y,pizza_image.get_width(),pizza_image.get_height()),3)

    pygame.display.flip()  # Update display
pygame.quit()

