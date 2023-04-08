from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class whistle(default_cmds.MuxCommand):
	key = "Whistle"
	aliases = ["whistle"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You bring the whistle to your lips and blow...")
		self.caller.msg("A sweet harmonious tune floats through the air.")
		yield 1
		if self.caller.location.db.fight == "no":
			self.caller.msg("|/Easy there killer, there's nothing to fight in this area.")
			return
		else:
			self.caller.tags.add("letsfight")
			self.caller.tags.add("fightrare")
			self.caller.execute_cmd('fight')

class WhistleCmdSet(CmdSet):
	key = "WhistleCmdSet"
	def at_cmdset_creation(self):
		self.add(whistle())

class monsterwhistle(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A red crystal whistle covered with intricate carvings of rare monsters."
		self.cmdset.add_default(WhistleCmdSet, permanent=True)
		self.locks.add("drop:false()")