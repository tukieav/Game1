from player import Player
from enemies import Enemies
class Physics:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def check_collisions(self, player, enemies):
        for enemy in enemies:
            if (player.player_x < enemy[0] + self.enemies.enemy_size and
                player.player_x + player.size > enemy[0] and
                player.player_y < enemy[1] + self.enemies.enemy_size and
                player.player_y + player.size > enemy[1]):
                return True
        return False
