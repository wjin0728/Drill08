from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 500), 90
        self.frame = random.randint(0,7)
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = 599
        self.speed = random.randint(5, 30)
        size = random.randint(0, 1)
        if size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 60:
            self.y -= self.speed
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)


def reset_world():
    global running
    global grass
    global boy
    global team
    global world

    running = True
    world = [Grass()]
    team = [Boy() for i in range(11)]
    balls = [Ball() for i in range(21)]
    world += team
    world += balls


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_world():
    for object in world:
        object.update()
    pass


def render_world():
    clear_canvas()
    for object in world:
        object.draw()
    update_canvas()


# initialization code

# game main loop code

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
