from player import Player
from enemies import Enemies, LargeEnemy
from weapons import Weapons

class Physics:
    def __init__(self, player, enemies, weapon, bullet):
        self.player = player
        self.enemies = enemies
        self.weapon = weapon
        self.bullet = bullet


    def hit_by_bullet(self, enemies, weapon):
        for bullet in weapon.bullets:
            for enemy in enemies:
                if (bullet[0] < enemy[0] + enemy[3] and
                    bullet[0] + weapon.size > enemy[0] and
                    bullet[1] < enemy[1] + enemy[3] and
                    bullet[1] + weapon.size > enemy[1]):
                    enemy[2] -= weapon.fire_power
                    if enemy[2] <= 0:
                        if enemy[3] == 60:  # Sprawdź, czy to duży wróg
                            enemies.remove(enemy)
                            self.player.points += 5

                        else:
                            enemies.remove(enemy)
                            self.player.points += 1
                    weapon.bullets.remove(bullet)
                    break

    def check_collisions(self, player, enemies):
        for enemy in enemies:
            if (player.player_x < enemy[0] + enemy[3] and
                player.player_x + player.size > enemy[0] and
                player.player_y < enemy[1] + enemy[3] and
                player.player_y + player.size > enemy[1]):
                if enemy[3] == 60:
                    player.health -= 50
                    enemies.remove(enemy)
                    self.player.points += 5
                else:
                    player.health -= 10
                    enemies.remove(enemy)
                    self.player.points += 1
                if player.health <= 0:
                    return True
        return False