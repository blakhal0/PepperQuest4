from evennia import DefaultObject, default_cmds, CmdSet, search_object
from evennia.prototypes.spawner import spawn
import random

class getbluekey(default_cmds.MuxCommand):
	key = "Open Drawer"
	alias = ["open drawer"]
	auto_help = True
	def func(self):
		answer = yield("|/Which drawer would you like to open?")
		if answer.lower() in ["ac", "ag", "al", "am", "ar", "as", "at", "au", "b", "ba", "be", "bh", "bi", "bk", "br", "c", "cd", "ce", "cf", "cl", "cm", "co", "cr", "cs", "cu", "ds", "db", "dy", "er", "es", "eu", "f", "fe", "fm", "fr", "ga", "gd", "ge", "h", "he", "hf", "hg", "ho", "hs", "i", "in", "ir", "k", "kr", "la", "li", "lr", "lu", "md", "mg", "mn", "mo", "mt", "n", "na", "nb", "nd", "ne", "ni", "no", "np", "o", "os", "p", "pa", "pb", "pd", "pm", "po", "pr", "pt", "pu", "ra", "rb", "re", "rf", "rg", "rh", "rn", "ru", "s", "sb", "sc", "se", "sg", "si", "sm", "sn", "sr", "ta", "tb", "tc", "te", "th", "ti", "tl", "tm", "u", "v", "w", "xe", "y", "yb", "zn", "zr"]:
			deaths = ["A plague riddled rat leaps from the drawer onto your face and begins to eat your eyeballs.", "You hear a slight click noise, a whirring blade removes your head from your shoulders.", "Huh, this one was just holding a bunch of dust. How odd... OH MY GOD IT'S FACE REMOVING DUST!!! Your face falls off.", "An itty bitty dragon pokes its head out of the drawer, aww what a cutie. Oh, look, it's yawning! You erupt into flames.", "You reach your hand into the drawer, it suddenly slams shut! You pull you arm back, whew, that was a close one. Oh, nope, you're missing a hand and rapidly bleeding to death."]
			fate = random.choice(deaths)
			self.caller.msg("|/You carefully open the drawer...")
			self.caller.msg(fate)
			self.caller.msg("|/|rWhat tragic fate, you have died.|n")
			self.caller.db.deathcount += 1
			self.caller.db.hp = int(self.caller.db.maxhp * .5)
			self.caller.db.mp = int(self.caller.db.maxmp * .5)
			self.caller.db.gold -= int(self.caller.db.gold * .2)
			results = search_object(self.caller.db.lastcity)
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		elif answer.lower() == "ca":
			amfblue_proto = {
			"key": "Ardismouf Blue Key",
			"typeclass": "typeclasses.objects.DefaultObject",
			"desc": "A Blue key for the Castle Ardismouf.",
			"locks": "drop:false()",
			"location": self.caller
			}
			if self.caller.search('Ardismouf Blue Key', location=self.caller, quiet=True):
				self.caller.msg("You already have the Blue Key.")
				return
			else:
				spawn (amfblue_proto)
				self.caller.msg("You wince slightly and carefully open the drawer labeled Ca.|/|gBEHOLD! You found the Blue Key!|n|/You grab the Blue Key.")
				return
		else:
			self.caller.msg("|/You search the drawers high and low, but can't find a drawer labeled %s." % (answer))
			return

class SpwnBlueKeyCmdSet(CmdSet):
	key = "SpwnBlueKeyCmdSet"
	priority = 4
	mergetype = "Union"
	def at_cmdset_creation(self):
		self.add(getbluekey())

class spwnbluekey(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Small drawers line one wall, all with strange little markings each handle, some single letters, some with two, but none with three, there are small numbers below the handles. It starts in the top right hand corner with H and a 1 and ends with Mt and 109. The numbers, while important, don't seem critical to opening the drawers. Maybe you want to try |cOpen Drawer|n."
		self.locks.add("get:false()")
		self.cmdset.add_default(SpwnBlueKeyCmdSet, permanent=True)