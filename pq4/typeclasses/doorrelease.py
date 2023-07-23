from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class doorreleasecmd(default_cmds.MuxCommand):
	key = "Press Button"
	aliases = ["press button", "push button", "Push Button"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("pirtsdoor"):
			self.caller.tags.remove("pirtsdoor")
			self.caller.msg("|/You press the button...")
			self.caller.msg("You feel a low rumble, stone grinding on stone, followed by a thud.")
			return
		else:
			self.caller.tags.add("pirtsdoor")
			self.caller.msg("|/You press the button...")
			self.caller.msg("You feel a low rumble, stone grinding on stone.")
			return

class DoorReleaseCmdSet(CmdSet):
	key = "DoorReleaseCmdSet"
	def at_cmdset_creation(self):
		self.add(doorreleasecmd())

class doorrelease(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A stone button with a carving of a female figure, arms extended as if for an embrace, is placed on a mosaic on the wall."
		self.cmdset.add_default(DoorReleaseCmdSet, permanent=True)
		self.locks.add("get:false()")
