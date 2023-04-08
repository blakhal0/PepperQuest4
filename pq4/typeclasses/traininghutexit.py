from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class enter(default_cmds.MuxCommand):
	key = "Training Hut"
	aliases = ["training hut", "South", "s", "south", "S"]
	auto_help = False
	def func(self):
		target = self.caller.search("Training Hut")
		if self.caller.tags.get("beginning"):
			self.caller.tags.add("training")
			place = target.db.thut
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.msg("|/" + self.caller.at_look(self.caller.location))
			return
		else:
			place = target.db.burnedhut
			results = search_object("%s" % (place))
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			self.caller.msg("|/" + self.caller.at_look(self.caller.location))
			return

class EnterCmdSet(CmdSet):
	key = "EnterCmdSet"
	def at_cmdset_creation(self):
		self.add(enter())
	
class traininghutexit(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The door to Master Roshi's training hut stands open, welcoming all who wish to learn."
		self.db.thut = "#7229"
		self.db.burnedhut = "#7231"
		self.cmdset.add_default(EnterCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialexit")