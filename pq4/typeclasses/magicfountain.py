from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class fountaincmd(default_cmds.MuxCommand):
	key = "Use Fountain"
	auto_help = True
	def func(self):
		self.caller.db.mp = self.caller.db.maxmp
		self.caller.msg("|/A wave of power washes over you as your magic reserves replenish.")
		return

class FountainCmdSet(CmdSet):
	key = "FountainCmdSet"
	def at_cmdset_creation(self):
		self.add(fountaincmd())

class magicfountain(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The magical fountain is a small, ornate structure made of polished stone and decorated with intricate carvings of arcane symbols and runes. It is situated in a quiet corner, surrounded by small patches of plants fed by the excess of the fountain.|/|cUse Fountain|n to replenish your magic reserves."
		self.cmdset.add_default(FountainCmdSet, permanent=True)
		self.locks.add("get:false()")