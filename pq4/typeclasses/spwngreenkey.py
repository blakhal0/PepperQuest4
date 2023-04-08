from evennia import default_cmds, search_object, CmdSet, DefaultObject
from evennia.prototypes.spawner import spawn

class getgreenkey(default_cmds.MuxCommand):
	key = "Pick a Pepper"
	alias = ["pick a pepper"]
	auto_help = False
	def func(self):
		answer = yield("|/You lift the dome cautiously... the humid air escaping burns your eyes and makes your skin itch.|/Which pepper plant would you like to look at? Tyrant, Rex, Duality, Blood, Sevenhells, or Loyal?")
		if answer.lower() in ["blood"]:
			amfgreen_proto = {
			"key": "Ardismouf Green Key",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A Green key for the Castle Ardismouf.",
			"locks": "drop:false()",
			"location": self.caller
			}
			if self.caller.search('Ardismouf Green Key', location=self.caller, quiet=True):
				self.caller.msg("You already have the Green Key.")
				return
			else:
				spawn (amfgreen_proto)
				self.caller.msg("|/With great caution you carefully pick up the planter holding the blood peppers revealing the Green Key.|/You grab the Green Key.")
				return
		elif answer.lower() in ["tyrant", "rex", "duality", "sevenhells", "loyal"]:
			self.caller.msg("|/Your skin immediately begins to blister, hellfire climbs up your arm, seizing your chest in wracking agony.")
			self.caller.msg("|/|rWhat tragic fate, you have died.|n")
			self.caller.db.deathcount += 1
			self.caller.db.hp = int(self.caller.db.maxhp * .5)
			self.caller.db.mp = int(self.caller.db.maxmp * .5)
			self.caller.db.gold -= int(self.caller.db.gold * .2)
			results = search_object(self.caller.db.lastcity)
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|/There's no %s to pick up." % (answer.lower()))
			return

class SpwnGreenKeyCmdSet(CmdSet):
	key = "SpwnGreenKeyCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(getgreenkey())

class spwngreenkey(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.locks.add("get:false()")
		self.locks.add("view:false()")
		self.cmdset.add_default(SpwnGreenKeyCmdSet, permanent=True)