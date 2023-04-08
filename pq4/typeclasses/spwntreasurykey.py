from evennia import DefaultObject, default_cmds, CmdSet, search_object
from evennia.prototypes.spawner import spawn
import random

class gettreasurykey(default_cmds.MuxCommand):
	key = "Get Treasury Key"
	alias = ["get treasury key"]
	auto_help = True
	def func(self):
		if "Guard Captain" not in self.caller.db.monsterstats.keys():
			self.caller.msg("|/You walk to the back of the room, chuckling to yourself at the ease of your impending victory. As you reach out to grasp the key a heavy gauntleted hand suddenly grabs your wrist in a metallic vice like grip.")
			self.caller.msg("|mGuard Captain|n says: HAHA!! Caught you thief scum! Now, I'm going to kill you!")
			yield 1
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')
			return
		else:
			amftreas_proto = {
			"key": "Ardismouf Treasury Key",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "Castle Ardismouf Treasury Key.",
			"locks": "drop:false()",
			"location": self.caller
			}
			if self.caller.search('Ardismouf Treasury Key', location=self.caller, quiet=True):
				self.caller.msg("You already have the Treasury Key.")
				return
			else:
				spawn (amftreas_proto)
				self.caller.msg("You step over the Guard Captain as they gasp for air on the floor and grab the Treasury Key.")
				return

class SpwnTreasuryKeyCmdSet(CmdSet):
	key = "SpwnTreasuryKeyCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(gettreasurykey())

class spwntreasurykey(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.locks.add("get:false()")
		self.locks.add("view:false()")
		self.cmdset.add_default(SpwnTreasuryKeyCmdSet, permanent=True)