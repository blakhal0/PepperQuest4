from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class ringbell(default_cmds.MuxCommand):
	key = "Ring Bell"
	aliases = ["ring bell", "Ring bell", "ring Bell"]
	auto_help = True
	def func(self):
		if self.caller.location.key == "Titan Arena":
			self.caller.msg("|/You walk over and strike the bell, ready for battle.")
		else:
			self.caller.msg("|/You ring the bell...")
			self.caller.msg("*jinglejinglejingle*|/pspspspspspspsps, heeeeerrrree monster monster monster!")
		yield 1
		if self.caller.location.db.fight == "no":
			self.caller.msg("|/Easy there killer, there's nothing to fight in this area.")
			return
		else:
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')

class BellCmdSet(CmdSet):
	key = "BellCmdSet"
	def at_cmdset_creation(self):
		self.add(ringbell())

class monsterbell(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A small, ornate, golden bell in the shape of a monster."
		self.cmdset.add_default(BellCmdSet, permanent=True)
		self.locks.add("drop:false()")