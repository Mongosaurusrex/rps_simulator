import pygame
from game_objects.game_obj import GameObj
from game_objects.rules import RulesObj
from game_objects.assets.sprite_resolver import (
    SCISSOR,
    ROCK,
    PAPER,
    RULES,
    object_sprite_resolver,
)

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)

WIDTH = 1000
HEIGHT = 600
SCREEN_RES = (WIDTH, HEIGHT)
pygame.display.set_caption("Rock paper scissors sim")
screen = pygame.display.set_mode(SCREEN_RES)

RED = (255, 0, 0)
GRAY = (120, 120, 120)

display_sprite_group: pygame.sprite.Group = pygame.sprite.Group()
rules_obj = RulesObj(sprite_group=display_sprite_group)

game_obj_sprite_group: pygame.sprite.Group = pygame.sprite.Group()

stats = {SCISSOR: 0, PAPER: 0, ROCK: 0}

for amount_of_spawns in range(200):
    GameObj(
        sprite_group=game_obj_sprite_group,
        screen=screen,
        object_type=SCISSOR,
        stats=stats,
    )
    GameObj(
        sprite_group=game_obj_sprite_group, screen=screen, object_type=ROCK, stats=stats
    )
    GameObj(
        sprite_group=game_obj_sprite_group,
        screen=screen,
        object_type=PAPER,
        stats=stats,
    )


def show_results():
    rock_surface = my_font.render(f"Rocks: {stats[ROCK]}", False, (0, 0, 0))
    paper_surface = my_font.render(f"Papers: {stats[PAPER]}", False, (0, 0, 0))
    scissor_surface = my_font.render(f"Scissors: {stats[SCISSOR]}", False, (0, 0, 0))
    total_surface = my_font.render(
        f"Total: {stats[SCISSOR] + stats[PAPER] + stats[ROCK]}", False, (0, 0, 0)
    )
    screen.blit(rock_surface, (0, 0))
    screen.blit(paper_surface, (0, 30))
    screen.blit(scissor_surface, (0, 60))
    screen.blit(total_surface, (0, 90))


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(GRAY)

    display_sprite_group.update()
    display_sprite_group.draw(screen)
    game_obj_sprite_group.update()
    game_obj_sprite_group.draw(screen)
    show_results()
    pygame.display.flip()
