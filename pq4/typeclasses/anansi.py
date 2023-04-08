from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class anansifight(default_cmds.MuxCommand):
	key = "Talk Anansi"
	aliases = ["talk anansi", "Talk anansi", "talk Anansi"]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mAnansi|n says: Well well well, you come to my temple, but you're not a disciple of mine. That means you must be food.")
		self.caller.msg("|mOm|n says: You invade and desecrate MY temple, and then you THREATEN ME?")
		self.caller.msg("|mOm|n says: Take care of this interloper %s." % (self.caller.key))
		self.caller.msg("|m%s|n says: Wait what? I have to fight this thing? I was not made aware of this part of the deal." % (self.caller.key))
		self.caller.msg("|mAnansi|n says: HAHAhahahaha, well I must ask then my friend? Are you prepared to die?")
		answer = yield("Have you made peace with your chosen gods? Are you prepared to fight a god and die?|/|gY|nes, |gN|no")
		if answer.lower() in ["y", "yes"]:
			self.caller.msg("|mAnansi|n says: Excellent, you should always keep a close relationship with your god. You're about to be very close to your new god.")
		elif answer.lower() in ["n", "no"]:
			self.caller.msg("|mAnansi|n says: How very unfortunate, lucky for you I will be your new god now, and I accept your death.")
		else:
			self.caller.msg("|mAnansi|n says: *sigh* It is very saddening to see an opponent lose their wits from fear. But I am used to it.")
		yield 3
		self.caller.tags.add("letsfight")
		self.caller.execute_cmd('fight')

class AnansiCmdSet(CmdSet):
	key = "AnansiCmdSet"
	def at_cmdset_creation(self):
		self.add(anansifight())

class anansi(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The spider god focuses its many eyes on you."
		self.cmdset.add_default(AnansiCmdSet, permanent=True)
		self.locks.add("get:false()")