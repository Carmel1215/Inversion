import os
from core.loader import load

# Player
BLACK_PLAYER_IDLE_FRONT = []
BLACK_PLAYER_IDLE_BACK = []
BLACK_PLAYER_IDLE_LEFT = []
BLACK_PLAYER_IDLE_RIGHT = []

BLACK_PLAYER_WALK_FRONT = []
BLACK_PLAYER_WALK_BACK = []
BLACK_PLAYER_WALK_LEFT = []
BLACK_PLAYER_WALK_RIGHT = []

WHITE_PLAYER_IDLE_FRONT = []
WHITE_PLAYER_IDLE_BACK = []
WHITE_PLAYER_IDLE_LEFT = []
WHITE_PLAYER_IDLE_RIGHT = []

WHITE_PLAYER_WALK_FRONT = []
WHITE_PLAYER_WALK_BACK = []
WHITE_PLAYER_WALK_LEFT = []
WHITE_PLAYER_WALK_RIGHT = []

# UI
START_BUTTON_IDLE, START_BUTTON_CLICKED = None, None
QUIT_BUTTON_IDLE, QUIT_BUTTON_CLICKED = None, None

def load_assets():
    global BLACK_PLAYER_IDLE_FRONT, BLACK_PLAYER_IDLE_BACK, BLACK_PLAYER_IDLE_LEFT, BLACK_PLAYER_IDLE_RIGHT
    global BLACK_PLAYER_WALK_FRONT, BLACK_PLAYER_WALK_BACK, BLACK_PLAYER_WALK_LEFT, BLACK_PLAYER_WALK_RIGHT
    global WHITE_PLAYER_IDLE_FRONT, WHITE_PLAYER_IDLE_BACK, WHITE_PLAYER_IDLE_LEFT, WHITE_PLAYER_IDLE_RIGHT
    global WHITE_PLAYER_WALK_FRONT, WHITE_PLAYER_WALK_BACK, WHITE_PLAYER_WALK_LEFT, WHITE_PLAYER_WALK_RIGHT
    global START_BUTTON_IDLE, START_BUTTON_CLICKED
    global QUIT_BUTTON_IDLE, QUIT_BUTTON_CLICKED

    BLACK_PLAYER_IDLE_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleFront', f'IdleFront{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_IDLE_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleBack', f'IdleBack{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_IDLE_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleLeft', f'IdleLeft{i}.png'))
        for i in range(1, 3)
    ]

    BLACK_PLAYER_IDLE_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleRight', f'IdleRight{i}.png'))
        for i in range(1, 3)
    ]

    BLACK_PLAYER_WALK_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkFront', f'WalkFront{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_WALK_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkBack', f'WalkBack{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_WALK_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkLeft', f'WalkLeft{i}.png'))
        for i in range(1, 9)
    ]

    BLACK_PLAYER_WALK_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkRight', f'WalkRight{i}.png'))
        for i in range(1, 9)
    ]

    WHITE_PLAYER_IDLE_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleFront', f'IdleFront{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_IDLE_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleBack', f'IdleBack{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_IDLE_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleLeft', f'IdleLeft{i}.png'))
        for i in range(1, 3)
    ]

    WHITE_PLAYER_IDLE_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleRight', f'IdleRight{i}.png'))
        for i in range(1, 3)
    ]

    WHITE_PLAYER_WALK_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkFront', f'WalkFront{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_WALK_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkBack', f'WalkBack{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_WALK_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkLeft', f'WalkLeft{i}.png'))
        for i in range(1, 9)
    ]

    WHITE_PLAYER_WALK_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkRight', f'WalkRight{i}.png'))
        for i in range(1, 9)
    ]

    START_BUTTON_IDLE = load(os.path.join('assets', 'images', 'UI', 'Button', 'Start', 'Start1.png'))
    START_BUTTON_CLICKED = load(os.path.join('assets', 'images', 'UI', 'Button', 'Start', 'Start2.png'))

    QUIT_BUTTON_IDLE = load(os.path.join('assets', 'images', 'UI', 'Button', 'Quit', 'Quit1.png'))
    QUIT_BUTTON_CLICKED = load(os.path.join('assets', 'images', 'UI', 'Button', 'Quit', 'Quit2.png'))