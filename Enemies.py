import random

import pygame

pygame.init()


class Enemies(pygame.sprite.Sprite):
    # initiliazing
    def __init__(self, enemy, knight, screen):
        super().__init__()
        self.screen = screen
        self.enemy_list = []
        self.enemy_index = 0
        self.knight = knight
        self.enemy_x = 48 * random.randint(15, 19)
        self.enemy_y = 48 * random.randint(0, 19)
        self.enemy = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f0.png").convert_alpha()
        if enemy == 1:
            self.enemy_1 = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f0.png").convert_alpha()
            self.enemy_1 = pygame.transform.rotozoom(self.enemy_1, 0, 3)
            self.enemy_2 = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f1.png").convert_alpha()
            self.enemy_2 = pygame.transform.rotozoom(self.enemy_2, 0, 3)
            self.enemy_3 = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f2.png").convert_alpha()
            self.enemy_3 = pygame.transform.rotozoom(self.enemy_3, 0, 3)
            self.enemy_4 = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f3.png").convert_alpha()
            self.enemy_4 = pygame.transform.rotozoom(self.enemy_4, 0, 3)
            self.enemy_5 = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f4.png").convert_alpha()
            self.enemy_5 = pygame.transform.rotozoom(self.enemy_5, 0, 3)
            self.enemy_6 = pygame.image.load(".gitignore/assets/enemies/slime/slime_run_anim_f5.png").convert_alpha()
            self.enemy_6 = pygame.transform.rotozoom(self.enemy_6, 0, 3)
            self.enemy_list = [self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4, self.enemy_4, self.enemy_5]

        else:
            self.enemy_1 = pygame.image.load(
                ".gitignore/assets/enemies/flying-creature/fly_anim_f0.png").convert_alpha()
            self.enemy_1 = pygame.transform.rotozoom(self.enemy_1, 0, 3)
            self.enemy_2 = pygame.image.load(
                ".gitignore/assets/enemies/flying-creature/fly_anim_f1.png").convert_alpha()
            self.enemy_2 = pygame.transform.rotozoom(self.enemy_2, 0, 3)
            self.enemy_3 = pygame.image.load(
                ".gitignore/assets/enemies/flying-creature/fly_anim_f2.png").convert_alpha()
            self.enemy_3 = pygame.transform.rotozoom(self.enemy_3, 0, 3)
            self.enemy_4 = pygame.image.load(
                ".gitignore/assets/enemies/flying-creature/fly_anim_f3.png").convert_alpha()
            self.enemy_4 = pygame.transform.rotozoom(self.enemy_4, 0, 3)
            self.enemy_list = [self.enemy_1, self.enemy_2, self.enemy_3, self.enemy_4]

        # enemy rectangle
        self.enemy_rect = self.enemy.get_rect(topleft=(self.enemy_x, self.enemy_y))

    # enemy animation
    def enemy_animation(self):
        self.enemy_index += 0.1
        if self.enemy_index >= len(self.enemy_list) - 1:
            self.enemy_index = 0
        self.enemy = self.enemy_list[int(self.enemy_index)]

    # movement logic of enemies , they track knight
    def movement(self):
        if self.enemy_x > self.knight.knight_x and self.enemy_y < self.knight.knight_y:
            dx = self.enemy_x - self.knight.knight_x
            dy = self.knight.knight_y - self.enemy_y
            dx /= 99
            dy /= 99
            self.enemy_x -= dx
            self.enemy_y += dy
            self.enemy_rect = self.enemy.get_rect(topleft=(self.enemy_x, self.enemy_y))
        elif self.enemy_x > self.knight.knight_x and self.enemy_y > self.knight.knight_y:
            dx = self.enemy_x - self.knight.knight_x
            dy = self.enemy_y - self.knight.knight_y
            dx /= 99
            dy /= 99
            self.enemy_x -= dx
            self.enemy_y -= dy
            self.enemy_rect = self.enemy.get_rect(topleft=(self.enemy_x, self.enemy_y))
        elif self.enemy_x < self.knight.knight_x and self.enemy_y > self.knight.knight_y:
            dx = self.enemy_x - self.knight.knight_x
            dy = self.enemy_y - self.knight.knight_y
            dx /= 99
            dy /= 99
            self.enemy_x -= dx
            self.enemy_y -= dy
            self.enemy_rect = self.enemy.get_rect(topleft=(self.enemy_x, self.enemy_y))
        elif self.enemy_x < self.knight.knight_x and self.enemy_y < self.knight.knight_y:
            dx = self.enemy_x - self.knight.knight_x
            dy = self.enemy_y - self.knight.knight_y
            dx /= 99
            dy /= 99
            self.enemy_x -= dx
            self.enemy_y -= dy
            self.enemy_rect = self.enemy.get_rect(topleft=(self.enemy_x, self.enemy_y))

        self.enemy_rect = self.enemy.get_rect(topleft=(self.enemy_x, self.enemy_y))

    # override update method
    def update(self):
        super().update()
        self.enemy_animation()
        self.movement()
