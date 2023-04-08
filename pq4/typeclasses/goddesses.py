from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
from random import randint

class chatgoddesses(default_cmds.MuxCommand):
	key = "talk goddesses"
	aliases = ["Talk Goddesses", "Talk Nemesis", "Talk Tyche"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/|mTyche|n says: Thank you, Fortunate One, for releasing us. The world is far out of balance, we have our work cut out for us.")
		self.caller.msg("|mNemesis|n says: Even I would not cause ruin on the scale that has occurred.")
		self.caller.msg("The Goddesses each touch one side of the scale...")
		if self.caller.tags.get("beginning"):
			self.caller.msg("|/|mTyche|n says: Nem wait! Look into their eyes. Do you not see it? %s, you must return home. I am sorry that it will not be a happy return. Don't delay, while your swift arrival will not change what has happened, you must make haste." % (self.caller.key))
			self.caller.tags.remove("beginning")
		self.caller.msg("A blinding light bursts forth.")
		results = search_object("#9309")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class getgoddesses(default_cmds.MuxCommand):
	key = "get goddesses"
	auto_help = False
	def func(self):
		self.caller.msg("|/|mNemesis|n shouts: You little piece of scum.")
		self.caller.msg("Nemesis raises her lash.")
		self.caller.msg("|mTyche|n says: Now now, %s did save us Nem, they made a mistake, let's give them a fair chance." % (self.caller.key))
		self.caller.msg("Nemesis and Tyche each roll a die.")
		if self.caller.tags.get("beginning"):
			self.caller.msg("|/|mTyche|n says: Nem stop! Look into their eyes. Do you not see it? %s, you must return home. I am sorry that it will not be a happy return. Don't delay, while your swift arrival will not change what has happened, you must make haste." % (self.caller.key))
			self.caller.tags.remove("beginning")
			return
		if randint(1,2) == 2:
			self.caller.msg("|/|rWhat tragic fate, your luck has run out and retribution has been served for your undeserved fortunes, today Nemesis has found you.|n|/You have brought shame to yourself and your family.")
			self.caller.db.deathcount += 1
			self.caller.db.hp = int(self.caller.db.maxhp * .5)
			self.caller.db.mp = int(self.caller.db.maxmp * .5)
			self.caller.db.gold -= int(self.caller.db.gold * .2)
			results = search_object(self.caller.db.lastcity)
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		else:
			self.caller.msg("|/|mNemesis|n grumbles: One day your fortune will run out, and when it does the last thing you will see is my smile and the last thing you will feel is the sting of my lash and edge of my blade.")
			return

class GoddessesCmdSet(CmdSet):
	key = "GoddessesCmdSet"
	def at_cmdset_creation(self):
		self.add(chatgoddesses())
		self.add(getgoddesses())

class goddesses(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Goddesses stand tall, holding the symbols of their office. They each look at you, one with a faint sense of empathy, one with a slight grin."
		self.tags.add("specialnpc")
		self.cmdset.add_default(GoddessesCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:inlist(accolades, Fortunate One)")
