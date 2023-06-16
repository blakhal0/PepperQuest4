from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class lookmirror(default_cmds.MuxCommand):
	key = "Look Mirror"
	aliases = ["Look mirror", "look Mirror", "look mirror", "l Mirror", "L Mirror", "l mirror", "L mirror"]
	auto_help = False
	def func(self):
	#Armor Desc
		if self.caller.db.armorequipped in ["None", "none"]:
			armordesc = "wearing not a single stitch of armor"
		else:
			armordesc = "clad in " + self.caller.db.armorequipped.lower()
	#Shield Desc
		if not self.caller.db.shieldequipped.lower() == "none":
			armordesc += " and a %s" % (self.caller.db.shieldequipped.lower())
	#Weapon Desc
		if self.caller.db.weaponequipped in ["none", "None"]:
			weapondesc = "clenching your bruised and bloody fists"
		else:
			weapondesc = "holding a " + self.caller.db.weaponequipped.lower()
	#Reversed character self.caller.db.desc
		mirrormirror = "".join(reversed(self.caller.db.desc))
		self.caller.msg("You gaze into the mirror and see yourself, %s, %s." % (armordesc, weapondesc))
	#Check if keyword is in description.
		if "yawrood" in self.caller.db.desc.lower():
			self.caller.msg("Looking deeper, you see a doorway.")
			self.caller.msg("You step forward slowly, passing through the mirror...")
			yield 1
			results = search_object("#10036")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		else:
			self.caller.msg("Looking deeper, you see %s." % (mirrormirror))
			return

class MirrorCmdSet(CmdSet):
	key = "MirrorCmdSet"
	def at_cmdset_creation(self):
		self.add(lookmirror())

class mirror(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A mirror."
		self.cmdset.add_default(MirrorCmdSet, permanent=True)
		self.locks.add("get:false()")