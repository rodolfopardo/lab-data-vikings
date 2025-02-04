#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:51:50 2019

@author: Luis Gallo / Rodolfo Pardo
"""
# Soldier
#Declaro clase Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self): 
        return self.strength
   
    def receive_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        
        

# Viking
#Declaro clase Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name
    
    def attack(self): 
        return self.strength
    
    def receive_damage(self, damage): 
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f'{self.name} has received {self.damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
#Declaro clase Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self): 
        return self.strength
    
    def receive_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"




class War:
    vikingArmy = []
    saxonArmy = []
    def __init__(self):
        vikingArmy = []
        saxonArmy = []
    def add_viking(Viking):
        vikingArmy.append(self.strength)
    def add_saxon(self):
        saxonArmy.append(self.strength)
    def viking_attack():
        sax.receive_damage(gabriel.attack())
    def saxon_attack():
        gabriel.receive_damage(sax.attack())
    def show_status():
        if saxonArmy == 0:
            return "Vikings have won the war of the century!"
        elif VikingArmy == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif saxonArmy == 1 and VikingArmy == 1: 
            return "Vikings and Saxons are still in the thick of battle."
    
    

#soldado = Soldier(100, 60)
#gabriel = Viking("Gabriel", 100, 10)
#sax = Saxon(100, 60)


    
