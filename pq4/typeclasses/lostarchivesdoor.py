from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class depthsofknowledgedoor(default_cmds.MuxCommand):
	key = "Lost Archives"
	aliases = ["Lost archives", "lost Archives", "lost archives"]
	auto_help = False
	def func(self):
		def dothemove():
			self.caller.msg("|/|mScholar|n says: You are both wise and knowledgeable. Your request to enter has been granted.")
			results = search_object("#9832")
			self.caller.move_to(results[0], quiet=True, move_hooks=True)
			return
		def wronganswer():
			self.caller.msg("|/|mScholar|n says: If your mind was a library, it would be full of children's picture books.")
			return
		self.caller.msg("|/You grasp the door and put all your effort into opening it, the door does not budge. Slowly, a wispy blue form begins to envelop the door. The ghost of an ancient scholar emerges.")
		self.caller.msg("|mScholar|n says: Beyond this door lays immense and dangerous knowledge. What is the password?")
		answer = yield("How do you answer? ")
		if answer == "2961":
			dothemove()
			return
		else:
			wronganswer()
			return

class DepthsofKnowledgeDoorCmdSet(CmdSet):
	key = "DepthsofKnowledgeDoorCmdSet"
	def at_cmdset_creation(self):
		self.add(depthsofknowledgedoor())

class lostarchivesdoor(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A heavy wooden door with iron straps blocks your entrance to the Lost Archives."
		self.tags.add("specialexit")
		self.cmdset.add_default(DepthsofKnowledgeDoorCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.db.get_err_msg = "|/|rThe door is firmly attached to the door frame and does not budge.|n"