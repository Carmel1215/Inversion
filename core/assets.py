import os
from core.loader import load

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

def load_assets():
    global BLACK_PLAYER_IDLE_FRONT, BLACK_PLAYER_IDLE_BACK, BLACK_PLAYER_IDLE_LEFT, BLACK_PLAYER_IDLE_RIGHT
    global BLACK_PLAYER_WALK_FRONT, BLACK_PLAYER_WALK_BACK, BLACK_PLAYER_WALK_LEFT, BLACK_PLAYER_WALK_RIGHT
    global WHITE_PLAYER_IDLE_FRONT, WHITE_PLAYER_IDLE_BACK, WHITE_PLAYER_IDLE_LEFT, WHITE_PLAYER_IDLE_RIGHT
    global WHITE_PLAYER_WALK_FRONT, WHITE_PLAYER_WALK_BACK, WHITE_PLAYER_WALK_LEFT, WHITE_PLAYER_WALK_RIGHT

    BLACK_PLAYER_IDLE_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleFront', f'BlackIdleFront{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_IDLE_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleBack', f'BlackIdleBack{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_IDLE_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleLeft', f'BlackIdleLeft{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_IDLE_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'IdleRight', f'BlackIdleRight{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_WALK_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkFront', f'BlackWalkFront{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_WALK_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkBack', f'BlackWalkBack{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_WALK_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkLeft', f'BlackWalkLeft{i}.png'))
        for i in range(1, 5)
    ]

    BLACK_PLAYER_WALK_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'Black', 'WalkRight', f'BlackWalkRight{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_IDLE_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleFront', f'WhiteIdleFront{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_IDLE_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleBack', f'WhiteIdleBack{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_IDLE_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleLeft', f'WhiteIdleLeft{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_IDLE_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'IdleRight', f'WhiteIdleRight{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_WALK_FRONT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkFront', f'WhiteWalkFront{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_WALK_BACK = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkBack', f'WhiteWalkBack{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_WALK_LEFT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkLeft', f'WhiteWalkLeft{i}.png'))
        for i in range(1, 5)
    ]

    WHITE_PLAYER_WALK_RIGHT = [
        load(os.path.join('assets', 'images', 'Player', 'White', 'WalkRight', f'WhiteWalkRight{i}.png'))
        for i in range(1, 5)
    ]