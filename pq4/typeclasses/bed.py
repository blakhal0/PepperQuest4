from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class sleepytime(default_cmds.MuxCommand):
	key = "sleep"
	auto_help = True
	def func(self):
		self.caller.msg("|/You lay down and burrow under the thick warm blankets, quickly falling asleep.")
		self.caller.db.hp = self.caller.db.maxhp
		self.caller.db.mp = self.caller.db.maxmp
		yield 3
		self.caller.msg("|/You wake feeling refreshed.")
		return

class BedCmdSet(CmdSet):
	key = "BedCmdSet"
	def at_cmdset_creation(self):
		self.add(sleepytime())

class bed(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A simple yet sturdy bed, carved from bone, covered with thick warm fur and blankets. Decorated skulls adorn the four posts."
		self.cmdset.add_default(BedCmdSet, permanent=True)
		self.locks.add("get:false()")