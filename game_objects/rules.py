import pygame
from game_objects.assets.sprite_resolver import object_sprite_resolver, RULES


class RulesObj(pygame.sprite.Sprite):
    def __init__(self, sprite_group):
        super().__init__()

        self.sprite_group = sprite_group
        self.image = object_sprite_resolver[RULES]
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 200

    def update(self) -> None:
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y
