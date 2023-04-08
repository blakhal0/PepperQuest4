from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject


class travelterminalcmd(default_cmds.MuxCommand):
	key = "Use Terminal"
	aliases = ["use terminal"]
	auto_help = True
	def func(self):
		target = self.caller.search("Travel Terminal")
		results = search_object(target.db.traveldestination)
		self.caller.msg("|/You place your hand on the terminal, a prismatic light engulfs you.")
		yield 1
		self.caller.move_to(results[0], quiet=True, move_hooks=True)
		return
		
class TravelTerminalCmdSet(CmdSet):
	key = "TravelTerminalCmdSet"
	def at_cmdset_creation(self):
		self.add(travelterminalcmd())

class travelterminal(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A waist high crystal pedestal twists up from the ground. A small feather is carved into a recessed hand print on the top. Colors flash up and down in the twisting crystal pillars that form the travel terminal."
		self.db.traveldestination = "#XXXX"
		self.cmdset.add_default(TravelTerminalCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/Passers by look at you oddly as you attempt to slide your pocket over the top of the terminal and slide down it, try as you might it won't fit."