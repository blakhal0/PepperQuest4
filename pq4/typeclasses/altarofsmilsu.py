from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class smilsucmd(default_cmds.MuxCommand):
	key = "Pray"
	auto_help = True
	def func(self):
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "Horrorcane" in contentslist or "horrorcane" in self.caller.db.battlespells:
			self.caller.msg("|/|mThe Mother of Sands|n says: You have already received my gift. Do not be a greedy child.")
		else:
			self.caller.msg("|/|mThe Mother of Sands|n says: Child, you have proven yourself worthy. Receive my gift, use it to drive your enemies to their knees and scatter their very souls to the winds, send them back into my embrace.")
			tow_proto = {
			"key": "Horrorcane",
			"typeclass": "typeclasses.items.horrorcanespellbook",
			"location": self.caller
			}
			spawn(tow_proto)
			self.caller.msg("|/You receive a spell book.")
		self.caller.msg("|/|mSmilsu|n says: Return to the world and make your mother proud.")
		results = search_object("#8878")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)

class SmilsuAltarCmdSet(CmdSet):
	key = "SmilsuAltarCmdSet"
	def at_cmdset_creation(self):
		self.add(smilsucmd())

class altarofsmilsu(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Circling around to the front, you look up into the face of Smilsu, the Mother of Sands. Sand pours from her upturned palms onto the ground down upon carvings of skeletons."
		self.cmdset.add_default(SmilsuAltarCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/You hear a soft amused laugh on the wind.|/|mThe Mother of Sands|n says: Now, now, I am with you always child, there is no need to take my altar."