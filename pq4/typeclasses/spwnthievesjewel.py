from evennia import DefaultObject, default_cmds, CmdSet, search_object
from evennia.prototypes.spawner import spawn

class getthievesjewel(default_cmds.MuxCommand):
	key = "Get Thieves Jewel"
	alias = ["get thieves jewel", "get the thieves jewel", "Get The Thieves Jewel"]
	auto_help = True
	def func(self):
		tjewl_proto = {
		"key": "Thieves Jewel",
		"typeclass": "typeclasses.objects.DefaultObject",
		"desc": "A stunningly deep blue, almost black, sapphire.",
		"locks": "drop:false()",
		"location": self.caller
		}
		if self.caller.search('Thieves Jewel', location=self.caller, quiet=True):
			self.caller.msg("You already have the Thieves Jewel.")
			return
		elif self.caller.tags.get("kingofthieves"):
			self.caller.msg("Haven't you ever heard the old saying about returning to the scene of the crime? There's nothing left to steal in here.")
			return
		else:
			spawn (tjewl_proto)
			self.caller.msg("Delicately, as if you could break it, you lift the Thieves Jewel off the satin pillow.|/Even in this light its beauty is mesmerizing. You quickly tuck it into your pocket.")
			return

class SpwnThievesJewelCmdSet(CmdSet):
	key = "SpwnThievesJewelCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(getthievesjewel())

class spwnthievesjewel(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.locks.add("get:false()")
		self.locks.add("view:false()")
		self.cmdset.add_default(SpwnThievesJewelCmdSet, permanent=True)