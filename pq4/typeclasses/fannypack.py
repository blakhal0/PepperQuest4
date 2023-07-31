from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class checkfannypack(default_cmds.MuxCommand):
	key = "check pack"
	aliases = ["Check Pack", "Check pack", "check Pack"]
	auto_help = True
	def func(self):
		self.caller.msg("|/Unzipping your hella fly dope ass fanny pack you see:")
		self.caller.msg("%s pepper coins." % (str(self.caller.db.tirgusmarket['foolsgold'])))
		for i in self.caller.db.tirgusmarket.keys():
			if not i == "foolsgold":
				self.caller.msg("%s %s.|/" % (self.caller.db.tirgusmarket[i]['name'], str(self.caller.db.tirgusmarket[i]['quantity'])))
		self.caller.msg("You zip your fanny pack back up.")
		return

class leavemarket(default_cmds.MuxCommand):
	key = "Leave Market"
	aliases = ["leave market", "Leave market", "leave Market"]
	auto_help = True
	def func(self):
		del self.caller.db.tirgusmarket
		for i in self.caller.contents:
			if i.key == "Fanny Pack":
				i.delete()
		self.caller.msg("|/You take off your wicked sweet kickin fanny pack and, with a tear in your eye, reluctantly turn it in and take your leave of the Eternal Bazaar.")
		results = search_object("#12877")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)


class FannyPackCmdSet(CmdSet):
	key = "FannyPackCmdSet"
	def at_cmdset_creation(self):
		self.add(checkfannypack())
		self.add(leavemarket())

class fannypack(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "One dope ass fanny pack. On the front is printed 'I shopped my fanny off at the Eternal Bazaar'"
		self.cmdset.add_default(FannyPackCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("drop:false()")
