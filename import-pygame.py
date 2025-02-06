
import pygame
import random

# Initialiser pygame
pygame.init()

# Skærmstørrelse
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fang bolden")

# Farver
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Spillerens platform
player_width = 100
player_height = 15
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 7

# Bolden
ball_size = 20
ball_x = random.randint(0, WIDTH - ball_size)
ball_y = 0
ball_speed = 10

# Spillet kører
running = True
score = 0
level = 1

tilbage = 10


font = pygame.font.Font(None, 36)

def reset():
    global score, level, tilbage,ball_x,ball_y  # Brug globalt scope for at opdatere variablerne
    score=0
    level=1
    tilbage=10
    ball_y = 0
    ball_x = random.randint(0, WIDTH - ball_speed)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # Exit reset() when SPACE is pressed
            elif event.type == pygame.QUIT:
                pygame.quit()
                
def levelUp():
    global level,ball_speed,tilbage,player_width,ball_size
    level=level+1
    tilbage = 10
    if level == 2:
        ball_speed = 12
    elif level == 3:
        player_width = 75
    elif level ==4:
        ball_size = 15
    elif level==5:
        player_width = 50


while running:
    screen.fill(WHITE)

    # Events (luk spillet med kryds)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spillerens bevægelse
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Boldens bevægelse
    ball_y += ball_speed

    # Tjek om bolden rammer platformen
    if ball_y + ball_size >= player_y and player_x < ball_x < player_x + player_width:
        ball_y = 0
        ball_x = random.randint(0, WIDTH - ball_size)
        score += 1  # +1 point
        tilbage = tilbage -1
    if tilbage <= 0:
        levelUp()
    # Tjek om bolden rammer bunden (tabt)
    if ball_y > HEIGHT:
        reset()

    # Tegn spilleren og bolden
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, ball_size, ball_size))

    # Tegn scoren
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    text = font.render(f"level: {level}", True, (10, 25, 5))
    screen.blit(text, (400, 10))

    text = font.render(f"Tilbage: {tilbage}", True, (10, 25, 5))
    screen.blit(text, (180, 10))


    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
