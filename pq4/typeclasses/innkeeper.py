from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatinnkeeper(default_cmds.MuxCommand):
	key = "talk innkeeper"
	aliases = ["Talk Innkeeper", "Talk innkeeper", "talk Innkeeper" ]
	auto_help = True
	def func(self):
		target = self.caller.search("innkeeper")
		def nonsense():
			self.caller.msg("|/|mInnkeeper|n says: %s" % (target.db.nonsensemsg))
			leave()
		def leave():
			self.caller.msg("|/|mInnkeeper|n says: %s" % (target.db.leavemsg))
			return
		self.caller.msg("|/|mInnkeeper|n says: %s" % (target.db.welcomemsg))
		answer = yield("What can I do for you?|/|cS|ntay at the inn, |cR|numors, |cE|nxit")
	#Exit
		if answer.lower() in ["e", "exit"]:
			leave()
			return
	#Rumors
		elif answer.lower() in ["r", "rumors"]:
			if target.db.rumors == "":
				self.caller.msg("|mInnkeeper|n says: Sorry, I don't know any rumors. Not much one for gossip.")
				leave()
			else:
				self.caller.msg("|mInnkeeper|n says: %s" % (target.db.rumors))
				leave()
	#Stay
		elif answer.lower() in ["s", "stay"]:
			self.caller.msg("|mInnkeeper|n says: Oh, well let me take a look and see if we've got anything.")
			price = int(self.caller.db.lvl) * 6
			if self.caller.db.gold < int(price):
				self.caller.msg("|mInnkeeper|n says: I'm very sorry, it appears we don't have any rooms for someone of your...ummm... meager means. Rooms cost %d gold." % (int(price)))
				leave()
			else:
				self.caller.msg("|mInnkeeper|n says: Let's see here, that'll be %d for the night." % (int(price)))
				stayanswer = yield("Stay at the Inn? |cY|nes, |cN|no.")
				if stayanswer.lower() in ["y", "yes"]:
					self.caller.db.gold -= int(price)
					self.caller.msg("|mInnkeeper|n says: Fantastic, let me show you to your room.")
					self.caller.msg("You bed down for the night and awake feeling well rested.")
					self.caller.db.hp = int(self.caller.db.maxhp)
					self.caller.db.mp = int(self.caller.db.maxmp)
					yield 1
					self.caller.msg("Your Health and Magic have been restored.")
					self.caller.execute_cmd('look')
					return
				if stayanswer.lower() in ["n", "no"]:
					self.caller.msg("|mInnkeeper|n says: Well that's a shame, we've got really comfy beds. If you change your mind, just let me know!")
					leave()
		else:
			nonsense()


class InnkeeperCmdSet(CmdSet):
	key = "InnkeeperCmdSet"
	def at_cmdset_creation(self):
		self.add(chatinnkeeper())

class innkeeper(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The innkeeper is busy attending to patrons."
		self.db.rumors = ""
		self.db.leavemsg = "Bye-bye! Take care now ya-hear!"
		self.db.welcomemsg = "Well hi there traveler, welcome to Winkers!"
		self.db.nonsensemsg = "What in the world are you saying? Oh no, I'm not dealing with a lunatic again. Last time I let one of you stay here it took a week to get the smell out."
		self.tags.add("specialnpc")
		self.cmdset.add_default(InnkeeperCmdSet, permanent=True)
		self.locks.add("get:false()")