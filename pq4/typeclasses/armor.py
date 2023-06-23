from evennia import DefaultObject

#class (armor):
#	name = ""
#	price = 
#	defense = 
#	desc = ""
#	def at_object_creation(self):
#		self.tags.add("equipable", category="armor")
#		self.locks.add("drop:false()")
#		self.db.name = ""
#		self.db.price = 
#		self.db.defense = 
#		self.db.desc = ""

#Sainted Armor
#class saintedarmor(armor):
#	name = ""
#	price = 0
#	defense = 0
#	heal = 0
#	desc = ""
#	def at_object_creation(self):
#		self.tags.add("equipable", category="armor")
#		self.tags.add("sainted")
#		self.locks.add("drop:false()")
#		self.db.heal = int(self.heal)
#		self.db.name = self.name
#		self.db.price = int(self.price)
#		self.db.defense = int(self.defense)
#		self.db.desc = self.desc

#Cursed Armor
#class cursedarmor(armor):
#	name = ""
#	price = 0
#	defense = 0
#	unheal = 0
#	desc = ""
#	def at_object_creation(self):
#		self.tags.add("equipable", category="armor")
#		self.tags.add("cursed")
#		self.locks.add("drop:false()")
#		self.db.unheal = int(self.unheal)
#		self.db.name = self.name
#		self.db.price = int(self.price)
#		self.db.defense = int(self.defense)
#		self.db.desc = self.desc

#armor desc
class armor(DefaultObject):
	def return_appearance(self,looker):
		desc = str()
		desc = "|/"+ self.key + ": Armor, +" + str(self.db.defense) + " defense." + "|/" + self.db.desc
		return desc

#shield desc
class shield(DefaultObject):
	def return_appearance(self,looker):
		desc = str()
		desc = "|/"+ self.key + ": Shield, +" + str(self.db.defense) + " defense." + "|/" + self.db.desc
		return desc

#shields
class enigmashield(shield):
	name = "Enigma Shield"
	price = 0
	defense = 0
	desc = "Light traces across patterned lines covering the shield. You see the following carved in runes and geometric shapes: II, 11 Rings, and a rhombicuboctahedron with position 5 illuminated."
	def at_object_creation(self):
		self.tags.add("equipable", category="shield")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class potlid(shield):
	name = "Pot Lid"
	price = 90
	defense = 4
	desc = "A cast iron pot lid. Not great as a shield, but better than nothing."
	def at_object_creation(self):
		self.tags.add("equipable", category="shield")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class bronzebuckler(shield):
	name = "Bronze Buckler"
	price = 800
	defense = 10
	desc = "A small basic shield made of hammered bronze."
	def at_object_creation(self):
		self.tags.add("equipable", category="shield")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class crystalshield(shield):
	name = "Crystal Shield"
	price = 148000
	defense = 20
	desc = "A prismatic crystal shield, wide and tall."
	def at_object_creation(self):
		self.tags.add("equipable", category="shield")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class titanshield(shield):
	name = "Titan Shield"
	price = 14800
	defense = 30
	desc = "Shield of the Titan Ophion."
	def at_object_creation(self):
		self.tags.add("equipable", category="shield")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"



#armor template
class armortemplate(armor):
	name = ""
	price = 0
	defense = 0
	desc = ""
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class enigmaarmor(armor):
	name = "Enigma Armor"
	price = 0
	defense = 0
	desc = "Light traces across patterned lines covering the armor. You see the following carved in runes and geometric shapes: III, 3 Rings, and a rhombicuboctahedron with position 12 illuminated."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

#Vak Dal Upper District Fancy Clothes
class fancyclothes(armor):
	name = "Fancy Clothes"
	price = 100
	defense = 0
	desc = "A finely tailored set of clothing, oh it's so fancy!"
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"
		self.tags.add("fancy")

#papricallah 1-3
class tatteredrags(armor):
	name = "Tattered Rags"
	price = 10
	defense = 1
	desc = "Slightly better than fighting naked."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class travelerscloak(armor):
	name = "Travelers Cloak"
	price = 20
	defense = 2
	desc = "A thick woolen cloak."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

#tormey 4-6
class wayfarersrobes(armor):
	name = "Wayfarers Robes"
	price = 70
	defense = 4
	desc = "A hardy set of robes."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class woodenbarrel(armor):
	name = "Wooden Barrel"
	price = 160
	defense = 6
	desc = "A wooden barrel with shoulder straps."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

#kharro 10-12
class scalemail(armor):
	name = "Scale Mail"
	tokens = 800
	price = 300
	defense = 10
	desc = "A shirt of iridescent overlapping snake scales."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class peacockpeacoat(armor):
	name = "Peacock Peacoat"
	tokens = 1400
	price = 500
	defense = 12
	desc = "A fabulously fancy bit of plumage to protect your tail."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

#orthan 16-18
class tacticaltux(armor):
	name = "Tactical Tux"
	price = 1000
	defense = 16
	desc = "For when you've got dinner reservations at 7 and a monster fight at 9."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class spikedarmor(armor):
	name = "Spiked Armor"
	price = 1500
	defense = 18
	desc = "The best way to gain a reputation for killer hugs."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

#varken 24-26
class perfectponcho(armor):
	name = "Perfect Poncho"
	price = 3000
	defense = 24
	desc = "What more could you possibly want? It's PERFECT!"
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class weremadilloplate(armor):
	name = "Weremadillo Plate"
	price = 5000
	defense = 26
	desc = "A full body suit of plated armor made from authentic weremadillo."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

#valaharra 30
class pepperplate(armor):
	name = "Pepper Plate"
	price = 7700
	defense = 28
	desc = "Plate armor forged with a hellfire fueled by spice."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"


#holy and evil
class anointedarmor(armor):
	name = "Anointed Armor"
	price = 5000
	defense = 18
	heal = 3
	desc = "Armor anointed with holy oil. Heals 3 hp during battle and while exploring."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.tags.add("sainted")
		self.locks.add("drop:false()")
		self.db.heal = int(self.heal)
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"

class ominousarmor(armor):
	name = "Ominous Armor"
	tokens = 6660000
	price = 5000
	defense = 22
	unheal = 4
	desc = "Armor with an evil aura. Inflicts 4 damage during battle and while exploring."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.tags.add("cursed")
		self.locks.add("drop:false()")
		self.db.unheal = int(self.unheal)
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"


class gimpsuit(armor):
	name = "Gimp Suit"
	price = 2000
	defense = 8
	unheal = 2
	desc = "Glistening black leather. Inflicts 2 pain... err damage during battle and while exploring."
	def at_object_creation(self):
		self.tags.add("equipable", category="armor")
		self.tags.add("cursed")
		self.locks.add("drop:false()")
		self.db.unheal = int(self.unheal)
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.defense = int(self.defense)
		self.db.desc = self.desc
		self.db.upgraded = "no"
