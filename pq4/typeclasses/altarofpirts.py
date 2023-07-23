from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class pirtscmd(default_cmds.MuxCommand):
	key = "Pray"
	auto_help = True
	def func(self):
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "KhioneKiss" in contentslist or "khionekiss" in self.caller.db.battlespells:
			self.caller.msg("|/|mThe Mother of Bathhouses|n says: You have already received my gift. Do not be a greedy child and remember to clean behind your ears.")
		else:
			self.caller.msg("|/|mThe Mother of Bathhouses|n says: Child, you have proven yourself worthy. Receive my gift, use it to clean from the face of this mortal world the worst of the filth which you are able.")
			tow_proto = {
			"key": "KhioneKiss",
			"typeclass": "typeclasses.items.khionekissspellbook",
			"location": self.caller
			}
			spawn(tow_proto)
			self.caller.msg("|/You receive a spell book.")
		self.caller.db.hp = self.caller.db.maxhp
		self.caller.db.mp = self.caller.db.maxmp
		self.caller.msg("|/|mPirts|n says: Return to the world, wash clean that which is filthy.")
		results = search_object("#11211")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)

class PirtsAltarCmdSet(CmdSet):
	key = "PirtsAltarCmdSet"
	def at_cmdset_creation(self):
		self.add(pirtscmd())

class altarofpirts(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A smiling woman with deep lines in her face beams happiness, warmth, and care as she washes a chubby smiling child."
		self.cmdset.add_default(PirtsAltarCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/You hear a soft amused laugh on the wind.|/|mThe Mother of Bathhouses|n says: Now, now, I am with you always child, there is no need to take my altar."