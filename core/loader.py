import pygame
from core.settings import SCALE

def load(path : str, scale : float = SCALE) -> pygame.Surface:
    image = pygame.image.load(path).convert_alpha()
    width, height = image.get_size()
    scaled_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    return scaled_image