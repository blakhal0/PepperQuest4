from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class gettorch(default_cmds.MuxCommand):
	key = "get torch"
	aliases = ["Get Torch", "Get torch", "get Torch" ]
	auto_help = False
	def func(self):
		if self.caller.tags.get("thekingisdead"):
			self.caller.msg("|/You try to take the torch, it's stuck. Apparently they've nailed it to the wall.|/|mGuard|n says: We had to nail it down, some jerk prisoner stole one and I had to pay for it.")
			return
		for i in self.caller.contents:
			if i.key == "Torch":
				self.caller.msg("|/You already have the torch.")
				return
		torch_proto = {
		"key": "Torch",
		"typeclass": "typeclasses.objects.torch",
		"location": self.caller
		}
		spawn(torch_proto)
		self.caller.msg("|/You take the torch out of the holder on the wall.")

class TorchCmdSet(CmdSet):
	key = "TorchCmdSet"
	def at_cmdset_creation(self):
		self.add(gettorch())

class torchholder(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "It's invisible."
		self.cmdset.add_default(TorchCmdSet, permanent=True)
		self.locks.add("view:false()")
		self.locks.add("get:false()")