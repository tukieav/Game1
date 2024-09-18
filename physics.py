from player import Player
from enemies import Enemies
class Physics:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def check_collisions (self, player, enemies):
        for enemies in enemies:
            if (player.player_x < enemies.enemy[0] < player.player_x + player.player_size or player.player_x < enemies.enemy[0] + enemies.enemy_size < player.player_x + player.player_size):
                return True
        return False
