from evennia import DefaultObject

class weapon(DefaultObject):
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = ""
		self.db.price = 0
		self.db.attack = 0
		self.db.desc = ""
		self.db.upgraded = "no"
	def return_appearance(self,looker):
		desc = str()
		desc = "|/" + self.key + ": Weapon, +" + str(self.db.attack) + " attack." + "|/" + self.db.desc
		return desc


#papricallah 2-4
class dullspoon(weapon):
	name = "Dull Spoon"
	price = 10
	attack = 1
	desc = "A dull soup spoon."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class wetnoodle(weapon):
	name = "Wet Noodle"
	price = 10
	attack = 1
	desc = "A wide wet noodle. Good for slapping."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.upgraded = "no"
		self.db.atkphr = ["SLAP!!", "WHAP!!", "IN THE NAME OF HIS NOODLY GOODNESS I SMITE THEE FIEND!!", "THWAP!"]

class stick(weapon):
	name = "Stick"
	price = 20
	attack = 2
	desc = "A sharpened stick. Don't poke your eye out."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class pitchfork(weapon):
	name = "Pitch Fork"
	price = 100
	attack = 3
	desc = "A three tined pitchfork, perfect for all your peasant rioting needs."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["THEY STOLE OUR CHICKENS!!", "DEATH TO THE RULING CLASS!"]
		self.db.upgraded = "no"

class silverknife(weapon):
	name = "Silver Knife"
	price = 60
	attack = 4
	desc = "A smooth beautiful silver knife."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["Knife to meet you!"]
		self.db.upgraded = "no"

#tormey 4-10
class cheddarchopper(weapon):
	name = "Cheddar Chopper"
	price = 60
	attack = 4
	desc = "A clever cleaver made of cheddar cheese. Don't worry, it's SHARP cheddar."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class coppersword(weapon):
	name = "Copper Sword"
	price = 110
	attack = 6
	desc = "An authoritarian sword guaranteed to put down any enemy."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["FREEZE SCUMBAG!", "STOP RESISTING!", "AGAINST THE WALL AND SPREAD EM!", "RESPECT MY AUTHORITY!"]
		self.db.upgraded = "no"

class warhamr(weapon):
	name = "War Hamr"
	price = 180
	attack = 10
	desc = "A nice hunk of aged ham on a stick. Mmmmmm ham."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["Oink! SQUEEEEEE!", "Oink, oink!", "OINK! *BOINK*"]
		self.db.upgraded = "no"

#Kharro 10-15
class cactusclub(weapon):
	name = "Cactus Club"
	tokens = 400
	price = 180
	attack = 10
	desc = "A spiky club made from the arm of a saguaro cactus. Imported from Arizona and parts of northern Mexico. NOT TEXAS."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["Spike-ological Warfare!!"]
		self.db.upgraded = "no"

class sunspear(weapon):
	name = "Sun Spear"
	tokens = 700
	price = 256
	attack = 12
	desc = "A hefty spear with a sinuous point polished to a mirror shine."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["Prepare for a spear-itual awakening!"]
		self.db.upgraded = "no"

class snakewhip(weapon):
	name = "Snake Whip"
	tokens = 700
	price = 256
	attack = 12
	desc = "A fanged snake with a handle on its tail. Make your enemies hisss-tory."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["HISSSSSS!", "HISSS *CRACK*"]
		self.db.upgraded = "no"

#Orthan 15-20
class buzzooka(weapon):
	name = "Buzzooka"
	price = 560
	attack = 15
	desc = "*bzzzzz* *bzzz*. Blasts your enemies with bees!"
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["*BZZZZZZ*", "*Angry bee noises*"]
		self.db.upgraded = "no"

class lightsaber(weapon):
	name = "Light Saber"
	price = 1500
	attack = 16
	desc = "Don't get all excited, it's just not as heavy as a regular saber."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["|x(]HHH[|g================|n", "VRRRRMmmmmmm", "|x(]HHH[|r================|n", "vvrrrRRRMmmmmmm", "|x(]HHH[|m================|n", "I'M A JEDI BITCH!!!"]
		self.db.upgraded = "no"

#Varken 20-28
class monstermasher(weapon):
	name = "Monster Masher"
	price = 1500
	attack = 20
	desc = "A large war hammer. Flat on one side, pyramid spikes on the other, makes any enemy tender hearted."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class fullmoonaxe(weapon):
	name = "Full Moon Axe"
	price = 1500
	attack = 20
	desc = "A nasty looking double sided axe. Watch out werewolves."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class johnwickspencil(weapon):
	name = "John Wicks Pencil"
	price = 3000
	attack = 23
	desc = "Once used to kill 3 men in a bar. Don't worry, we washed it off."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

#Valaharra 20-28
class pen(weapon):
	name = "PEN"
	price = 9800
	attack = 28
	desc = "Is the P.E.N truly mightier? Yup, it is. Pure Evil kNife. Now with 28% more evil!"
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class kingslimesword(weapon):
	name = "King Slime Sword"
	price = 9200
	attack = 26
	desc = "A sword fit for a king... if the king was big, blue, and giggly."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class angrygoose(weapon):
	name = "Angry Goose"
	price = 150000
	attack = 30
	desc = "It's a goo*HONK* ouch! The F*&^#% thing is biting me! *HONK* Son of a*HONK* GET IT OFF ME! *HONK-HONK*."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["*HONK*"]
		self.db.upgraded = "no"

#ultimate
class shamshirofspice(weapon):
	name = "Shamshir of Spice"
	price = 300000
	attack = 50
	desc = "Legendary sword forged of pure spice. The blade glows red as spice and fire flicker along the honed edge."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

#Special 40+
#shank
class diamondhands(weapon):
	name = "Diamond Hands"
	tokens = 42069000
	price = 420690
	attack = 40
	desc = "Diamond spiked gauntlets of the Ape King."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = ["I just like the stock.", "STONKS"]
		self.db.upgraded = "no"

class souledge(weapon):
	name = "Soul Edge"
	price = 0
	attack = 50
	desc = "A massive blade emitting a dark red aura. Twisting dripping flesh interweaving with the jagged iron. A large lidless eye stares at you from the center of the hilt."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.db.removable = "no"
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"

class enigmaweapon(weapon):
	name = "Enigma Weapon"
	price = 10
	attack = 0
	desc = "Light traces across patterned lines covering the weapon. You see the following carved in runes and geometric shapes: IV, 10 Rings, and a rhombicuboctahedron with position 21 illuminated."
	def at_object_creation(self):
		self.tags.add("equipable", category="weapon")
		self.locks.add("drop:false()")
		self.db.name = self.name
		self.db.price = int(self.price)
		self.db.attack = int(self.attack)
		self.db.desc = self.desc
		self.db.atkphr = []
		self.db.upgraded = "no"