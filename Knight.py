import pygame

pygame.init()


class Knight(pygame.sprite.Sprite):
    # initiliazing
    def __init__(self, screen):
        super().__init__()
        self.knight_list = []
        self.knight_index = 0
        self.knight = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f0.png").convert_alpha()
        self.screen = screen
        self.knight_x = self.screen.get_width() / 2 - 24
        self.knight_y = self.screen.get_height() / 2 + 24
        self.sword_x = self.screen.get_width() / 2 + 24
        self.sword_y = self.screen.get_height() / 2 + 24

        # knight idle
        self.knight_idle_1 = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f0.png").convert_alpha()
        self.knight_idle_1 = pygame.transform.rotozoom(self.knight_idle_1, 0, 3)
        self.knight_idle_2 = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f1.png").convert_alpha()
        self.knight_idle_2 = pygame.transform.rotozoom(self.knight_idle_2, 0, 3)
        self.knight_idle_3 = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f2.png").convert_alpha()
        self.knight_idle_3 = pygame.transform.rotozoom(self.knight_idle_3, 0, 3)
        self.knight_idle_4 = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f3.png").convert_alpha()
        self.knight_idle_4 = pygame.transform.rotozoom(self.knight_idle_4, 0, 3)
        self.knight_idle_5 = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f4.png").convert_alpha()
        self.knight_idle_5 = pygame.transform.rotozoom(self.knight_idle_5, 0, 3)
        self.knight_idle_6 = pygame.image.load(".gitignore/assets/knight/idle/knight_idle_anim_f5.png").convert_alpha()
        self.knight_idle_6 = pygame.transform.rotozoom(self.knight_idle_6, 0, 3)
        self.knight_idle_list = [self.knight_idle_1, self.knight_idle_2, self.knight_idle_3, self.knight_idle_4,
                                 self.knight_idle_5, self.knight_idle_6]
        self.knight_idle = self.knight_idle_list[int(self.knight_index)]
        # knight run
        self.knight_run_1 = pygame.image.load(".gitignore/assets/knight/run/knight_run_anim_f0.png").convert_alpha()
        self.knight_run_1 = pygame.transform.rotozoom(self.knight_run_1, 0, 3)
        self.knight_run_2 = pygame.image.load(".gitignore/assets/knight/run/knight_run_anim_f1.png").convert_alpha()
        self.knight_run_2 = pygame.transform.rotozoom(self.knight_run_2, 0, 3)
        self.knight_run_3 = pygame.image.load(".gitignore/assets/knight/run/knight_run_anim_f2.png").convert_alpha()
        self.knight_run_3 = pygame.transform.rotozoom(self.knight_run_3, 0, 3)
        self.knight_run_4 = pygame.image.load(".gitignore/assets/knight/run/knight_run_anim_f3.png").convert_alpha()
        self.knight_run_4 = pygame.transform.rotozoom(self.knight_run_4, 0, 3)
        self.knight_run_5 = pygame.image.load(".gitignore/assets/knight/run/knight_run_anim_f4.png").convert_alpha()
        self.knight_run_5 = pygame.transform.rotozoom(self.knight_run_5, 0, 3)
        self.knight_run_6 = pygame.image.load(".gitignore/assets/knight/run/knight_run_anim_f5.png").convert_alpha()
        self.knight_run_6 = pygame.transform.rotozoom(self.knight_run_6, 0, 3)
        self.knight_run_list = [self.knight_run_1, self.knight_run_2, self.knight_run_3, self.knight_run_4,
                                self.knight_run_5, self.knight_run_6]
        self.knight_run = self.knight_run_list[int(self.knight_index)]
        # sword
        self.sword_1 = pygame.image.load(".gitignore/assets/knight/weapon/weapon_sword_1.png").convert_alpha()
        self.sword_1 = pygame.transform.rotozoom(self.sword_1, 0, 3)
        self.sword_2 = pygame.transform.rotozoom(self.sword_1, -45, 1)
        self.sword_3 = pygame.transform.rotozoom(self.sword_1, -45, 1)
        self.sword_list = [self.sword_1, self.sword_2, self.sword_3, self.sword_2]
        self.sword_index = 0
        self.sword = self.sword_list[int(self.sword_index)]
        # knight and sword rectangle
        self.knight_rect = pygame.rect.Rect((self.knight_x, self.knight_y), (48, 48))
        self.sword_rect = pygame.rect.Rect((self.sword_x, self.sword_y), (48, 48))
        # sound chanel and sound
        self.channel_3 = pygame.mixer.Channel(3)
        self.sword_sound = pygame.mixer.Sound(".gitignore/assets/sounds/air_cut.wav")

    # knight sprites in list
    def knight_display(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
            self.knight_list = self.knight_run_list
        else:
            self.knight_list = self.knight_idle_list
        self.knight = self.knight_list[int(self.knight_index)]

    # knight movement
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.knight_y += 3
            self.sword_y += 3
            self.knight_rect = pygame.rect.Rect((self.knight_x, self.knight_y), (48, 48))
            self.sword_rect = pygame.rect.Rect((self.sword_x, self.sword_y), (48, 48))
        elif keys[pygame.K_a]:
            self.knight_x -= 3
            self.sword_x -= 3
            self.knight_rect = pygame.rect.Rect((self.knight_x, self.knight_y), (48, 48))
            self.sword_rect = pygame.rect.Rect((self.sword_x, self.sword_y), (48, 48))
        elif keys[pygame.K_d]:
            self.knight_x += 3
            self.sword_x += 3
            self.knight_rect = pygame.rect.Rect((self.knight_x, self.knight_y), (48, 48))
            self.sword_rect = pygame.rect.Rect((self.sword_x, self.sword_y), (48, 48))
        elif keys[pygame.K_w]:
            self.knight_y -= 3
            self.sword_y -= 3
            self.knight_rect = pygame.rect.Rect((self.knight_x, self.knight_y), (48, 48))
            self.sword_rect = pygame.rect.Rect((self.sword_x, self.sword_y), (48, 48))

    # knight animation
    def knight_animation(self):
        self.knight_index += 0.1
        self.knight_display()
        self.screen.blit(self.knight, self.knight_rect)
        if self.knight_index >= len(self.knight_list) - 1:
            self.knight_index = 0

    # sword animation
    def sword_animation(self):
        mouse_button = pygame.mouse.get_pressed(3)
        self.sword_index += 0.1
        if self.sword_index >= len(self.sword_list) - 1:
            self.sword_index = 0
        if mouse_button == (1, 0, 0):
            self.sword = self.sword_list[int(self.sword_index)]
            self.screen.blit(self.sword, self.sword_rect)
            self.channel_3.play(self.sword_sound)
        self.sword = self.sword_1

    # override update
    def update(self):
        self.movement()
        self.knight_animation()
        self.sword_animation()
