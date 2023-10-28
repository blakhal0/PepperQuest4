from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from evennia.prototypes.spawner import spawn

class sandsoftimecmd(default_cmds.MuxCommand):
	key = "get sands of time"
	aliases = ["get sands", "Get Sands of Time", "Get Sands", "get sand", "Get Sand"]
	auto_help = True
	def func(self):
		if self.caller.tags.get("sands of time"):
			self.caller.msg("|/You reach your hand into the sands of time, but it passes through. You have already touched the sands of time, you cannot touch them again.")
			return
		if "Pendrin Guardian of Time" in self.caller.db.monsterstats.keys():
			sot_proto = {
			"key": "Sands of Time",
			"typeclass": "typeclasses.sandsoftime.sandsoftime",
			"location": self.caller
			}
			spawn(sot_proto)
			if self.caller.db.weaponequipped in ["none", "None"]:
				weapondesc = "fist"
			else:
				weapondesc = self.caller.db.weaponequipped.lower()
			self.caller.msg("You approach the sands of time and unleash a furious strike on the black orb with your %s." % (weapondesc.title()))
			self.caller.msg("The eerie green light bursts forth from the orb before fading out, the orb shatters. You reach into the flow and take a handful of sand.")
			self.caller.msg("|/You receive a handful of Sands of Time")
			self.caller.msg("You hear familiar voices, all of them your own, whispering in your head.")
			self.caller.msg("|mThousands of Versions of You|n say: You can only use it once, destiny now branches and only one path can be followed, don't make the same mistake that I did.")
			self.caller.tags.add("sands of time")
			return
		else:
			self.caller.msg("|/You reach for the sands of time...")
			self.caller.msg("*CA-CRACK*")
			self.caller.msg("A bolt of green lightning shoots out from the black orb striking you in the chest. As you are reeling, Pendrin's robes erupt in purple flame as they draw the giant key from their robes and dip it into the sands, through bleary eyes you watch the key transform into a gigantic silver full moon axe. The two blades form the shape of an hour glass.")
			self.caller.msg("|mPendrin|n says: I will not let you destroy time again!! You've damaged this world enough times! Different faces, different names, different reasons, but always you destroy! Not again, never again. I will remove your vile stain from the weave of time once and for all.")
			self.caller.tags.add("letsfight")
			self.caller.execute_cmd('fight')
			return


class SandsofTimeCmdSet(CmdSet):
	key = "SandsofTimeCmdSet"
	def at_cmdset_creation(self):
		self.add(sandsoftimecmd())

class sandsource(DefaultObject):
	def at_object_creation(self):
		self.db.desc = ""
		self.cmdset.add_default(SandsofTimeCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:false()")