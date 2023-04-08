from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class talkmalashai(default_cmds.MuxCommand):
	key = "Talk Malashai"
	aliases = ["talk Malashai", "talk malashai", "Talk malashai"]
	auto_help = True
	def func(self):
		if not self.obj.access(self.caller, "view"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/|mMalashai|n mocks you: Ah, the savior of Hellview. Come to lend a helping hand once again? HAHAHAHAHAHA.")
		self.caller.msg("|m%s|n says: ...I brought you back into this world, and I'm going to take you back out." % (self.caller.key))
		self.caller.msg("|mMalashai|n says: I see some traits stayed strong. Arrogance, overconfidence, and stupidity. Spark of the consuming flame indeed. Ah, here it is.")
		self.caller.msg("Malashai takes an hourglass from the shelves.")
		self.caller.msg("|m%s|n says: You speak as though you know me." % (self.caller.key))
		self.caller.msg("|mMalashai|n says: I have, I will, I do. Again and again and again.|/Malashai turns to face you, gaping black eyes drinking in the light of the room.|/|mMalashai|n says: You haven't discovered the secrets of Panahon yet this time, interesting. So many times you've failed there.")
		self.caller.msg("|m%s|n says: This time? Panahon?" % (self.caller.key))
		self.caller.msg("|mMalashai|n says: Ugh, never the matter. You won't have the chance this time...")
		self.caller.msg("Malashai turns the hourglass in his hand, his form solidifying to a vaguely human shape, a dark aura surrounding him.")
		self.caller.msg("|mMalashai|n says: Ah, much better. This form is limiting in certain aspects, but it does have its advantages.")
		self.caller.tags.add("letsfight")
		self.caller.execute_cmd('fight')
		return

class TalkMalashaiCmdSet(CmdSet):
	key = "TalkMalashaiCmdSet"
	def at_cmdset_creation(self):
		self.add(talkmalashai())

class malashai(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A figure flashes in and out of view, flipping back and forth from the figure of a man, to an inky black tendriled miasma. One thing that remains consistent is the black gaping caverns for eyes."
		self.cmdset.add_default(TalkMalashaiCmdSet, permanent=True)
		self.db.get_err_msg = "Malashai laughs as you fall on your face, passing right through him."
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.locks.add("view:monnotdef(Malashai)")