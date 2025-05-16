import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0

    def add_score(self, amount):
        self.score += amount

    def draw(self, screen):
        font = pygame.font.Font("Roboto-Bold.ttf", 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))