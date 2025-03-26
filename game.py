import pygame
pygame.init()
mikser_image = pygame.image.load('mikser.png')
pizza_image = pygame.image.load('pizza.png')
cheeese_image = pygame.image.load('cheeese.png')
cheese_image = pygame.image.load('cheese.png')
tomatoes_image = pygame.image.load('tomatoes.png')
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("PizzaMaker")
mouse_x, mouse_y = 0, 0
pizza_x, pizza_y = 450, 700
running = True
mouse_down = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    screen.fill((255, 255, 255))  # Clear background
    screen.blit(mikser_image, (450, 550))  # Draw mikser image
    if mouse_down:
        pizza_x, pizza_y = mouse_x, mouse_y     
    screen.blit(pizza_image, (pizza_x, pizza_y))  # Draw pizza image
    pizza_x, pizza_y = mouse_x, mouse_y     
    screen.blit(cheeese_image, (cheeese_x, cheeese_y))  # Draw cheeese image
    cheeese_x, cheeese_y = mouse_x, mouse_y     
    screen.blit(cheese_image, (cheese_x, cheese_y))  # Draw cheese image
    cheese_x, cheese_y = mouse_x, mouse_y
    screen.blit(tomatoes_image, (tomatoes_x, tomatoes_y))  # Draw tomatoes image
    tomatoes_x, tomatoes_y = mouse_x, mouse_y
    pygame.display.flip()  # Update display
pygame.quit()


