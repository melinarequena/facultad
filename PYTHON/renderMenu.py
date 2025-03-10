import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menú Animado")

font = pygame.font.Font(None, 50)
text = font.render("Bienvenido al Juego", True, (255, 255, 255))
clock = pygame.time.Clock()

x, y = 50, HEIGHT // 2
direction = 3

running = True
while running:
    screen.fill((0, 0, 0))  # Fondo negro
    screen.blit(text, (x, y))
    pygame.display.flip()

    x += direction
    if x + text.get_width() >= WIDTH or x <= 0:
        direction *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)

pygame.quit()
