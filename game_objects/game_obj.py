from typing import Any
import pygame
import random

from game_objects.assets.sprite_resolver import (
    object_sprite_resolver,
    PAPER,
    ROCK,
    SCISSOR,
)


class GameObj(pygame.sprite.Sprite):
    def __init__(
        self, sprite_group: pygame.sprite.Group, screen, object_type: str, stats: dict
    ) -> None:
        super().__init__()
        self.type = object_type
        self.sprite_group = sprite_group
        self.image = object_sprite_resolver[self.type]
        self.create_random_direction()
        self.rect = self.image.get_rect()
        self.screen = screen

        self.sprite_group.add(self)
        WIDTH, HEIGHT = self.screen.get_size()
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)
        self.stats = stats
        self.stats[self.type] += 1

    def create_random_direction(self):
        direction_choices = [
            1,
            -1,
        ]
        self.velocity = [
            random.choice(direction_choices),
            random.choice(direction_choices),
        ]

    def bounce(self, colliding_sprite):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]
        colliding_sprite.velocity[0] = -colliding_sprite.velocity[0]
        colliding_sprite.velocity[1] = -colliding_sprite.velocity[1]

    def update(self) -> None:
        collision = pygame.sprite.spritecollide(self, self.sprite_group, False)

        if collision:
            collider = collision[0]
            collider_type = collision[0].type
            if self.type != collider_type:
                if self.type == PAPER and collider_type == SCISSOR:
                    self.type = SCISSOR
                    self.stats[PAPER] -= 1
                    self.stats[SCISSOR] += 1
                if self.type == SCISSOR and collider_type == ROCK:
                    self.type = ROCK
                    self.stats[SCISSOR] -= 1
                    self.stats[ROCK] += 1
                if self.type == ROCK and collider_type == PAPER:
                    self.type = PAPER
                    self.stats[ROCK] -= 1
                    self.stats[PAPER] += 1
                if self.type == SCISSOR and collider_type == PAPER:
                    collider.type = SCISSOR
                    self.stats[PAPER] -= 1
                    self.stats[SCISSOR] += 1
                if self.type == ROCK and collider_type == SCISSOR:
                    collider.type = ROCK
                    self.stats[SCISSOR] -= 1
                    self.stats[ROCK] += 1
                if self.type == PAPER and collider_type == ROCK:
                    collider.type = PAPER
                    self.stats[ROCK] -= 1
                    self.stats[PAPER] += 1

                self.image = object_sprite_resolver[self.type]
                collider.image = object_sprite_resolver[collider.type]
                self.bounce(colliding_sprite=collision[0])

        WIDTH, HEIGHT = self.screen.get_size()
        if self.rect.x >= WIDTH or self.rect.x < 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y >= HEIGHT or self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
