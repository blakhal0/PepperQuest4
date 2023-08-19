from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn


class chatkarl(default_cmds.MuxCommand):
	key = "talk karl"
	aliases = ["talk Karl", "Talk karl", "Talk Karl"]
	auto_help = False
	def func(self):
		for i in self.caller.contents:
			if i.key == "Fatbeards Key":
				self.caller.msg("|/Karl gives you the stink eye, poops, then flaps his wings.")
				return
		self.caller.msg("Karl begins to make an unusual gurgling sound and pukes up a key.")
		fbk_proto = {
		"key": "Fatbeards Key",
		"typeclass": "typeclasses.objects.nodropobj",
		"desc": "The fabled key of the pirate Fat Beard.",
		"location": self.caller
		}
		spawn(fbk_proto)
		self.caller.msg("|/You pick up the seagull vomit covered key, it's Fatbeards Treasure Key!!")

class KarlCmdSet(CmdSet):
	key = "KarlCmdSet"
	def at_cmdset_creation(self):
		self.add(chatkarl())

class karl(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A seagull stands on a rock, making a very annoying mewing sound."
		self.cmdset.add_default(KarlCmdSet, permanent=True)
		self.locks.add("get:false()")