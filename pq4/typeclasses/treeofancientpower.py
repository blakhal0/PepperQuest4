from evennia import search_object, default_cmds, CmdSet
from evennia.prototypes.spawner import spawn
from random import randint
import random
import typeclasses.items as items
from typeclasses.objects import DefaultObject


class praytree(default_cmds.MuxCommand):
	key = "Pray"
	aliases = ["pray"]
	auto_help = True
	def func(self):
		lw = random.choice(["powerpepper", "magicalpepper", "armoredpepper"])
		lootname = getattr(items, lw).name
		quantity = randint(1,3)
		self.caller.msg("|/|mTree of the Ancient Power|n says: You have proven yourself worthy, I give to you %s %s!|/You add the %s to your inventory." % (str(quantity), lootname, lootname))
		wt = self.caller.search(lootname, candidates=self.caller.contents, quiet=True)
		if not wt:
			sitc = "typeclasses.items.%s" % (lw)
			tc_proto = {
			"key": "%s" % (lootname),
			"typeclass": "%s" % (sitc),
			"qty": int(quantity),
			"location": self.caller
			}
			spawn(tc_proto)
		else:
			wt[0].db.qty += int(quantity)
		self.caller.msg("A warm light surrounds you and you find yourself back away from the tree.")
		results = search_object("#13041")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)

class TreeofAncientPowerCmdSet(CmdSet):
	key = "TreeofAncientPowerCmdSet,"
	def at_cmdset_creation(self):
		self.add(praytree())

class treeofancientpower(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "This gnarled, mystical tree, with its roots deeply entwined in the island's secrets and its branches heavy with the Peppers of Power, stands as a beacon of ancient wonder and a symbol of the island's unique, magical heritage."
		self.cmdset.add_default(TreeofAncientPowerCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "You give a root of the tree a tug, it doesn't move or give in any way. You feel a burning stare bore into the back of your head."