from evennia import DefaultObject, default_cmds, CmdSet
from evennia.prototypes.spawner import spawn

class getredkey(default_cmds.MuxCommand):
	key = "Get Red key"
	alias = ["get red key", "get key", "Get Key"]
	auto_help = False
	def func(self):
		amfred_proto = {
			"key": "Ardismouf Red Key",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A Red key for the Castle Ardismouf.",
			"locks": "drop:false()",
			"location": self.caller
			}
		if self.caller.search('Ardismouf Red Key', location=self.caller, quiet=True):
			self.caller.msg("You already have the Red Key.")
			return
		else:
			spawn (amfred_proto)
			self.caller.msg("You reach down and grab the Red Key.")

class SpwnRedKeyCmdSet(CmdSet):
	key = "SpwnRedKeyCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(getredkey())

class spwnredkey(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.locks.add("get:false()")
		self.locks.add("view:false()")
		self.cmdset.add_default(SpwnRedKeyCmdSet, permanent=True)