from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class train(default_cmds.MuxCommand):
	key = "Train"
	auto_help = True
	def func(self):
		self.caller.msg("|/You step up to the training dummy...")
		self.caller.msg("The Dummy suddenly starts to move and strikes a fighting stance!!!")
		self.caller.tags.add("letsfight")
		self.caller.execute_cmd('fight')

class TrainCmdSet(CmdSet):
	key = "TrainCmdSet"
	def at_cmdset_creation(self):
		self.add(train())

class trainingdummy(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A stout training dummy covered in padding. It looks a bit worn from repeated use."
		self.db.ruin = "The training dummy stares at you with an eerie face slowly appearing in the charred padding."
		self.cmdset.add_default(TrainCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/Master Roshi swiftly swings his cane down, cracking you across the hands with a sharp slapping noise.|/|mMaster Roshi|n says: Take my training dummy will you? You must be a dummy yourself to think I'd allow that!! *harumpff*"
	def return_appearance(self, looker):
		desc = str()
		if looker.tags.get("training"):
			desc = self.db.desc
		else:
			desc = self.db.ruin
		return desc