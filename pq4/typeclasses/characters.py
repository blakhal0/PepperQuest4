"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from evennia.prototypes.spawner import spawn


class Character(DefaultCharacter):
	"""
	The Character defaults to reimplementing some of base Object's hook methods with the
	following functionality:

	at_basetype_setup - always assigns the DefaultCmdSet to this object type
					(important!)sets locks so character cannot be picked up
					and its commands only be called by itself, not anyone else.
					(to change things, use at_object_creation() instead).
	at_after_move(source_location) - Launches the "look" command after every move.
	at_post_unpuppet(account) -  when Account disconnects from the Character, we
					store the current location in the pre_logout_location Attribute and
					move it to a None-location so the "unpuppeted" character
					object does not need to stay on grid. Echoes "Account has disconnected"
					to the room.
	at_pre_puppet - Just before Account re-connects, retrieves the character's
					pre_logout_location Attribute and move it back on the grid.
	at_post_puppet - Echoes "AccountName has entered the game" to the room.

	"""
	def pop_inven(self):
		self.mj_proto = {
			"key": "Monster Journal",
			"typeclass": "typeclasses.objects.monsterjournal",
			"location": self
		}
		spawn(self.mj_proto)
	
	def at_object_creation(self):
		self.db.desc = "An adventurer."
		self.db.hp = 10
		self.db.mp = 2
		self.db.maxhp = 10
		self.db.maxmp = 2
		self.db.lvl = 1
		self.db.exp = 0
		self.db.gold = 10
		self.db.tokens = 0
		self.db.winnings = 0
		self.db.bank = 0
		self.db.defense = 2
		self.db.attack = 2
		self.db.equipatt = 0
		self.db.equipdef = 0
		self.db.shielddef = 0
		self.db.battlespells = []
		self.db.overworldspells = []
		self.db.locations = []
		self.db.chests = []
		self.db.lastcity = "#7121"
		self.db.deathcount = 0
		self.db.weaponequipped = "none"
		self.db.armorequipped = "none"
		self.db.shieldequipped = "none"
		self.db.monsterstats = {}
		self.pop_inven()
		self.tags.add("beginning")
		self.db.accolades = []
		self.db.quests = {}


	pass
