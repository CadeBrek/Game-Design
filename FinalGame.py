import pygame
import sys
import random
from pygame import display
from pygame.display import init
from pygame.locals import *
import os
# Game Initialization

pygame.init()
# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
cake= pygame.image.load("cake.png")
explosion= pygame.image.load("Explosion.png")
warmachine= pygame.image.load("warmachine.png")
monkey= pygame.image.load("monkey 1.png")
baboon= pygame.image.load("baboon.png")
explosion = pygame.transform.scale(explosion , (100,100))
warmachine = pygame.transform.scale(warmachine , (100,100))

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
def ballz():
    import pygame
    screen_width=800
    screen_height=600
    screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)

        return newText


    # Colors
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)
    cake= pygame.image.load("cake.png")
    explosion= pygame.image.load("Explosion.png")
    warmachine= pygame.image.load("warmachine.png")
    monkey= pygame.image.load("monkey 1.png")
    baboon= pygame.image.load("baboon.png")
    # Game Fonts
    font = "Retro.ttf"


    # Game Framerate
    clock = pygame.time.Clock()
    FPS=30
    size = (800, 600)
    screen = pygame.display.set_mode
    screen=pygame.display.set_mode(size)
    all_sprites_list = pygame.sprite.Group() 

    score = 0
    lives = 3

        # Open a new window

        #This will be a list that will contain all the sprites we intend to use in our game.
        #Create the Paddle

    import pygame
    BLACK = (0,0,0)

    class Paddle(pygame.sprite.Sprite):
        #This class represents a paddle. It derives from the "Sprite" class in Pygame.

        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Pass in the color of the paddle, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            # Draw the paddle (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])

            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()


        def moveLeft(self, pixels):
            self.rect.x -= pixels
            #Check that you are not going too far (off the screen)
            if self.rect.x < 0:
                self.rect.x = 0

        def moveRight(self, pixels):
            self.rect.x += pixels
            #Check that you are not going too far (off the screen)
            if self.rect.x > 700:
                self.rect.x = 700
        
        def moveUp(self, pixels):
            self.rect.y -= pixels
            if self.rect.y < 550:
                self.rect.y = 551

        def moveDown(self, pixels):
            self.rect.y += pixels
            if self.rect.y < 0:
                self.rect.y = 0


    paddle = Paddle(LIGHTBLUE, 100, 10)
    paddle.rect.x = 350
    paddle.rect.y = 560

    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop

        # --- Game logic should go here
        all_sprites_list.update()

        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.fill(DARKBLUE)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))

        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(180)


    #Create the ball sprite
    import pygame
    from random import randint

    BLACK = (0, 0, 0)

    class Ball(pygame.sprite.Sprite):
        #This class represents a ball. It derives from the "Sprite" class in Pygame.
        
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            # Pass in the color of the ball, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            # Draw the ball (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            
            self.velocity = [randint(4,8),randint(-8,8)]
            
            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
            
        def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            
        def bounce(self):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8,8)
    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195


    import pygame
    BLACK = (0,0,0)

    class Brick(pygame.sprite.Sprite):
        #This class represents a brick. It derives from the "Sprite" class in Pygame.

        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Pass in the color of the brick, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            # Draw the brick (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])

            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
    all_bricks = pygame.sprite.Group()
    for i in range(7):
        brick = Brick(RED,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(ORANGE,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(YELLOW,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop

        #Moving the paddle when the use uses the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(8)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(8)
        if keys[pygame.K_UP]:
            paddle.moveUp(1)
        if keys[pygame.K_DOWN]:
            paddle.moveDown(1)

        # --- Game logic should go here
        all_sprites_list.update()

        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>590:
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                #Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(100)

                #Stop the Game
                carryOn=False

        if ball.rect.y<40:
            ball.velocity[1] = -ball.velocity[1]

        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        #Check if there is the ball collides with any of bricks
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            ball.bounce()
            score += 1
            brick.kill()
        if len(all_bricks)==0:
            #Display Level Complete Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                #Stop the Game
                carryOn=False

        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.fill(DARKBLUE)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))

        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


# Game Initialization
pygame.init()


# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
def ballz2():
    import pygame
    screen_width=800
    screen_height=600
    screen=pygame.display.set_mode((screen_width, screen_height))

    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)

        return newText


    # Colors
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)

    # Game Fonts
    font = "Retro.ttf"


    # Game Framerate
    clock = pygame.time.Clock()
    FPS=30
    size = (800, 600)
    screen = pygame.display.set_mode
    screen=pygame.display.set_mode(size)
    all_sprites_list = pygame.sprite.Group() 

    score = 0
    lives = 3

        # Open a new window

        #This will be a list that will contain all the sprites we intend to use in our game.
        #Create the Paddle
    import pygame
    BLACK = (0,0,0)

    import pygame
    BLACK = (0,0,0)

    class Paddle(pygame.sprite.Sprite):
        #This class represents a paddle. It derives from the "Sprite" class in Pygame.

        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Pass in the color of the paddle, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            # Draw the paddle (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])

            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()


        def moveLeft(self, pixels):
            self.rect.x -= pixels
            #Check that you are not going too far (off the screen)
            if self.rect.x < 0:
                self.rect.x = 0

        def moveRight(self, pixels):
            self.rect.x += pixels
            #Check that you are not going too far (off the screen)
            if self.rect.x > 700:
                self.rect.x = 700
        
        def moveUp(self, pixels):
            self.rect.y -= pixels
            if self.rect.y < 550:
                self.rect.y = 551

        def moveDown(self, pixels):
            self.rect.y += pixels
            if self.rect.y < 0:
                self.rect.y = 0


    paddle = Paddle(LIGHTBLUE, 100, 10)
    paddle.rect.x = 350
    paddle.rect.y = 560

    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop

        # --- Game logic should go here
        all_sprites_list.update()

        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.fill(DARKBLUE)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))

        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(180)


    #Create the ball sprite
    import pygame
    from random import randint

    BLACK = (0, 0, 0)

    class Ball(pygame.sprite.Sprite):
        #This class represents a ball. It derives from the "Sprite" class in Pygame.
        
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()
            
            # Pass in the color of the ball, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            # Draw the ball (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            
            self.velocity = [randint(4,8),randint(-8,8)]
            
            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
            
        def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            
        def bounce(self):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8,8)
    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195


    import pygame
    BLACK = (0,0,0)

    class Brick(pygame.sprite.Sprite):
        #This class represents a brick. It derives from the "Sprite" class in Pygame.

        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Pass in the color of the brick, and its x and y position, width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)
            self.image.set_colorkey(BLACK)

            # Draw the brick (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])

            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()
    all_bricks = pygame.sprite.Group()
    for i in range(7):
        brick = Brick(RED,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(ORANGE,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(YELLOW,80,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    # Add the paddle to the list of sprites
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop

        #Moving the paddle when the use uses the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(4)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(4)
        if keys[pygame.K_UP]:
            paddle.moveUp(1)
        if keys[pygame.K_DOWN]:
            paddle.moveDown(1)

        # --- Game logic should go here
        all_sprites_list.update()

        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>590:
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                #Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(100)

                #Stop the Game
                carryOn=False

        if ball.rect.y<40:
            ball.velocity[1] = -ball.velocity[1]

        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        #Check if there is the ball collides with any of bricks
        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            ball.bounce()
            score += 1
            brick.kill()
        if len(all_bricks)==0:
            #Display Level Complete Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                #Stop the Game
                carryOn=False

        # --- Drawing code should go here
        # First, clear the screen to dark blue.
        screen.fill(DARKBLUE)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

        #Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))

        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)



## LISTS FOR MENU MESSAGES

screenMessage=[ "800x800", "800x600", "600x600"]
settingMessages=["Screen Size", "Background colors", "Object Colors","Sounds On/Off"]
mainMenu=["Instructions", 'Settings', "Easy Mode", "Hard Mode", "ScoreBoard", "Exit"]
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
SCOREBOARD=False
OBJECTCOLOR=False
SOUNDS=False
flag=False
selected="start"
# Screen and square definition
WIDTH=800
HEIGHT=700
wbox=30
hbox=30
x=70
y=150
xs=50
ys=200
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")
square=pygame.Rect(x,y, wbox,hbox)
screenSize=pygame.Rect(xs,ys,wbox*4, hbox*4)
win.fill(COLOR)
squaresSize=[pygame.Rect(xs,ys,wbox*4, hbox*4), pygame.Rect(xs,ys,wbox*4, hbox*3), pygame.Rect(xs,ys,wbox*3, hbox*3)]
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans', 80)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
INSTRUCTIONS_FONT=pygame.font.SysFont('comicsans', 30)
text= TITLE_FONT.render('message',1,BLACK)
#New window title
#images
#Function to print Titles to all screens
cake = pygame.image.load('cake.png')
cake = pygame.transform.scale(cake , (100,100))
monkey = pygame.image.load('monkey 1.png')
monkey = pygame.transform.scale(monkey, (100,100))
baboon = pygame.image.load('baboon.png')
baboon = pygame.transform.scale(baboon, (100,100))
def display_Title(message,ym):
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

#Function to print all the menus 
def Menu_function(line):
    pygame.time.delay(100)
    ym=y
    square.y=y
    xm=x+wbox+10
    for i in range(0,len(line)):
        word=line[i]
        pygame.draw.rect(win, ORANGE, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym
    
def MainMenuWin(xm,ym):
    global MAINMENU
    global INSTRUCTIONS
    global SETTINGS
    global LEVEL1
    global LEVEL2
    global SCOREBOARD
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        SETTINGS = True  
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Easy Mode")
        display_Title("Easy Mode",  70)
        display_Title("Back", HEIGHT-95)

        pygame.display.update()
        MAINMENU = False
        LEVEL1 = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 2")
        display_Title("Level 2",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=550 and ym<=575: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("ScoreBoard")
        display_Title("Scoreboard",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=650 and ym<=675: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("Exit",  70)
        display_Title("Back", HEIGHT-95)
        pygame.display.update()
        MAINMENU = False
        global run
        run=False
def SettingMenuWin(xm,ym):
    global SETTINGS
    global SCREEN
    global BACKGROUND
    global OBJECTCOLOR
   
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        display_Title("Screen Size", 70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        SCREEN = True  
                   
    if xm>=70 and xm<=95 and ym>=250 and ym<=275 and flag: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("BACKGROUND COLORS",  70)
        display_Title("BACK", 750)
        pygame.display.update()
        BACKGROUND = True
        SETTINGS = False             
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("OBJECT COLORS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("SOUNDS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
def Menu_Back():
    win.fill(COLOR)
    display_Title("MAIN", 70)
    Menu_function(mainMenu)
    pygame.display.update()
def Setting_Back():
    win.fill(COLOR)
    display_Title("SETTINGS", 70)
    Menu_function(settingMessages)
    display_Title("Back", HEIGHT-95)
    pygame.display.update()
def Screen_size():
    pygame.time.delay(100)
    ym=ys
    screenSize.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(win, ORANGE, squary)
        word= screenMessage[i]
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200
def game_Mainmenu():
    win.blit(cake, (0,0))
    win.blit(warmachine, (400,0))
    win.blit(explosion, (300,0))
    pygame.display.set_caption("Easy Mode")
    if selected=="Easy Mode":
        print("Easy Mode")
    pygame.display.flip()
    #add your game logic here
def game_Settings():
    win.blit(monkey, (0,0))
    win.blit(baboon, (600,0))
    pygame.display.set_caption("Hard Mode")
    if selected=="Hard Mode":
        print("Hard Mode")
    pygame.display.flip()
# def Color_screen():
#     for key in colors:
#Start Program
display_Title("MENU", 40)
Menu_function(mainMenu)
run=True 
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    mouse_pos=(0,0)
    if eve.type==pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            xm=mouse_pos[0]
            ym=mouse_pos[1]
            if MAINMENU:
                MainMenuWin(xm,ym)
            if INSTRUCTIONS:
                game_Mainmenu()
                myFile=open('instructions.txt', 'r')
                yi=150
                for line in myFile.readlines():
                    text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                    win.blit(text, (40,yi))
                    pygame.display.update()
                    pygame.time.delay(100)
                    yi+=50
                myFile.close()
                if xm >335 and xm<460 and ym>645 and ym<695:
                    Menu_Back()
                    MAINMENU = True
                    INSTRUCTIONS = False
            if SETTINGS:
                game_Settings()
                SettingMenuWin(xm,ym)
                flag=True
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Menu_Back()
                    MAINMENU = True
                    SETTINGS = False
                    flag=False
            if SCREEN:
                Screen_size()
                display_Title("Back", HEIGHT-95)
                pygame.display.update()
                if xm>450 and xm <540 and ym>200 and ym<290: 
                    WIDTH=600
                    HEIGHT=600
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.fill(COLOR)
                    Screen_size()
                    display_Title("Back", HEIGHT-95)
                    pygame.display.update()
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
                
                if SCREEN:
                    Screen_size()
                display_Title("Back", HEIGHT-95)
                pygame.display.update()
                if xm>100 and xm <200 and ym>200 and ym<290: 
                    WIDTH=800
                    HEIGHT=800
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.fill(COLOR)
                    Screen_size()
                    display_Title("Back", HEIGHT-95)
                    pygame.display.update()
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False

                if SCREEN:
                    Screen_size()
                display_Title("Back", HEIGHT-95)
                pygame.display.update()
                if xm>250 and xm <400 and ym>200 and ym<290: 
                    WIDTH=800
                    HEIGHT=600
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.fill(COLOR)
                    Screen_size()
                    display_Title("Back", HEIGHT-95)
                    pygame.display.update()
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False

            if BACKGROUND:
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    BACKGROUND = False
            if OBJECTCOLOR:
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    OBJECTCOLOR = False
            if LEVEL1:
                #play game here
                ballz()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    LEVEL1 = False
                pygame.display.flip()
            if LEVEL2:
                #Play game
                ballz2()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    LEVEL2 = False
            if SCOREBOARD:
                game_Mainmenu()
                myFile=open('scoreboard.txt', 'r')
                yi=150
                for line in myFile.readlines():
                    text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                    win.blit(text, (40,yi))
                    pygame.display.update()
                    pygame.time.delay(100)
                    yi+=50
                myFile.close()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    SCOREBOARD = False
pygame.display.flip()
pygame.quit()
quit()