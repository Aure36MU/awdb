
import game
import textparser


"""
Matchup calculator
class Matchup:
	CurrentCO ally
	CurrentCO enemy
	CurrentUnit unit1
	CurrentUnit unit2


Needs all loaded data (COdata, Unitdata, Gamedata)
"""

def main():
	t1 = TextParser("unitexample")
	unit_list = createUnits(t1)
	t2 = TextParser("coexample")
	co_list = createCOs(t2)
	return unit_list


def createUnits(parser):
	unit_indexes = []
	parser.start()
	if parser.getNextLine() != ["***"]:
		parser.advNextLine()
	while not(parser.endOfFile()):
		pass
		unit_name = parser.getNextWord()
		parser.advNextLine()
		unit_variables = parser.getNextLine()
		unit_variables = splitList(unit_variables, ' ')
		try:
			unit_division = unit_variables[0]
			unit_cost = unit_variables[1]
			unit_movement = unit_variables[2]
			unit_movement_type = unit_variables[3]
			(unit_base_fuel, unit_base_fuel_consumption) = unit_variables[4]
			unit_vision = unit_variables[5]
		except (ValueError, IndexError):
			pass
		if (unit_variables[-1] == 0): #No weapon
			parser.advNextLine()

		if (unit_variables[-1] != 2): #First weapon
			parser.advNextLine()
			unit_weapon_1_name = parser.getNextWord()
			unit_base_ammo = parser.getNextWord()
			unit_weapon_1_type = parser.getNextWord()
			unit_fire_range = parser.getNextWord()
			if not(parser.endOfLine()):
				unit_max_movement_to_fire = parser.getNextWord()
			else:
				unit_max_movement_to_fire = 0
			if not(parser.endOfLine()):
				unit_counter_range = parser.getNextWord()
			else:
				unit_counter_range = 0
			parser.advNextLine()

		if (unit_variables[-1] != 1): #Second weapon
			unit_weapon_2_name = parser.getNextWord()
			parser.advNextLine()

		unit_properties = []
		while parser.getNextLine() != (["***"] or [""]):
			unit_properties.append(parser.getNextWord())
			parser.advNextLine()

		unit_indexes.append(Unit(unit_name, unit_division, unit_cost, unit_fire_range,
 					unit_counter_range, unit_max_movement_to_fire, unit_movement,
					unit_movement_type, unit_vision, unit_weapon_1_name,
					unit_weapon_2_name, unit_base_ammo, unit_base_fuel,
					unit_base_fuel_consumption, unit_properties))


		parser.advNextLine()

	return unit_indexes

		# While Get next line is not "***", Get next line
		# Get next line, Set name as Get next word
		# Get next line, should be "Division cost movement movement_type fuel[+x_per_turn] vision weapon_code"
		# Set variables
		# If weapon_code == 3, do both. If weapon_code == 1 or 2, do the first or the second :
		# 	Get next line, should be "Weapon_name : ammo weapon_type(D|I) fire_range(1|(min,max)) [max_movement_to_fire] [counter_range]"
		# 	Get next line, should be "Weapon_name : weapon_type(D|I) fire_range(1|(min,max)) [max_movement_to_fire] [counter_range]"
		# Set variables
		# After weapons ; While Get next line is not "***", Get next line
		# 	[Parse special effect]
		# Next line should be "***". Repeat all.




def createCOs(parser):
	co_indexes = []
	parser.start()
	if parser.getNextLine() != ["***"]:
		parser.advNextLine()
	while not(parser.endOfFile()):

		co_name = parser.getNextWord()
		parser.advNextLine()
		co_effect_name = parser.getNextWord()
		co_zone = parser.getNextWord()
		if (co_zone.find('+') != -1): # Increasing zone
			co_zone_size = int(co_zone.strip('+'))
			co_zone_type = "Increasing"
		else: # Fixed zone
			co_zone_size = co_zone
			co_zone_type = "Fixed"
		co_effects = []
		while not(parser.endOfLine()):
			co_effects.append(parser.getNextWord())
		parser.advNextLine()
		if (parser.currentLineLength() <= 1):
			co_has_power = False
		else:
			co_has_power = True
			co_power_name = parser.getNextWord()
			co_power_effects = []
			while not(parser.endOfLine()):
				co_power_effects.append(parser.getNextWord())
		parser.advNextLine()
		if (parser.currentLineLength() <= 1):
			co_has_superpower = False
		else:
			co_has_superpower = True
			co_superpower_name = parser.getNextWord()
			co_superpower_effects = []
			while not(parser.endOfLine()):
				co_superpower_effects.append(parser.getNextWord())

		# While Get next line is not "***", Get next line
		# Get next line, Set name as Get next word
		# Get next line, Set effect_name as Get next word
		# Get next word, Set co_zone_type and co_zone_size
		# Until end of line : Get next word and place them in effect[]
		# Get next line,
		#	if LineLength is <= 1 set has_co_power as False
		# 	else, set has_co_power as True and Get next word, Set co_power_name
		# 	Until end of line : Get next word and place them in co_power[]
		# Get next line, 
		#	if LineLength is <= 1 set has_sco_power as False
		# 	else, set has_sco_power as True and Get next word, Set sco_power_name
		# 	Until end of line : Get next word and place them in sco_power[]
		# Next line should be "***". Repeat all.


		# Create a dictionary of CO objects.
		# referenced by {id : <instance of CO>}
		# Create a new CO
		co_indexes.append(CO(co_name, co_effect_name, co_zone_type, co_zone_size, co_effects,
					co_has_power, co_power_name, co_power_effects,
					co_has_superpower, co_superpower_name, co_superpower_effects))

		while parser.getNextLine() != (["***"] or [""]):
			parser.advNextLine()
		parser.advNextLine()

	return co_indexes


"""
def loadCOBalance(filename, default=None):
	for instance in CO:
		del instance #Delete all CO objects in data
	
	if (default == "AWDS"):
	#The default balance in the AWDS game will be loaded.


	elif (default == "AWDoR"):
	#The default balance in the AWDoR game will be loaded.



	elif (default == "Custom"):
	#The custom balance of this project will be loaded.

		
		jake = CO("Jake", "Increase", 2, ["Prairie", "bonus : +20/+0 ALL plains"], True, ["Offensive", "set_movement_cost : 1 plains ALL", "bonus : +20/+0 ALL plains"], True, ["Hyper combat", "set_movement_cost : 1 plains ALL", "bonus : +40/+0 ALL plains", "increase_movement : 1 DirectLand"])
		rachel = CO("Rachel", "Increase", 4, ["Camaraderie", "repair_ratio effect=COZone : multiply 2 Properties ALL equal"], True, ["Bonne étoile", "set_luck_values : 0 30"], True, ["Pilonnage", "set_luck_values : 0 30", "missile : most_value 3 3 2 ALL_foe"])
		andy = CO("Andy", "Increase", 2, ["Mécano", "increase_HP : 1 ALL"], True, ["Réparafond", "increase_HP : 2 ALL", "bonus : +10/+0 ALL"], True, ["Génie logistique", "increase_HP : 5 ALL", "bonus : +10/+0 ALL, increase_movement : 1 ALL"])
		max = CO("Max", "Increase", 1, ["Attaque frontale", "bonus : +30/+0 Direct"], True, ["Max en force", "increase_movement : 1 Direct"], True, ["Puissance max", "increase_movement : 1 Direct", "bonus : +20/+0 Direct"])
		sami = CO("Sami", "Increase", 3, ["Forces spéciales", "bonus : +20/+30 Soldier", "increase_capture : 2 Properties Soldier"], True, ["Marche forcée", "increase_movement : 1 Transport", "increase_movement : 1 Soldier", "increase_capture : 3 Properties Soldier"], True, ["Conquête", "increase_movement : 2 Transport", "increase_movement : 2 Soldier", "increase_capture : 8 Properties Soldier"])
		nell = CO("Nell", "Increase", 3, ["Bonne fortune", "set_luck_values : 0 20"], True, ["Bonne étoile", "set_luck_values : 0 30"], True, ["Lady la chance", "set_luck_values : 0 50"])
		hachi = CO("Hachi", "Increase", 4, ["Economies", "bonus : +0/+10 ALL"], True, ["Troc", "decrease_price : 50% ALL"], True, ["Union marchande", "decrease_price : 50% ALL", "??????"])


	else:
	Open the file that contains the user balance.
		parser = TextParser(filename)
"""		

def loadUnitBalance(filename, default=False):
	pass
	#TODO
	# + don't forget to check if all the units are in Gamebalance !!!

def loadGameBalance(filename, default=False):
	pass
	#TODO
	#


"""-------------------------------------------------------------------"""

"""ATTENTION : All RNG functions defined here are purposely used for this program
We want a pseudo-RNG based on a seed (system time in sec since 1970), and keep a track on last ~10 RN used.

"""
###def RNG

# random.seed(time.time())
