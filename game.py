import pygame
pygame.init()
pizza_image = pygame.image.load('pizza.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PizzaMaker")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear background
    screen.blit(pizza_image, (100, 100))  # Draw pizza image
    pygame.display.flip()  # Update display
pygame.quit()


