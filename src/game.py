#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function #UNIX systems : Disable default print function

import io
import os
import random
import sys

import data



#######################
# CLASS : CURRENTUNIT #
#######################
"""
__CURRENTUNIT__
{Inherited from UNIT [data] :
	__ID
	name
	division
	cost
	fire_range //Weapon 1 only. Weapon 2 has always (1,1) (direct).
	counter_range //Weapon 1 only. Weapon 2 has always (1,1) (direct).
	max_movement_to_fire //Weapon 1 only. Weapon 2 has always x >= movement.
	movement
	movement_type
	vision
	weapon_1_name
	weapon_2_name
	base_ammo //Weapon 1 only. Weapon 2 has always infinite.
	base_fuel
	properties
}
health
max_ammo //Weapon 1 only.
max_fuel
rank
is_CO_unit
CO_owner ???
ammo //Weapon 1 only.
fuel
att_mult
def_mult
"""
class CurrentUnit:
	def __init__(self, unit, health=100, base_ammo=9, base_fuel=99, rank=0, is_co_unit=False, ammo=9, fuel=99, att_mult=1, def_mult=1, default=False, manual=None):

		#self.__dict__ = Unit.__dict__.copy() ????
		self.unit = unit
		if default:
			"""Create one object with the default parameters"""
			self.health = 100
			self.base_ammo = 9
			self.base_fuel = 99
			self.rank = 0
			self.is_co_unit = False
			self.ammo = 9
			self.fuel = 99
			self.att_mult = 1
			self.def_mult = 1

		elif manual is None:
			"""Create one object with the set parameters"""
			self.health = 100
			self.base_ammo = 9
			self.base_fuel = 99
			self.rank = 0
			self.is_co_unit = False
			self.ammo = 9
			self.fuel = 99
			self.att_mult = 1
			self.def_mult = 1
		else:
			"""Create one object manually"""
			print("Unit max health? (int)")
			self.health = input()
			print("Base ammo? (int)")
			self.base_ammo = input()
			print("Base fuel? (int)")
			self.base_fuel = input()
			print("Rank? (int)")
			self.rank = input()
			print("Is CO unit? (bool)")
			self.is_co_unit = input()
			print("Current ammo? (int)")
			self.ammo = input()
			print("Current fuel? (int)")
			self.fuel = input()
			print("ATT mult? (int)")
			self.att_mult = input()
			print("DEF mult? (int)")
			self.def_mult = input()


	def __getattr__(self, attr):
		try:
	    		return getattr(self.unit, attr)
		except AttributeError:
	    		return NULL



#####################
# CLASS : CURRENTCO #
#####################
"""
__CURRENTCO__
{ Inherited from CO [data] :
	__ID
	name
	CO_zone_type {Increase, Fixed, Global} //TODO : Solution pour Klaus qui remplit à partir des bâtiments
	CO_zone_size //Ne mettre que la taille minimum. Optionnel si TypeCOZone == Infinie car considéré à un nombre très grand, plus grand que la longueur max d'une map.
	effect
	has_CO_power
	CO_power
	has_SCO_power
	SCO_power
}
player //Number
army ???
CO_power_jauge //Number of bars
CO_power_status {0=None, 1="COP", 2="SCOP"}
.............

"""
class CurrentCO():

	def __init__(self, co, player=0, army="None", co_power_jauge=0, co_power_status=0, default=False, manual=None):
		self.co = co
		if default:
			"""Create one object with the default parameters"""
			self.player = 0
			self.army = "None"
			self.co_power_jauge = 0
			self.co_power_status = 0

		elif manual is None:
			"""Create one object with the set parameters"""
			self.player = player
			self.army = army
			self.co_power_jauge = co_power_jauge
			self.co_power_status = co_power_status

		else:
			"""Create one object manually"""
			print("Player N°? (int)")
			self.player = input()
			print("Army? (String)")
			self.army = input()
			print("CO power jauge? (int)")
			self.co_power_jauge = input()
			print("CO power status? (int)")
			self.co_power_status = input()

	def __getattr__(self, attr):
		try:
	    		return getattr(self.co, attr)
		except AttributeError:
	    		return NULL



######################
# CLASS : CURRENTMAP #
######################
"""
[Map data probably loaded from file]
height
length
terrain_list

rules {Dictionary]
turn
current_climate
"""
class CurrentMap:

	def __init__(self):
		pass

