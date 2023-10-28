from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatnuri(default_cmds.MuxCommand):
	key = "talk nuri"
	aliases = ["Talk Nuri"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mNuri|n says: Oh, loving sibling, you thought you would save me? Thought to be my protector, that I did not seek to hold this power? Do you really think you are the only one with the desire to live forever and rule? After these many centuries of birth and rebirth, watching you fail pathetically at every turn I finally marshaled all the pieces into place.")
		self.caller.msg("HAHAHAHAHAHAHAHAHAHA. BWAHAHAHAHAHAHAHAHAHA!!!!!!!")
		self.caller.msg("Nuri bursts into flame as her flesh rips and stretches. Fiery horns curling from her head, black shimmering eyes staring down at you as her figure grows, skin replaced by that familiar charred, cracked black flesh with burning red embers glowing beneath.")
		self.caller.msg("|mThe Demon Goddess Pyretta|n says: Did it really never occur to you that the same blood flows in my veins? That the same hunger for power would not be my appetite?")
		self.caller.msg("The last vestiges of your sister slough to the ground, the fiery demonic form of Pyretta towering over you. The red embers glowing under her skin burst into flame, dripping napalm blood whistling through the air before splashing and igniting on the ground.")
		self.caller.msg("|mThe Demon Goddess Pyretta|n says: I thought to offer you a place at my side after every last assassin I set in your path failed. But I cannot tolerate such a miserable pathetic wretch to carry my banner. There will be no more cycle of life for you. This time I end your foolish floundering forever.")
		self.caller.msg("The Demon Goddess Pyretta arches back echoing a mourning wail as walls of flames rise, surrounding and trapping you with nowhere to run.")
		yield 3
		results = search_object("#12991")
		self.caller.move_to(results[0], quiet=True, move_hooks=False)
		self.caller.tags.add("letsfight")
		self.caller.execute_cmd('fight')

class NuriCmdSet(CmdSet):
	key = "NuriCmdSet"
	def at_cmdset_creation(self):
		self.add(chatnuri())

class nuri(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A twisted form of your sister stands before you, grinning, cheeks ripped revealing jagged fangs."
		self.tags.add("specialnpc")
		self.cmdset.add_default(NuriCmdSet, permanent=True)
		self.locks.add("get:false()")