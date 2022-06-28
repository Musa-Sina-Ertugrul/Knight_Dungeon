#!/usr/bin/env python3
import pygame
import sys
from Knight import Knight
from Enemies import Enemies
import random

# initiliazing
pygame.init()
screen = pygame.display.set_mode((960, 960))
pygame.display.set_caption("Knight Dungeon")
knight = Knight(screen)
clock = pygame.time.Clock()
bg = pygame.image.load("assets/bg-tile/floor_1.png")
bg = pygame.transform.rotozoom(bg, 0, 3)
text_font = pygame.font.Font(None, 50)
death_sound = pygame.mixer.Sound("assets/sounds/got-hit.wav")
bg_size = 48
bg_column = 20
score = 0
game_active = False
channel_1 = pygame.mixer.Channel(1)
channel_2 = pygame.mixer.Channel(2)
bg_music = pygame.mixer.Sound("assets/sounds/bg-song.wav")

# music
channel_1.play(bg_music, -1)

# enemy death
enemy_list = []


def enemy_death():
    global score
    for enemy in enemy_list:
        if enemy.enemy_rect.colliderect(knight.sword_rect):
            enemy_list.remove(enemy)
            score += 1


# knight death
def knight_death():
    global game_active
    for enemy in enemy_list:
        if enemy.enemy_rect.colliderect(knight.knight_rect):
            game_active = False
            enemy_list.clear()
            channel_2.play(death_sound)


# main loop
while True:

    # x button for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # kill to swing sword
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            enemy_death()
        # starts game
        if event.type == pygame.KEYDOWN:
            game_active = True
    # setting background
    for row in range(bg_column):
        for column in range(bg_column):
            bg_rect = bg.get_rect(topleft=(bg_size * row, bg_size * column))
            screen.blit(bg, bg_rect)

    # screen of game
    if game_active:
        # setting enemies
        new_enemy = Enemies(random.randint(0, 2), knight, screen)
        if len(enemy_list) < 20:
            enemy_list.append(new_enemy)

        # drawing enemies
        for enemy in enemy_list:
            screen.blit(enemy.enemy, enemy.enemy_rect)
            enemy.update()
        knight_death()
        knight.update()
        score_text = text_font.render("Score: {}".format(str(score)), True, "White")
        score_text_rect = score_text.get_rect(center=(960 / 2, 100))
        screen.blit(score_text, score_text_rect)
    # game start and game end screen
    else:
        game_start_text = text_font.render("To start game press any key", True, "White")
        game_start_text_rect = game_start_text.get_rect(center=(960 / 2, 960 / 2))
        screen.blit(game_start_text, game_start_text_rect)

    clock.tick(60)
    pygame.display.update()
