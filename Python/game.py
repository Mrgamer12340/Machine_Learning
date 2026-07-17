import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_SPEED = 3
PIPE_WIDTH = 60
GAP_HEIGHT = 150
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Load assets
bird_img = pygame.image.load("bird.png")  # Use your own bird image
bird_img = pygame.transform.scale(bird_img, (40, 30))

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_vel = 0
score = 0
pipes = []

# Function to create pipes
def create_pipe():
    height = random.randint(100, 400)
    pipes.append([WIDTH, height])

# Main game loop
def game_loop():
    global bird_y, bird_vel, score
    running = True
    frame_count = 0
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_vel = JUMP_STRENGTH
        
        # Bird physics
        bird_vel += GRAVITY
        bird_y += bird_vel
        
        # Generate pipes
        if frame_count % 90 == 0:
            create_pipe()
        
        # Move pipes
        for pipe in pipes:
            pipe[0] -= PIPE_SPEED
            pygame.draw.rect(screen, (0, 255, 0), (pipe[0], 0, PIPE_WIDTH, pipe[1]))
            pygame.draw.rect(screen, (0, 255, 0), (pipe[0], pipe[1] + GAP_HEIGHT, PIPE_WIDTH, HEIGHT))
            
            # Collision detection
            if (bird_x + 40 > pipe[0] and bird_x < pipe[0] + PIPE_WIDTH) and (bird_y < pipe[1] or bird_y + 30 > pipe[1] + GAP_HEIGHT):
                running = False  # Game over
            
            # Update score
            if pipe[0] == bird_x:
                score += 1
        
        # Remove old pipes
        pipes[:] = [pipe for pipe in pipes if pipe[0] > -PIPE_WIDTH]
        
        # Draw bird
        screen.blit(bird_img, (bird_x, bird_y))
        
        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))
        
        # Check for ground collision
        if bird_y > HEIGHT - 30:
            running = False  # Game over
        
        pygame.display.update()
        clock.tick(30)
        frame_count += 1
    
    pygame.quit()
    quit()

game_loop()
