from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class ringgong(default_cmds.MuxCommand):
	key = "Ring Gong"
	aliases = ["ring gong", "Ring gong", "ring Gong"]
	auto_help = True
	def func(self):
		self.caller.msg("|/You walk over and strike the gong, ready for battle.")
		yield 1
		self.caller.tags.add("letsfight")
		self.caller.execute_cmd('fight')

class GongCmdSet(CmdSet):
	key = "GongCmdSet"
	def at_cmdset_creation(self):
		self.add(ringgong())

class battlegong(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A worn and dented gong and hammer hang on the wall of the arena. |cRing Gong|n to start the fight."
		self.cmdset.add_default(GongCmdSet, permanent=True)
		self.locks.add("drop:false()")