#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function #UNIX systems : Disable default print function

import io
import os
import random
import sys




####################
# GLOBAL CONSTANTS #
####################

"""
damage_chart=DEF_DC,
damage_chart_indexes=DEF_DCI, 
movement_chart=DEF_MC,
movement_chart_indexes=DEF_MCI, 
movement_type_list=DEF_MTL,
"""
DEF_DC = []
DEF_DCI = []
DEF_MC = []
DEF_MCI = []
DEF_MTL = []


#######################
# CLASS : UNIT (data) #
#######################
"""
__UNIT__ [Data]
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
weapon_code // 0=No weapon. 1|2=Weapon 1 or 2. 3=Both weapons.
weapon_1_name
weapon_2_name
base_ammo //Weapon 1 only. Weapon 2 has always infinite.
base_fuel
base_fuel_consumption
properties
"""
class Unit: #[DATA]
	def __init__(self, name="Default", division="Land", cost=0, fire_range=(1,1),
			counter_range=(1,1), max_movement_to_fire=99, movement=1,
			movement_type="Infantry", vision=1, weapon_code=2, weapon_1_name="One",
			weapon_2_name="Two", base_ammo=0, base_fuel=99, properties=[],
			default=False, manual=False):

		if default:
			"""Create one object with the default parameters"""
			self.name = "Default"
			self.division = "Land"
			self.cost = 0
			self.fire_range = (1,1)
			self.counter_range = (1,1)
			self.max_movement_to_fire = 99
			self.movement = 1
			self.movement_type = "Infantry"
			self.vision = 1
			self.weapon_code = 2
			self.weapon_1_name = "One"
			self.weapon_2_name = "Two"
			self.base_ammo = 0
			self.base_fuel = 99
			self.properties = []


		elif manual is False:
			"""Create one object with the set parameters"""
			self.name = name
			self.division = division
			self.cost = cost
			self.fire_range = fire_range
			self.counter_range = counter_range
			self.max_movement_to_fire = max_movement_to_fire
			self.movement = movement
			self.movement_type = movement_type
			self.vision = vision
			self.weapon_code = weapon_code
			self.weapon_1_name = weapon_1_name
			self.weapon_2_name = weapon_2_name
			self.base_ammo = base_ammo
			self.base_fuel = base_fuel
			self.properties = properties

		else:
			"""Create one object manually"""
			print("Name? (String)")
			self.name = input()
			print("Division? (String)")
			self.division = input()
			print("Cost? (int)")
			self.cost = input()
			print("Fire range (attacking)? ((int,int))")
			self.fire_range = input()
			print("Counter range (counterattacking)? ((int,int))")
			self.counter_range = input()
			print("Max movement to fire ? (int)")
			self.max_movement_to_fire = input()
			print("Movement? (int)")
			self.movement = input()
			print("MovementType? (String)")
			self.movement_type = input()
			print("Vision? (int)")
			self.vision = input()
			print("Weapons? (int) 0=None, 3=Both")
			self.weapon_code = weapon_code
			print("Weapon_1_name? (int)")
			self.weapon_1_name = weapon_1_name
			print("Weapon_2_name? (int)")
			self.weapon_2_name = weapon_2_name
			print("Base ammo for Weapon_1? (int)")
			self.base_ammo = base_ammo
			print("Base_fuel? (int)")
			self.base_fuel = base_fuel
			print("Other properties? (list of String)")
			self.properties = input()



	def setParam(self, name, division, cost, fire_range, counter_range, max_movement_to_fire, movement, movement_type, vision, weapon_code, weapon_1_name, weapon_2_name, base_ammo, base_fuel, properties):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.name = name
		self.division = division
		self.cost = cost
		self.fire_range = fire_range
		self.counter_range = counter_range
		self.max_movement_to_fire = max_movement_to_fire
		self.movement = movement
		self.movement_type = movement_type
		self.vision = vision
		self.weapon_code = weapon_code
		self.weapon_1_name = weapon_1_name
		self.weapon_2_name = weapon_2_name
		self.base_ammo = base_ammo
		self.base_fuel = base_fuel
		self.properties = properties

###	def display(self):
###		print("Name = ", self.name, "\nDivision = ", self.division, "\nCost = ", self.cost,  "\nFire_range = ", self.fire_range, "\nCounter_range = ", self.counter_range, "\nMaxToFire = ", self.max_movement_to_fire, "\nMovement = ", self.movement, "\nMovementType = ", self.movement_type, "\nVision = ", self.vision, "\nMaxAmmo = ", self.max_ammo, "\nMaxFuel = ", self.max_fuel, "\nProperties = ", self.properties)
		




#####################
# CLASS : CO (data) #
#####################
"""
__CO__ [Data]
__ID
name
effect_name
co_zone_type {Croissante, Fixe, Infinie} //TODO : Solution pour Klaus qui remplit à partir des bâtiments
co_zone_size //Ne mettre que la taille minimum. Optionnel si TypeCOZone == Infinie car considéré à un nombre très grand, plus grand que la longueur max d'une map.
effects
has_co_power
co_power_name
co_power_effects
has_sco_power
sco_power_name
sco_power_effects
"""
class CO: #[DATA]

	def __init__(self, name="Default", effect_name="Effect", co_zone_type="None", co_zone_size=0,
			effects=[], has_co_power=False, co_power_name="COP", co_power_effects=[], 
			has_sco_power=False, sco_power_name="SCOP", sco_power_effects=[],
			default=False, manual=None):

		if default:
			"""Create one object with the default parameters"""
			self.name = "Default"
			self.effect_name = "Effect"
			self.co_zone_type = "None"
			self.co_zone_size = 0
			self.effects = []
			self.has_co_power = False
			self.co_power_name = "COP"
			self.co_power_effects = []
			self.has_sco_power = False
			self.sco_power_name = "SCOP"
			self.sco_power_effects = []


		elif manual is None:
			"""Create one object with the set parameters"""
			self.name = name
			self.effect_name = effect_name
			self.co_zone_type = co_zone_type
			self.co_zone_size = co_zone_size
			self.effects = effects
			self.has_co_power = has_co_power
			self.co_power_name = co_power_name
			self.co_power_effects = co_power_effects
			self.has_sco_power = has_sco_power
			self.sco_power_name = sco_power_name
			self.sco_power_effects = sco_power_effects

		else:
			"""Create one object manually"""
			print("Name? (String)")
			self.name = input()
			print("Effect name? (String)")
			self.effect_name = input()
			print("COZoneType? (String)")
			self.co_zone_type = input()
			print("COZoneSize? (int)")
			self.co_zone_size = input()
			print("List of effects? [String]")
			self.effects = input()
			print("Has CO Power? (bool)")
			self.has_co_power = input()
			print("CO power name? (String)")
			self.co_power_name = input()
			print("List of COP effects? [String]")
			self.co_power_effects = input()
			print("Has SUPER CO Power? (bool)")
			self.has_sco_power = input()
			print("SUPER CO power name? (String)")
			self.sco_power_name = input()
			print("List of SCOP effects? [String]")
			self.sco_power_effects = input()


	def setParam(self, name, effect_name, co_zone_type, co_zone_size, effects, has_co_power, co_power_name, co_power_effects, has_sco_power, sco_power_name, sco_power_effects):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.name = name
		self.effect_name = effect_name
		self.co_zone_type = co_zone_type
		self.co_zone_size = co_zone_size
		self.effects = effects
		self.has_co_power = has_co_power
		self.co_power_name = co_power_name
		self.co_power_effects = co_power_effects
		self.has_sco_power = has_sco_power
		self.sco_power_name = sco_power_name
		self.sco_power_effects = sco_power_effects


###	def display(self):
###		print("Name = ", self.name, "\nCOZoneType = ", self.co_zone_type, "\nCOZoneSize = ", self.co_zone_size, "\neffect = ", self.effect, "\nhasCOPower = ", self.has_co_power, "\nCOpower = ", self.co_power, "\nhasSUPERCOPower = ", self.has_sco_power, "\nSUPERCOPower = ", self.sco_power)


#######################
# CLASS : TERRAIN (data) #
#######################
"""
name : String
type : String
coverage : int (number of '*' )
hideout : bool
"""
class Terrain: #[DATA]

	def __init__(self, name="Default", type_="ALL", coverage=0, hideout=False, default=False,
			manual=None):

		if default:
			"""Create one object with the default parameters"""
			self.name = "Default"
			self.type = "ALL"
			self.coverage = 0
			self.hideout = False


		elif manual is None:
			"""Create one object with the set parameters"""
			self.name = name
			self.type = type_
			self.coverage = coverage
			self.hideout = hideout

		else:
			"""Create one object manually"""
			print("Name? (String)")
			self.name = input()
			print("Type? (String)")
			self.type = input()
			print("Coverage value? (int)")
			self.coverage = input()
			print("Hideout? (bool)")
			self.hideout = input()


	def setParam(self, name, type_, coverage, hideout):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.name = name #String
		self.type = type_ #String
		self.coverage = coverage #int
		self.hideout = hideout #bool


	def display(self):
		print("Name = ", self.name, "\nType = ", self.type, "\nCoverage value = ", self.coverage, "\nHideout = ", self.hideout)


#######################
# CLASS : CLIMATE (data) #
#######################
"""
name : String
effects : list of String (commands)
"""
class Climate: #[DATA]

	def __init__(self, name="Default", effects=[], default=False, manual=None):

		if default:
			"""Create one object with the default parameters"""
			self.name = "Default"
			self.effects = []


		elif manual is None:
			"""Create one object with the set parameters"""
			self.name = name
			self.effects = effects

		else:
			"""Create one object manually"""
			print("Name? (String)")
			self.name = input()
			print("List of effects? (list of String representing commands)")
			self.effects = input()


	def setParam(self, name, effects):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.name = name #String
		self.effects = effects #list of String // commands


	def display(self):
		print("Name = ", self.name, "\nEffects = ", self.effects)


#######################
# CLASS : CHARTS (data) #
#######################
"""
damage_chart : 2d array [x:UNIT.Name] [y:UNIT.Name]
damage_chart_indexes : list of String [UNIT.Name]
movement_chart : 2d array [x:TERRAIN.Name] [y:UNIT.movement_type]
movement_chart_indexes : list of String [TERRAIN.Name]
movement_type_list : list of String [UNIT.movement_type]
"""
class Charts: #[DATA]

	def __init__(self, damage_chart=DEF_DC, damage_chart_indexes=DEF_DCI, movement_chart=DEF_MC,
			movement_chart_indexes=DEF_MCI, movement_type_list=DEF_MTL, default=False,
			manual=None):

		if default:
			"""Create one object with the default parameters"""
			self.damage_chart = DEF_DC
			self.damage_chart_indexes = DEF_DCI
			self.movement_chart = DEF_MC
			self.movement_chart_indexes = DEF_MCI
			self.movement_type_list = DEF_MTL


		elif manual is None:
			"""Create one object with the set parameters"""
			self.damage_chart = damage_chart
			self.damage_chart_indexes = damage_chart_indexes
			self.movement_chart = movement_chart
			self.movement_chart_indexes = movement_chart_indexes
			self.movement_type_list = movement_type_list

		else:
			"""Create one object manually"""
			print("Damage chart? (2d array of int, [UNIT.name][UNIT.name])")
			self.damage_chart = input()
			print("Damage chart indexes? (list of String [UNIT.name])")
			self.damage_chart_indexes = input()
			print("Movement chart? (2d array of int, [TERRAIN.name][UNIT.movement_type])")
			self.movement_chart = input()
			print("Movement chart indexes? (list of String [TERRAIN.name])")
			self.movement_chart_indexes = input()
			print("Movement type list? (list of String [UNIT.movement_type])")
			self.movement_type_list = input()


	def setParam(self, damage_chart, damage_chart_indexes, movement_chart, 
			movement_chart_indexes, movement_type_list):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.damage_chart = damage_chart #2d array of int, [UNIT.name][UNIT.name]
		self.damage_chart_indexes = damage_chart_indexes #list of String [UNIT.name]
		self.movement_chart = movement_chart #2d array of int, [TERRAIN.name][UNIT.movement_type]
		self.movement_chart_indexes = movement_chart_indexes #list of String [TERRAIN.name]
		self.movement_type_list = movement_type_list #list of String [UNIT.movement_type]


	def display(self):
		pass


	def getXYDamageChart(self, x, y):
		return self.damage_chart[self.damage_chart_indexes.index(x)][self.damage_chart_indexes.index(y)] #TODO Catch out-of-bounds

	def getXYMovementChart(self, x, y):
		return self.movement_chart[self.movement_chart_indexes.index(x)][self.movement_type_list.index(y)] #TODO Catch out-of-bounds


###################
# OTHER FUNCTIONS #
###################

		
""" chooseBetween(*arguments)
A function which picks randomly one element in the arguments and returns it. Typing is irrelevant.
"""
def chooseBetween(*arguments):
	list_ = []
	n = 0
	for arg in arguments:
		list_.append(arg)
		n = n+1
	return list_[random.randint(0,n-1)]
	

""" userChooseBetween(*arguments)
A function which lets the user choose one element in the arguments, then returns it. Typing is irrelevant.
"""
def userChooseBetween(*arguments):
	list_ = []
	n = 1
	print("Choose between :\n")
	for arg in arguments:
		list_.append(arg)
		print(n, ":", arg)
		n = n+1
	userin = input()
	return list_[userin-1]


