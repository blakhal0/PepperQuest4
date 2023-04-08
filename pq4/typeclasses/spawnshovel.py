from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class getshovel(default_cmds.MuxCommand):
	key = "get shovel"
	aliases = ["Get Shovel", "Get shovel", "get Shovel" ]
	auto_help = False
	def func(self):
		for i in self.caller.contents:
			if i.key == "Shovel":
				self.caller.msg("|/You already have the shovel.")
				return
		shovel_proto = {
		"key": "Shovel",
		"typeclass": "typeclasses.objects.shovel",
		"location": self.caller
		}
		spawn(shovel_proto)
		self.caller.msg("|/You take the shovel.")

class ShovelCmdSet(CmdSet):
	key = "ShovelCmdSet"
	def at_cmdset_creation(self):
		self.add(getshovel())

class spawnshovel(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "It's invisible."
		self.cmdset.add_default(ShovelCmdSet, permanent=True)
		self.locks.add("get:false()")