import pygame
from core.settings import SCALE

images = {} # 이미지 모아두는 딕셔너리

def load(path : str, scale : float = SCALE) -> pygame.Surface:
    key = (path, scale)

    if key in images:
        return images[key]
    image = pygame.image.load(path).convert_alpha()
    width, height = image.get_size()
    scaled_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

    images[key] = scaled_image
    return scaled_image