import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            pygame.sprite.Sprite.__init__(self, self.containers)
        else:
            pygame.sprite.Sprite.__init__(self)
        self.score = 0
        
    def update(self, dt):
        pass  # No need to update the score here, it's updated directly

    def draw(self, screen):
        font = pygame.font.SysFont(None, 36)  # Use default system font
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))