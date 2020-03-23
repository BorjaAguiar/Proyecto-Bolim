import pygame

class P1(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('..\Arte\Grafico\Sprites\p1walk.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 44, 57))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (8, 64, 36, 51), 1: (72, 64, 36, 51), 2: (136, 64, 36, 51), 3: (200, 64, 36, 51), 4: (264, 64, 36, 51), 5: (328, 64, 36, 51), 6: (392, 64, 36, 51), 7: (456, 64, 36, 51), 8: (520, 64, 36, 51) }
        self.right_states = { 0: (0, 192, 36, 51), 1: (64, 192, 36, 51), 2: (128, 192, 36, 51), 3: (192, 192, 36, 51), 4: (256, 192, 36, 51), 5: (320, 192, 36, 51), 6: (384, 192, 36, 51), 7: (448, 192, 36, 51), 8: (512, 192, 36, 51) }
        self.up_states = { 0: (7, 0, 30, 52), 1: (71, 0, 30, 52), 2: (135, 0, 30, 52), 3: (199, 0, 30, 52), 4: (263, 0, 30, 52), 5: (327, 0, 30, 52), 6: (391, 0, 30, 52), 7: (456, 0, 30, 52), 8: (519, 0, 30, 52) }
        self.down_states = { 0: (7, 123, 30, 57), 1: (71, 123, 30, 57), 2: (135, 123, 30, 57), 3: (200, 123, 30, 57), 4: (263, 123, 30, 57), 5: (327, 123, 30, 57), 6: (391, 123, 30, 57), 7: (455, 123, 30, 57), 8: (519, 123, 30, 57) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 10
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 10
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 10
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 10

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                self.update('left')
            if event.key == pygame.K_d:
                self.update('right')
            if event.key == pygame.K_w:
                self.update('up')
            if event.key == pygame.K_s:
                self.update('down')

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                self.update('stand_left')
            if event.key == pygame.K_d:
                self.update('stand_right')
            if event.key == pygame.K_w:
                self.update('stand_up')
            if event.key == pygame.K_s:
                self.update('stand_down')