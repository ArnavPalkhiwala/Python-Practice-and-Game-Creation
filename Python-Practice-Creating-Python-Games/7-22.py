import random

class BattleBot:
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.base_armor = 10
    self.base_damage = 10
    self.speed = 10
  
  def attack(self, opponent):
     damage_dealt = self.base_damage - (self.base_damage * (opponent.base_armor/100))
     opponent.take_damage(damage_dealt) 
    
  def take_damage(self, damage_dealt):
    self.health -= damage_dealt

  def build_attack(self):
    self.base_damage += 2
    self.base_armor -= 1
    self.speed -=1

  def build_armor(self):
    self.base_armor += 2
    self.base_damage -=1
    self.speed -=1

  def build_speed(self):
    self.speed += 2
    self.base_armor -= 1
    self.base_damage -= 1

  def is_alife(self):
    if self.health > 0:
      return True
    else:
      return False

  def get_stats(self):
    print("Name: " + self.name)
    print("Attack: " + str(self.base_damage))
    print("Defense: " + str(self.base_armor))
    print("Speed: " + str(self.speed))
    print("Health: " + str(self.health))

  def repair(self):
    self.health += (100-self.health) * .1

  def action(self, opponent):
    randomNum = random.randint(0, 100)
    if randomNum <= 25:
      self.build_attack()
    elif randomNum <= 38: 
      self.build_armor()
    elif randomNum <= 52:
      self.build_speed()
    elif randomNum <= 62:
      self.repair()
    elif randomNum <= 90:
      self.attack(opponent)
    else:
      print(self.name + " I was busy with something else")

