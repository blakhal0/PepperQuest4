from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject

class tunecmd(default_cmds.MuxCommand):
	key = "Tune"
	auto_help = True
	def func(self):
		target = self.caller.search("Travel Statue", quiet=True)
		if not target:
			target = search_tag("specialtravelstatue").filter(db_location=self.caller.location)
			target = self.caller.search(target[0])
		else:
			target = target[0]
		if target.db.locationname in self.caller.db.locations:
			self.caller.msg("|/You have already leaned this location.")
			return
		else:
			self.caller.db.locations.append(target.db.locationname)
			self.caller.msg("|/You study the area closely, committing even the smallest detail to memory.")
			self.caller.msg("You are now able to travel to %s with the Travel spell and Faster Feather." % (target.db.locationname.title()))
		return

class TuneCmdSet(CmdSet):
	key = "TuneCmdSet"
	def at_cmdset_creation(self):
		self.add(tunecmd())

class travelstatue(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A statue of a feathered wing made from glowing white crystal.|/Use the |cTune|n command to learn this location."
		self.db.locationname = ""
		self.cmdset.add_default(TuneCmdSet, permanent=True)
		self.locks.add("get:false()")