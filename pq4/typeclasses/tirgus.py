from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class chattirgus(default_cmds.MuxCommand):
	key = "talk tirgus"
	aliases = ["Talk Tirgus", "Talk tergus", "talk Tirgus"]
	auto_help = True
	def func(self):
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "Raijin" in contentslist or "raijin" in self.caller.db.battlespells:
			self.caller.msg("|/|mThe Mother of Markets|n says: You've already proven yourself a most thrifty shopper. There's no need for further challenges.")
		else:
			if self.caller.db.tirgusmarket['foolsgold'] >= 3000000:
				self.caller.msg("|/|mThe Mother of Markets|n says: Child, you have proven yourself worthy. Receive my gift, use it to destroy those that would attempt to exact a high price.")
				rai_proto = {
				"key": "Raijin",
				"typeclass": "typeclasses.items.raijinspellbook",
				"location": self.caller
				}
				spawn(rai_proto)
				self.caller.msg("|/You receive a spell book.")
			else:
				self.caller.msg("|/|mThe Mother of Markets|n says: Welcome to the Eternal Bazaar my child. If you wish to prove your worthiness, go forth and trade! Return to me with 3 million pepper coins to demonstrate your prudence, thrift, and deal making wisdom.")
				self.caller.msg("Tirgus gives you a big smile and shuffles you along.")
				self.caller.msg("|mThe Mother of Markets|n says: If you find yourself all shopped out, or just want to leave, you can |cLeave Market|n to return to the world. BUT, all your trades, deals, and coins will be lost once you leave. And we'll need to take the fanny pack back, its awesomeness would destroy the fabric of your reality.")
				return
		self.caller.db.hp = self.caller.db.maxhp
		self.caller.db.mp = self.caller.db.maxmp
		self.caller.msg("|/|mTirgus|n says: Return to your world child, and remember to never pay sticker price!")
		del self.caller.db.tirgusmarket
		for i in self.caller.contents:
			if i.key == "Fanny Pack":
				i.delete()
		results = search_object("#11211")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)


class TirgusCmdSet(CmdSet):
	key = "TirgusCmdSet"
	def at_cmdset_creation(self):
		self.add(chattirgus())

class tirgus(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Adorned in a flowing and intricately woven robe of rich silk, dyed in a kaleidoscope of colors, the fabric glimmering with iridescent threads, stands Tirgus. Her fingers are adorned with an assortment of rings, ears decorated with finely crafted earrings that sway gently with her movements each holding a different charm or trinket. Her eyes gleam green as she smiles at you."
		self.cmdset.add_default(TirgusCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")