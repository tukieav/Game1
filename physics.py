from player import Player
from enemies import Enemies
from weapons import Weapons



class Physics:
    def __init__(self, player, enemies, weapon, bullet):
        self.player = player
        self.enemies = enemies
        self.weapon = weapon
        self.bullet = bullet


    def check_collisions(self, player, enemies):
        for enemy in enemies:
            if (player.player_x < enemy[0] + self.enemies.enemy_size and
                player.player_x + player.size > enemy[0] and
                player.player_y < enemy[1] + self.enemies.enemy_size and
                player.player_y + player.size > enemy[1]):
                player.points += 1
                player.health -= 10
                enemies.remove(enemy)
                if player.health <= 0:
                    return True
        return False
    
    def hit_by_bullet(self, enemies, weapon):
        for bullet in weapon.bullets:
            for enemy in enemies:
                if (bullet[0] < enemy[0] + self.enemies.enemy_size and
                    bullet[0] + weapon.size > enemy[0] and
                    bullet[1] < enemy[1] + self.enemies.enemy_size and
                    bullet[1] + weapon.size > enemy[1]):
                    enemies.remove(enemy)
                    weapon.bullets.remove(bullet)
                    self.player.points += 1
                    break
