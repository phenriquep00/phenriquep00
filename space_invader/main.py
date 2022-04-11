import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('001-space-invaders.png')
playerX = 375
playerY = 480
playerX_change = 0

# enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _ in range(num_of_enemies):
    enemy_img.append(pygame.image.load('001-alien.png'))
    enemyX.append(random.randint(0, 767))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# bullet
bullet_img = pygame.image.load('001-bullet.png')
bulletY = 480
bulletX = 0
bulletY_change = 5
bullet_state = 'ready'  # ready means the bullet can't be seen, fire means the bullet is moving

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 26)

textX = 10
textY = 10

# game over text:
over_font = pygame.font.Font('freesansbold.ttf', 72)


# functions:
def game_over_text():

    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))



def show_score(x, y):

    score = font.render('Score :' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):

    screen.blit(player_img, (x, y))


def enemy(x, y, _):

    screen.blit(enemy_img[_], (x, y))


def fire_bullet(x, y):

    global  bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 8, y + 5))



def IsColision(enemyX, enemyY, bulletX, bulleY):

    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))

    if distance < 23:

        return True
    else: 

        return False


# Game loop
running = True

while running:
    
    # RED GREEN AND BLUE
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))

    # Event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # boundaries
    playerX += playerX_change

    # width borders
    if playerX <= 0:

        playerX = 0
    elif playerX >= 768:
        
        playerX = 768

    # Enemy movement
    for _ in range(num_of_enemies):

        # Game Over:
        if enemyY[_] > 440:
            for i in range(num_of_enemies):
                enemyY[i] = 2000
                
            game_over_text()
            break
        enemyX[_] += enemyX_change[_]
        # width borders
        if enemyX[_] <= 0:
            enemyX_change[_] = 2
            enemyY[_] += enemyY_change[_]
        elif enemyX[_] >= 768:
            enemyX_change[_] = -2
            enemyY[_] += enemyY_change[_]
        
        # Colision
        colision = IsColision(enemyX[_], enemyY[_], bulletX, bulletY)
        if colision:
            colision_sound = mixer.Sound('explosion.wav')
            colision_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[_] = random.randint(0, 767)
            enemyY[_] = random.randint(50, 150)

        enemy(enemyX[_], enemyY[_], _)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
