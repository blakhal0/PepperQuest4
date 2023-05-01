from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class readtrapbook(default_cmds.MuxCommand):
	key = "Read Your Fate"
	aliases = ["Read Your fate", "Read your fate", "Read your Fate", "read Your Fate", "read Your fate", "read your fate", "read your Fate"]
	auto_help = False
	def func(self):
		fates = ["land hard, narrowly missing a large pile of nasty looking spikes. You look up and see the trap door give way, it falls crushing you.", "fall hard, breaking your legs. You spend days wailing for help slowly starving to death.", "step back quickly avoiding the trap. Whew, that was close. *creeeeeeek* *SMASH*. You are crushed by a falling bookshelf.", "are suddenly wrapped in tentacles, struggling and scraping you claw to pull yourself free as you are slowly pulled toward a large snapping beak. *CRUNCH CRUNCH* You pass out in pain as your legs become a snack."]
		self.caller.msg("|gYour Fate|n|/The tragic end of %s.|/|/You pick the book up off the floor, brush some dust off of it and begin to read... but a trap door in the floor suddenly opens!|/You %s" % (self.caller.key, random.choice(fates)))
		self.caller.msg("|/|rWhat tragic fate, you died.|/You have brought shame to yourself and your family.")
		self.caller.db.deathcount += 1
		self.caller.db.hp = int(self.caller.db.maxhp * .5)
		self.caller.db.mp = int(self.caller.db.maxmp * .5)
		self.caller.db.gold -= int(self.caller.db.gold * .2)
		results = search_object(self.caller.db.lastcity)
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		return

class TrapBookCmdSet(CmdSet):
	key = "TrapBookCmdSet"
	def at_cmdset_creation(self):
		self.add(readtrapbook())

class booktrap(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "|/You pick up the book and look at the title pressed in to the cover: The untimely and tragic fate of "
		self.cmdset.add_default(TrapBookCmdSet, permanent=True)
		self.locks.add("get:false()")
	def return_appearance(self, looker):
		desc = str()
		desc = self.db.desc + " " + looker.key
		return desc