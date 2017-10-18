#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io
import os
import random
import sys



####################
# GLOBAL VARIABLES #
####################




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
	def __init__(self, default=False, manual=None):
		"""Create one object with the default parameters"""
		"""To create one manually, you can call __init__ with (self, any_argument)"""
		if default is not False:
			self.name = "Default" #String
			self.division = "Land" #String
			self.cost = 0 #int
			self.range = (1,1) #(int,int)
			self.movement = 1 #int
			self.movementType = "Infantry" #String
			self.vision = 1 #int
			self.ammoFirstWeapon = 0 #int
			self.fuel = 99 #int
			self.properties = [] #list of String

		elif manual is None:
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
			print "Name? (String)"
			self.name = input()
			print "Division? (String)"
			self.division = input()
			print "Cost? (int)"
			self.cost = input()
			print "Range? ((int,int))"
			self.range = input()
			print "Movement? (int)"
			self.movement = input()
			print "MovementType? (String)"
			self.movementType = input()
			print "Vision? (int)"
			self.vision = input()
			print "AmmoFirstWeapon? (int)"
			self.ammoFirstWeapon = input()
			print "Fuel? (int)"
			self.fuel = input()
			print "Other properties? (list of String)"
			self.properties = input()



	def new(self, name, division, cost, range_, movement, movementType, vision, ammoFirstWeapon, fuel, properties):
		"""Change all the attributes at the same time. Arguments are in the same order as initialisation"""
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


	def displayUnit(self):
		print "Name = ", self.name, "\nDivision = ", self.division, "\nCost = ", self.cost, "\nRange = ", self.range, "\nMovement = ", self.movement, "\nMovementType = ", self.movementType, "\nVision = ", self.vision, "\nAmmo1stWeapon = ", self.ammoFirstWeapon, "\nFuel = ", self.fuel, "\nProperties = ", self.properties
		
#test = Unit()
#Unit.displayUnit(test)		

