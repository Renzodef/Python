# Python's version used: 3.8.2 64 bit
# pip install pygame
# pip uninstall pyinstaller
# pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
# For Windows executable installer, go in the folder of the .py file and type:
# pyinstaller --onefile --noconsole --add-data="background.png;." --add-data="bird.png;." --add-data="base.png;." --add-data="gameover.png;." --add-data="tube.png;." --add-data="icon.png;." --icon=icon.ico "Flappy Bird.py"
import pygame
import random
import os
import sys

try:
    # Initialize pygame
    pygame.init()
    # Title of the window
    pygame.display.set_caption('Flappy Bird')
    # Icon
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(sys._MEIPASS, "icon.png")
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            icon_path = "icon.png"
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)

    # Loading all the images in the Image directory
    if getattr(sys, 'frozen', False):
        background_path = os.path.join(sys._MEIPASS, "background.png")
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            background_path = "background.png"
    background = pygame.image.load(background_path)
    if getattr(sys, 'frozen', False):
        bird_path = os.path.join(sys._MEIPASS, "bird.png")
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            bird_path = "bird.png"
    bird = pygame.image.load(bird_path)
    if getattr(sys, 'frozen', False):
        base_path = os.path.join(sys._MEIPASS, "base.png")
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            base_path = "base.png"
    base = pygame.image.load(base_path)
    if getattr(sys, 'frozen', False):
        gameover_path = os.path.join(sys._MEIPASS, "gameover.png")
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            gameover_path = "gameover.png"
    gameover = pygame.image.load(gameover_path)
    if getattr(sys, 'frozen', False):
        tube_path = os.path.join(sys._MEIPASS, "tube.png")
    else:
        try:
            os.chdir(os.path.dirname(__file__))
        except:
            pass
        finally:
            tube_path = "tube.png"
    tube = pygame.image.load(tube_path)
    tube_up = pygame.transform.flip(tube, False, True)

    # Setting the size of the display
    # according to the size of the background image
    display = pygame.display.set_mode((288, 512))
    # Setting the FPS
    fps = 50
    # Feed speed
    feed_speed = 3
    font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

    class tubes_creation():
        def __init__(self):
            # Horizontal position of the tube
            self.x = 300
            # Vertical position
            self.y = random.randint(-75, 150)

        def forward_and_draw(self):
            self.x -= feed_speed
            # Change these two numbers according to the difficulty you want to achieve
            # Lower numbers will make the game more difficult
            # The numbers must be the same
            display.blit(tube, (self.x, self.y + 230))
            display.blit(tube_up, (self.x, self.y - 230))

        def collision(self, bird, bird_x, bird_y):
            tolerance = 5
            bird_right_side = bird_x + bird.get_width() - tolerance
            bird_left_side = bird_x + tolerance
            tubes_right_side = self.x
            tubes_left_side = self.x + tube.get_width()
            bird_up_side = bird_y + tolerance
            bird_down_side = bird_y + bird.get_height() - tolerance
            tubes_up_side = self.y + 90
            tubes_down_side = self.y + 233
            if bird_right_side > tubes_right_side and bird_left_side < tubes_left_side:
                if bird_up_side < tubes_up_side or bird_down_side > tubes_down_side:
                    game_over()

        def between_the_tubes(self, bird, bird_x):
            tolerance = 5
            bird_right_side = bird_x + bird.get_width() - tolerance
            bird_left_side = bird_x + tolerance
            tubes_right_side = self.x
            tubes_left_side = self.x + tube.get_width()
            if bird_right_side > tubes_right_side and bird_left_side < tubes_left_side:
                return True

    # Initialize function
    def initialize():
        # bird_x is the x position of the bird
        # bird_y is the y position of the bird
        # bird_sy is the vertical speed of the bird
        global bird_x, bird_y, bird_sy
        global basex
        global tubes
        global points
        global between_the_tubes
        bird_x, bird_y = 60, 150
        bird_sy = 0
        basex = 0
        points = 0
        tubes = []
        tubes.append(tubes_creation())
        between_the_tubes = False

    def game_over():
        display.blit(gameover, (50, 180))
        update()
        begin_again = False
        # When we lose we want to start the game again
        # by pressing the space bar
        while not begin_again:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    initialize()
                    begin_again = True
                if event.type == pygame.QUIT:
                    pygame.quit()

    # Function needed to draw the objects throughout the game
    def draw_objects():
        display.blit(background, (0, 0))
        for t in tubes:
            t.forward_and_draw()
        display.blit(bird, (bird_x, bird_y))
        display.blit(base, (basex, 400))
        # The first argument of render is the string we want to visualize
        # the second is to make true the anti aliasing
        # the third is the color in RGB
        points_render = font.render(str(points), 1, (50, 205, 50))
        display.blit(points_render, (130, 420))

    # Screen and FPS update
    def update():
        pygame.display.update()
        pygame.time.Clock().tick(fps)

    initialize()

    # Main cycle
    # This game won't finish ever
    # because the loop will never be closed
    while True:
        # In every cycle
        # the base will be moved to left
        basex -= feed_speed
        # If basex has less than 45 pixel
        # we return it at the initial position
        # So the base will exist always
        if basex < -45: basex = 0
        # Gravity's effetct
        bird_sy += 1
        bird_y += bird_sy
        for event in pygame.event.get():
            # If we press a key and this key is the up key
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                # the bird will stop to go down and begin to go up
                bird_sy = -10
            # If we press the X the game will be closed
            if event.type == pygame.QUIT:
                pygame.quit()
        # Creation of new tubes
        # when the last tube reach a determined x position
        # Change the number according to the difficulty you want to achieve
        # Bigger number will make the game more difficult
        if tubes[-1].x < 120: tubes.append(tubes_creation())
        for t in tubes:
            t.collision(bird, bird_x, bird_y)
        if not between_the_tubes:
            for t in tubes:
                if t.between_the_tubes(bird, bird_x):
                    between_the_tubes = True
                    break
        # When the bird is out of the tubes
        if between_the_tubes:
            between_the_tubes = False
            for t in tubes:
                if t.between_the_tubes(bird, bird_x):
                    between_the_tubes = True
                    break
            if not between_the_tubes:
                points += 1

        # 390 is the y value where the base begins
        # 0 in Pygame is the highest point
        if bird_y > 392:
            game_over()

        # Display's update
        draw_objects()
        update()
except:
    pass