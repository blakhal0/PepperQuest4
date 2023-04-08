from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class chatcasinohost(default_cmds.MuxCommand):
	key = "talk casino host"
	aliases = ["Talk Casino Host", "Talk Casino host", "Talk casino Host", "talk Casino Host", "talk Casino host", "talk casino Host" ]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
		if "High Roller" in self.caller.db.accolades:
			self.caller.msg("|/|mCasino Host|n says: Ah, %s, welcome back. I do hope you've been having a wonderful time here and enjoying the finer amenities a patron such as yourself is entitled to." % (self.caller.key))
			return
		if self.caller.db.tokens > 10000 or self.caller.db.winnings > 10000:
			self.caller.msg("|/|mCasino Host|n says: Welcome to the Golden Parliament Casino, I can see you're a player of exceptional skill and ability. For our more exceptional customers such as yourself we offer a very exclusive High Limit room. Just let me get you added to the list.... and there we are. Please, enjoy your time here and good luck!")
			self.caller.db.accolades.append("High Roller")
			return
		else:
			self.caller.msg("|/|mCasino Host|n says: Welcome to the Golden Parliament Casino, I hope you're enjoying yourself! Go and win! Good luck!")
			return

class CasinoHostCmdSet(CmdSet):
	key = "CasinoHostCmdSet"
	def at_cmdset_creation(self):
		self.add(chatcasinohost())

class casinohost(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Straight backed, with a beaming smile, the casino host greets the players at the tables wishing them luck."
		self.tags.add("specialnpc")
		self.cmdset.add_default(CasinoHostCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:inlist(accolades, Fortunate One)")