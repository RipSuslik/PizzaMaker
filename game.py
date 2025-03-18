import pygame
pygame.init()
mikser_image = pygame.image.load('mikser.png')
pizza_image = pygame.image.load('pizza.png')
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("PizzaMaker")
mouse_x, mouse_y = 0, 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.fill((255, 255, 255))  # Clear background
    screen.blit(mikser_image, (mouse_x, mouse_y))  # Draw mikser image
    screen.blit(pizza_image, (mouse_x, mouse_y))  # Draw pizza image
    pygame.display.flip()  # Update display
pygame.quit()


