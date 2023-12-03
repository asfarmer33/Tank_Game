import pygame
class Music():

    def __init__(self):
        self.level = 0
        self.old_level = 0
        self.song = pygame.mixer.Sound("sounds/background_music.wav")
        self.song_time = 0

    def update(self, level):
        self.level = level
        if self.level != self.old_level: # if the menu changes stop the previous music
            self.song.fadeout(500)
            self.song_time = 0
        if self.level == 0: # for main menu
            if self.song_time == 0 or pygame.time.get_ticks() - self.song_time > 168000:
                self.song.fadeout(500)
                self.song = pygame.mixer.Sound("sounds/main_music.wav")
                self.song.set_volume(0.1)
                self.song.play()
                self.song_time = pygame.time.get_ticks()
        if self.level == 1 or self.level == 51: # for level select menu
            if self.song_time == 0 or pygame.time.get_ticks() - self.song_time > 87000:
                self.song.fadeout(500)
                self.song = pygame.mixer.Sound("sounds/level_music.wav")
                self.song.set_volume(0.1)
                self.song.play()
                self.song_time = pygame.time.get_ticks()
        if self.level > 1 and self.level < 50 and self.level != 12: # for one player levels
            if self.song_time == 0 or pygame.time.get_ticks() - self.song_time > 60000:
                self.song.fadeout(500)
                self.song = pygame.mixer.Sound("sounds/background_music.wav")
                self.song.set_volume(0.3)
                self.song.play()
                self.song_time = pygame.time.get_ticks()
        if self.level > 51 and self.level < 62: # for two player levels
            if self.song_time == 0 or pygame.time.get_ticks() - self.song_time > 60000:
                self.song.fadeout(500)
                self.song = pygame.mixer.Sound("sounds/background_music.wav")
                self.song.set_volume(0.3)
                self.song.play()
                self.song_time = pygame.time.get_ticks()
        if self.level == 12 or self.level == 62: # for bonus level
            if self.song_time == 0 or pygame.time.get_ticks() - self.song_time > 126000:
                self.song.fadeout(500)
                self.song = pygame.mixer.Sound("sounds/11_music.wav")
                self.song.set_volume(0.5)
                self.song.play()
                self.song_time = pygame.time.get_ticks()
        if self.level == 100: # for save menu
            if self.song_time == 0 or pygame.time.get_ticks() - self.song_time > 90000:
                self.song.fadeout(500)
                self.song = pygame.mixer.Sound("sounds/save_music.wav")
                self.song.set_volume(0.1)
                self.song.play()
                self.song_time = pygame.time.get_ticks()
        self.old_level = self.level

    def stop(self):
        self.song.stop()
