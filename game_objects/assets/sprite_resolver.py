import os
import pygame
from typing import Callable, Dict

SCISSOR = "SCISSOR"
PAPER = "PAPER"
ROCK = "ROCK"
RULES = "RULES"

_scissor = pygame.transform.scale(
    pygame.image.load("./game_objects/assets/scissor.png"), (15, 15)
)
_paper = pygame.transform.scale(
    pygame.image.load("./game_objects/assets/paper.png"), (15, 15)
)
_rock = pygame.transform.scale(
    pygame.image.load("./game_objects/assets/rock.png"), (15, 15)
)
_rules = pygame.image.load("./game_objects/assets/rules.png")


object_sprite_resolver: Dict[str, pygame.Surface] = {
    SCISSOR: _scissor,
    PAPER: _paper,
    ROCK: _rock,
    RULES: _rules,
}
