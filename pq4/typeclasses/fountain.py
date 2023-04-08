from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class rechargemp(default_cmds.MuxCommand):
	key = "Chargemp"
	auto_help = True
	def func(self):
		if self.caller.tags.get("mpcharge"):
			self.caller.msg("|/The fountain has not replenished, you have to wait to use it again.")
			return
		elif self.caller.db.mp == self.caller.db.maxmp:
			self.caller.msg("|/Your MP is already at the maximum level, there is no need to use the fountain.")
			return
		else:
			self.caller.tags.add("mpcharge")
			self.caller.db.mp = self.caller.db.maxmp
			self.caller.msg("|/You drink deep from the bubbling fountain, restoring your MP.|/The fountain is now depleted and will need time to refill before it can be used again.")
			yield 80
			self.caller.tags.remove("mpcharge")
			return

class RechargeMPCmdSet(CmdSet):
	key = "RechargemPCmdSet"
	def at_cmdset_creation(self):
		self.add(rechargemp())

class fountain(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The fountain is full."
		self.db.depleteddesc = "The fountain is empty."
		self.cmdset.add_default(RechargeMPCmdSet, permanent=True)
		self.locks.add("get:false()")
	def return_appearance(self, looker):
		if not looker:
			return ""
		if looker.tags.get("mpcharge"):
			desc = self.db.depleteddesc
		else:
			desc = self.db.desc
		return desc
