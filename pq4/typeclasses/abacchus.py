from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from random import randint

class chatabacchus(default_cmds.MuxCommand):
	key = "talk abacchus"
	aliases = ["Talk Abacchus"]
	auto_help = True
	def func(self):
		if self.caller.location.key == "A Well Suited Path":
			if self.caller.tags.get(category="SuitPath") in ["spade", "heart", "club", "diamond"]:
				self.caller.msg("|/|mAbacchus|n says: You are already well suited for your path. Follow your path.")
				return
			else:
				paths = ["spade", "heart", "club", "diamond"]
				pathchoice = random.choice(paths)
				self.caller.msg("|/|mAbacchus|n says: I am Abacchus, a lesser deity of chaos and order, I preside over the trials of the House of Duality. If you wish to see the Goddesses, you must pass through the trials.")
				self.caller.msg("|mAbacchus|n says: Luck, Chaos, Misfortune, and Order, two sides of the same coin each bringing balance to the other.")
				self.caller.msg("|mAbacchus|n says: I once traveled a path with groups from different kingdoms, as we traveled they would change their dress to the local fashion.")
				self.caller.msg("Abacchus closes their eyes and puts a hand towards you.")
				self.caller.tags.add(pathchoice, category="SuitPath")
				self.caller.msg("|mAbacchus|n says: Yes, you are well suited to a path of %s. Stay on your path, stray and you risk chaos." % (pathchoice))
		elif self.caller.location.key == "Bone Shaker":
			if self.caller.tags.get(category="SuitPath"):
				self.caller.tags.remove(category="SuitPath")
			diceone = randint(1,6)
			dicetwo = randint(1,6)
			while diceone == dicetwo:
				dicetwo = randint(1,6)
			fandb = [0, 6, 5, 4, 3, 2, 1]
			backone = fandb[int(diceone)]
			backtwo = fandb[int(dicetwo)]
			self.caller.msg("|/|mAbacchus|n says: Twin beasts stare you down, six faces has each beast and twenty-one eyes.")
			answer = yield("|mAbacchus|n says: One beast stares at you with %d eyes, the other with %d.|/What do they have behind their back?" % (diceone, dicetwo))
			if "eyes" in answer:
				answer = answer.replace('eyes', '').strip()
			if answer in [str(str(backone) + " " + str(backtwo)), str(str(backone) + ", " + str(backtwo)), str(str(backone) + "," + str(backtwo)), str(int(backone) + int(backtwo))]:
				results = search_object("#9353")
				self.caller.msg("|/|mAbacchus|n says: You are wise indeed.")
				self.caller.move_to(results[0], quiet=True, move_hooks=True)
				return
			else:
				self.caller.msg("|/Abacchus flips a coin...")
				luck = randint(1,2)
				if luck == 2:
					self.caller.msg("|mAbacchus|n says: Luck is not on your side today.")
					results = search_object("#9310")
					self.caller.move_to(results[0], quiet=True, move_hooks=True)
					return
				else:
					self.caller.msg("|mAbacchus|n says: Luck favors you today. Talk to me again when you are ready.")
					return
		elif self.caller.location.key == "Luck Lab":
			if self.caller.tags.get("fortunecatappeased"):
				self.caller.msg("|/|mAbacchus|n says: You have passed all the trials, you are worthy of an audience with the goddesses of fortune and dispensing of dues. Ascend the stairs.")
				return
			else:
				self.caller.msg("|/|mAbacchus|n says: Luck is sometimes like a river, it flows. Try not to die, alchemy is dangerous.")
				self.caller.msg("Abacchus laughs a raucous laugh, stomping a hooved foot.")
				return



class AbacchusCmdSet(CmdSet):
	key = "AbacchusCmdSet"
	def at_cmdset_creation(self):
		self.add(chatabacchus())

class abacchus(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Abacchus stands in the hallway, a set of dice in one hand, a counting device with many many rows in the other. They throw the dice, then slide a bead across one of the sections."
		self.tags.add("specialnpc")
		self.cmdset.add_default(AbacchusCmdSet, permanent=True)
		self.locks.add("get:false()")