from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class wateron(default_cmds.MuxCommand):
	key = "Water On"
	aliases = ["water on"]
	auto_help = True
	def func(self):
		self.caller.db.bathhouse["water"] = "on"
		self.caller.msg("|/Grabbing the wheel and turning with all your might it begins to squeal and breaks loose. You hear water begin to gurgle and flow in the pit below, the pipes rattle and shake but the water begins to flow.")
		return

class wateroff(default_cmds.MuxCommand):
	key = "Water Off"
	aliases = ["water off"]
	auto_help = True
	def func(self):
		self.caller.db.bathhouse["water"] = "off"
		self.caller.msg("|/Grabbing the wheel and turning with all your might it begins to squeal and breaks loose. You hear the water in the pit below to slow, then come to a slow drip. Air glugs through the pipes as the water flow stops.")
		return

class WaterCmdSet(CmdSet):
	key = "WaterCmdSet"
	def at_cmdset_creation(self):
		self.add(wateron())
		self.add(wateroff())

class watercontrol(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A very large, and slightly rusty, wheel is mounted to a very large pipe on the wall. It appears to control the water flow to the bathhouse pipes. You can turn the |cWater On|n or turn the |cWater Off|n."
		self.cmdset.add_default(WaterCmdSet, permanent=True)
		self.locks.add("get:false()")
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		desc = self.db.desc
		if looker.db.bathhouse['water'] == "off":
			desc += "|/The water is currently off."
		if looker.db.bathhouse['water'] == "on":
			desc += "|/The water is currently on."
		return desc