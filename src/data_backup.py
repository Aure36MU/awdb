#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io
import os
import random
import sys

from __future__ import print_function



####################
# GLOBAL VARIABLES #
####################

"""
damageChart=DEF_DC,
damageChartIndexes=DEF_DCI, 
movementChart=DEF_MC,
movementChartIndexes=DEF_MCI, 
movementTypeList=DEF_MTL,
"""
DEF_DC = [[]]
DEF_DCI = []
DEF_MC = [[]]
DEF_MCI = []
DEF_MTL = []


#######################
# CLASS : UNIT (data) #
#######################
"""
__UNITS__ [Data]
__ID
Name
Division
Cost
Range
Movement
MovementType
Vision
AmmoFirstWeapon //Contrôle le nombre de munitions max. de l'arme primaire. 0 s'il n'en a pas.
Fuel
Properties
"""
class Unit: #[DATA]
	def __init__(self, name="Default", division="Land", cost=0, range_=(1,1), movement=1,
			movementType="Infantry", vision=1, ammoFirstWeapon=0, fuel=99,
			properties=[], default=False, manual=False):

		if default is not False:
			"""Create one object with the default parameters"""
			self.name = "Default"
			self.division = "Land"
			self.cost = 0
			self.range = (1,1)
			self.movement = 1
			self.movementType = "Infantry"
			self.vision = 1
			self.ammoFirstWeapon = 0
			self.fuel = 99
			self.properties = []


		elif manual is False:
			"""Create one object with the set parameters"""
			self.name = name
			self.division = division
			self.cost = cost
			self.range = range_
			self.movement = movement
			self.movementType = movementType
			self.vision = vision
			self.ammoFirstWeapon = ammoFirstWeapon
			self.fuel = fuel
			self.properties = properties

		else:
			"""Create one object manually"""
			print("Name? (String)")
			self.name = input()
			print("Division? (String)")
			self.division = input()
			print("Cost? (int)")
			self.cost = input()
			print("Range? ((int,int))")
			self.range = input()
			print("Movement? (int)")
			self.movement = input()
			print("MovementType? (String)")
			self.movementType = input()
			print("Vision? (int)")
			self.vision = input()
			print("AmmoFirstWeapon? (int)")
			self.ammoFirstWeapon = input()
			print("Fuel? (int)")
			self.fuel = input()
			print("Other properties? (list of String)")
			self.properties = input()



	def setParam(self, name, division, cost, range_, movement, movementType, vision, ammoFirstWeapon, fuel, properties):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.name = name #String
		self.division = division #String
		self.cost = cost #int
		self.range = range_ #(int,int)
		self.movement = movement #int
		self.movementType = movementType #String
		self.vision = vision #int
		self.ammoFirstWeapon = ammoFirstWeapon #int
		self.fuel = fuel #int
		self.properties = properties #list of String


	def displayUnit(self):
		print("Name = ", self.name, "\nDivision = ", self.division, "\nCost = ", self.cost, "\nRange = ", self.range, "\nMovement = ", self.movement, "\nMovementType = ", self.movementType, "\nVision = ", self.vision, "\nAmmo1stWeapon = ", self.ammoFirstWeapon, "\nFuel = ", self.fuel, "\nProperties = ", self.properties)
		
#test = Unit()
#Unit.displayUnit(test)		



#####################
# CLASS : CO (data) #
#####################
"""
__COS__ [Data]
__ID
Name
COZoneType {Croissante, Fixe, Infinie} //TODO : Solution pour Klaus qui remplit à partir des bâtiments
COZoneSize //Ne mettre que la taille minimum. Optionnel si TypeCOZone == Infinie car considéré à un nombre très grand, plus grand que la longueur max d'une map.
Effect
HasCOPower
COPower
HasSUPERCOPower
SUPERCOPower
"""
class CO: #[DATA]

	def __init__(self, name="Default", COZoneType="None", COZoneSize=0, effect=[],
			hasCOPower=False, COPower=[], hasSUPERCOPower=False, SUPERCOPower=[],
			default=False, manual=None):

		if default is not False:
			"""Create one object with the default parameters"""
			self.name = "Default"
			self.COZoneType = "None"
			self.COZoneSize = 0
			self.effect = []
			self.hasCOPower = False
			self.COPower = []
			self.hasSUPERCOPower = False
			self.SUPERCOPower = []


		elif manual is None:
			"""Create one object with the set parameters"""
			self.name = name
			self.COZoneType = COZoneType
			self.COZoneSize = COZoneSize
			self.effect = effect
			self.hasCOPower = hasCOPower
			self.COPower = COPower
			self.hasSUPERCOPower = hasSUPERCOPower
			self.SUPERCOPower = SUPERCOPower

		else:
			"""Create one object manually"""
			print("Name? (String)")
			self.name = input()
			print("COZoneType? (String)")
			self.COZoneType = input()
			print("COZoneSize? (int)")
			self.COZoneSize = input()
			print("List of effects? [String]")
			self.effect = input()
			print("Has CO Power? (bool)")
			self.hasCOPower = input()
			print("List of COP effects? [String]")
			self.COPower = input()
			print("Has SUPER CO Power? (bool)")
			self.hasSUPERCOPower = input()
			print("List of SCOP effects? [String]")
			self.SUPERCOPower = input()


	def setParam(self, name, COZoneType, COZoneSize, effect, hasCOPower, COPower, hasSUPERCOPower, SUPERCOPower):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.name = name #String
		self.COZoneType = COZoneType #String
		self.COZoneSize = COZoneSize #int
		self.effect = effect #list of String
		self.hasCOPower = hasCOPower #bool
		self.COPower = COPower #list of String
		self.hasSUPERCOPower = hasSUPERCOPower #bool
		self.SUPERCOPower = SUPERCOPower #list of String

	def displayCO(self):
		print("Name = ", self.name, "\nCOZoneType = ", self.COZoneType, "\nCOZoneSize = ", self.COZoneSize, "\neffect = ", self.effect, "\nhasCOPower = ", self.hasCOPower, "\nCOPower = ", self.COPower, "\nhasSUPERCOPower = ", self.hasSUPERCOPower, "\nSUPERCOPower = ", self.SUPERCOPower)


#######################
# CLASS : TERRAIN (data) #
#######################
"""
Name : String
Type : String
Coverage : int (number of * )
Hideout : bool
"""
class Terrain: #[DATA]

	def __init__(self, name="Default", type_="ALL", coverage=0, hideout=False, default=False,
			manual=None):

		if default is not False:
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


	def displayTerrain(self):
		print("Name = ", self.name, "\nType = ", self.type, "\nCoverage value = ", self.coverage, "\nHideout = ", self.hideout)


#######################
# CLASS : CLIMATE (data) #
#######################
"""
Name : String
Effects : list of String (commands)
"""
class Climate: #[DATA]

	def __init__(self, name="Default", effects=[], default=False, manual=None):

		if default is not False:
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


	def displayClimate(self):
		print("Name = ", self.name, "\nEffects = ", self.effects)


#######################
# CLASS : CHARTS (data) #
#######################
"""
DamageChart : 2d array [x:UNIT.Name] [y:UNIT.Name]
DamageChartIndexes : list of String [UNIT.Name]
MovementChart : 2d array [x:TERRAIN.Name] [y:UNIT.MovementType]
MovementChartIndexes : list of String [TERRAIN.Name]
MovementTypeList : list of String [UNIT.MovementType]
"""
class Charts: #[DATA]

	def __init__(self, damageChart=DEF_DC, damageChartIndexes=DEF_DCI, movementChart=DEF_MC,
			movementChartIndexes=DEF_MCI, movementTypeList=DEF_MTL, default=False,
			manual=None):

		if default is not False:
			"""Create one object with the default parameters"""
			self.damageChart = DEF_DC
			self.damageChartIndexes = DEF_DCI
			self.movementChart = DEF_MC
			self.movementChartIndexes = DEF_MCI
			self.movementTypeList = DEF_MTL


		elif manual is None:
			"""Create one object with the set parameters"""
			self.damageChart = damageChart
			self.damageChartIndexes = damageChartIndexes
			self.movementChart = movementChart
			self.movementChartIndexes = movementChartIndexes
			self.movementTypeList = movementTypeList

		else:
			"""Create one object manually"""
			print("Damage chart? (2d array of int, [UNIT.name][UNIT.name])")
			self.damageChart = input()
			print("Damage chart indexes? (list of String [UNIT.name])")
			self.damageChartIndexes = input()
			print("Movement chart? (2d array of int, [TERRAIN.name][UNIT.movementType])")
			self.movementChart = input()
			print("Movement chart indexes? (list of String [TERRAIN.name])")
			self.movementChartIndexes = input()
			print("Movement type list? (list of String [UNIT.movementType])")
			self.movementTypeList = input()


	def setParam(self, damageChart, damageChartIndexes, movementChart, movementChartIndexes, 
			movementTypeList):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
		self.damageChart = damageChart #2d array of int, [UNIT.name][UNIT.name]
		self.damageChartIndexes = damageChartIndexes #list of String [UNIT.name]
		self.movementChart = movementChart #2d array of int, [TERRAIN.name][UNIT.movementType]
		self.movementChartIndexes = movementChartIndexes #list of String [TERRAIN.name]
		self.movementTypeList = movementTypeList #list of String [UNIT.movementType]


	def displayCharts(self):
		pass


###################
# OTHER FUNCTIONS #
###################

		
""" choose_between(*arguments)
A function which picks randomly one element in the arguments and returns it. Typing is irrelevant.
"""
def choose_between(*arguments):
	list_ = []
	n = 0
	for arg in arguments:
		list_.append(arg)
		n = n+1
	return list_[random.randint(0,n-1)]
	

""" user_choose_between(*arguments)
A function which lets the user choose one element in the arguments, then returns it. Typing is irrelevant.
"""
def user_choose_between(*arguments):
	list_ = []
	n = 1
	print("Choose between :\n")
	for arg in arguments:
		list_.append(arg)
		print(n, ":", arg)
		n = n+1
	userin = input()
	return list_[userin-1]

"""
def load_CObalance(filename, default=None):
	for instance in CO:
		del instance #Delete all CO objects in data
	
	if (default == "AWDS"):
	The default balance in the AWDS game will be loaded.


	elif (default == "AWDoR"):
	The default balance in the AWDoR game will be loaded.



	elif (default == "Custom"):
	The custom balance of this project will be loaded.

		
		jake = CO("Jake", "Increase", 2, ["Prairie", "bonus +20/+0 ALL plains"], True, ["Offensive", "set_movement_cost 1 plains ALL", "bonus +20/+0 ALL plains"], True, ["Hyper combat", "set_movement_cost 1 plains ALL", "bonus +40/+0 ALL plains", "increase_movement 1 DirectLand"])
		rachel = CO("Rachel", "Increase", 4, ["Camaraderie", "repair_ratio effect=COZone multiply 2 Properties ALL equal"], True, ["Bonne étoile", "set_luck_values 0 30"], True, ["Pilonnage", "set_luck_values 0 30", "missile most_value 3 3 2 ALL_foe"])
		andy = CO("Andy", "Increase", 2, ["Mécano", "increase_HP 1 ALL"], True, ["Réparafond", "increase_HP 2 ALL", "bonus +10/+0 ALL"], True, ["Génie logistique", "increase_HP 5 ALL", "bonus +10/+0 ALL, increase_movement 1 ALL"])
		max = CO("Max", "Increase", 1, ["Attaque frontale", "bonus +30/+0 Direct"], True, ["Max en force", "increase_movement 1 Direct"], True, ["Puissance max", "increase_movement 1 Direct", "bonus +20/+0 Direct"])
		sami = CO("Sami", "Increase", 3, ["Forces spéciales", "bonus +20/+30 Soldier", "increase_capture 2 Properties Soldier"], True, ["Marche forcée", "increase_movement 1 Transport", "increase_movement 1 Soldier", "increase_capture 3 Properties Soldier"], True, ["Conquête", "increase_movement 2 Transport", "increase_movement 2 Soldier", "increase_capture 8 Properties Soldier"])
		nell = CO("Nell", "Increase", 3, ["Bonne fortune", "set_luck_values 0 20"], True, ["Bonne étoile", "set_luck_values 0 30"], True, ["Lady la chance", "set_luck_values 0 50"])
		hachi = CO("Hachi", "Increase", 4, ["Economies", "bonus +0/+10 ALL"], True, ["Troc", "decrease_price 50% ALL"], True, ["Union marchande", "decrease_price 50% ALL", "??????"])


	else:
	Open the file that contains the user balance.
		file.open(filename)
"""		

def load_Unitbalance(filename, default=False):
	pass #TODO
	# + don't forget to check if all the units are in Gamebalance !!!

def load_Gamebalance(filename, default=False):
	pass #TODO
	#
	

