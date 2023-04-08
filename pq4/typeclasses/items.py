from evennia import DefaultObject

class item(DefaultObject):
	name = ""
	price = ""
	desc = ""
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("battle" "world" "both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = "?"
		self.db.desc = self.desc
	def return_appearance(self,looker):
		desc = str()
		desc = "|/"+ self.key + " - " + str(self.db.qty) + ". " + self.db.desc
		return desc

#sellable
class goldbar(item):
	name = "Gold Bar"
	price = 1500
	desc = "A shiny bar of solid gold."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class diamondring(item):
	name = "Diamond Ring"
	price = 5000
	desc = "A sparkling ring with a diamond in the shape of a slime."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class seashell(item):
	name = "Sea Shell"
	price = 20
	desc = "An iridescent shell that shimmers in the sun."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class greenglass(item):
	name = "Green Glass"
	price = 700
	desc = "Beautiful green colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Green"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class redglass(item):
	name = "Red Glass"
	price = 700
	desc = "Beautiful red colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Red"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class blueglass(item):
	name = "Blue Glass"
	price = 700
	desc = "Beautiful blue colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Blue"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class yellowglass(item):
	name = "Yellow Glass"
	price = 700
	desc = "Beautiful yellow colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Yellow"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class purpleglass(item):
	name = "Purple Glass"
	price = 700
	desc = "Beautiful purple colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Purple"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class orangeglass(item):
	name = "Orange Glass"
	price = 700
	desc = "Beautiful orange colored glass."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.glasscolor = "Orange"
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class chromacrystal(item):
	name = "Chroma Crystal"
	tokens = 350
	price = 80
	desc = "A color changing crystal."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class marcasitesugar(item):
	name = "Marcasite Sugar"
	price = 80
	desc = "Blue sand that glows in moonlight."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

class hangmansrope(item):
	name = "Hangmans Rope"
	price = 1
	desc = "A length of hangmans rope."
	def at_object_creation(self):
		self.tags.add("sellableitem")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.desc = self.desc

#World and Battle
	#health
class spicyherb(item):
	name = "Spicy Herb"
	tokens = 25
	price = 25
	desc = "Restores 15 HP. A spicy herb to put some pep in your step."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["health", "15"]
		self.db.desc = self.desc

class fixerflask(item):
	name = "Fixer Flask"
	tokens = 75
	price = 75
	desc = "Restores 60 HP. Just a little sip to perk up the spirits."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["health", "60"]
		self.db.desc = self.desc

	#magic
class magicdust(item):
	name = "Magic Dust"
	tokens = 30
	price = 30
	desc = "Restores 5 MP. Just like Grandma used to make!"
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["magic", "5"]
		self.db.desc = self.desc

class sageelixir(item):
	name = "Sage Elixir"
	tokens = 130
	price = 65
	desc = "Restores 15 MP. Small batch, hand crafted by dedicated sages."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["magic", "15"]
		self.db.desc = self.desc

	#health and magic
class restoringruby(item):
	name = "Restoring Ruby"
	tokens = 200
	price = 200
	desc = "Restores 50 HP and 15 MP."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["all", "50", "15"]
		self.db.desc = self.desc

class yorkshiretea(item):
	name = "Yorkshire Tea"
	tokens = 750
	price = 750
	desc = "Restores Full HP and Full MP."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("both")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["all", "9999", "9999"]
		self.db.desc = self.desc

#World Only
	#travel
class fasterfeather(item):
	name = "Faster Feather"
	tokens = 10
	price = 50
	desc = "A mysterious feather of a lesser known avian. Travel to any known location."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["travel"]
		self.db.desc = self.desc

#Battle Only
	#flee
class pocketsand(item):
	name = "Pocket Sand"
	tokens = 50
	price = 50
	desc = "Blinding sand used to escape from battle."
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("givable")
		self.tags.add("battle")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.phrase = "SHA-SHA-SHAAAA!!! You throw a handful of sand in the enemies eyes blinding them as you flee from battle."
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["flee"]
		self.db.desc = self.desc

#Attribute Increase
class powerpepper(item):
	name = "Power Pepper"
	price = 0
	statinc = 1
	stattype = "attack"
	desc = "Permanently increase attack by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

class armoredpepper(item):
	name = "Armored Pepper"
	price = 0
	statinc = 1
	stattype = "defense"
	desc = "Permanently increase defense by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

class magicalpepper(item):
	name = "Magical Pepper"
	price = 0
	statinc = 3
	stattype = "magic"
	desc = "Permanently increase max MP by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

class lifepepper(item):
	name = "Life Pepper"
	price = 0
	statinc = 5
	stattype = "health"
	desc = "Permanently increase max HP by %d." % (statinc)
	def at_object_creation(self):
		self.tags.add("item")
		self.tags.add("world")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.qty = 0
		self.db.action = ["statinc"]
		self.db.stat = self.stattype
		self.db.increase = int(self.statinc)
		self.db.desc = self.desc

#Generic
class itembook(DefaultObject):
	def at_object_creation(self):
		self.tags.add("readable", category="isreadable")
		self.tags.add("single", category="isreadable")
		self.db.story = "Book Contents"
		self.locks.add("drop:false()")
		self.db.desc = "It's a book, you might want to try and Read it."
		
class ardtreaskey(DefaultObject):
	def at_object_creation(self):
		self.locks.add("drop:false()")
		self.db.desc = "Key to the Castle Ardismouf Treasury."