from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject

class chatssinnkeeper(default_cmds.MuxCommand):
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
		if "Fortunate One" in self.caller.db.accolades:
			self.caller.msg("|/|mInnkeeper|n says: %s" % (target.db.accoladewelcomemsg))
		else:
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


class SSInnkeeperCmdSet(CmdSet):
	key = "InnkeeperCmdSet"
	def at_cmdset_creation(self):
		self.add(chatssinnkeeper())

class silversandsinnkeeper(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A gaunt man in rough spun clothing stares at you unbelieving as you walk in."
		self.db.accoladedesc = "A jolly innkeeper in fine cloth welcomes you and motions for you to come over."
		self.db.rumors = "They say there's an oasis in the middle of the desert, all I've ever seen is a giant sand storm."
		self.db.leavemsg = "Don't let the Sands slip through your fingers!"
		self.db.welcomemsg = "Whuu, who are you? Where did you come from? How do you have money??? Oh, forgive me, I forget my manners these days.|/Welcome to the Silver Sands Inn."
		self.db.accoladewelcomemsg = "Ahh! Hello, hello, hello. Welcome to the Silver Sands Inn! Please come in, let's get you a room."
		self.db.nonsensemsg = "What in the world are you saying? Oh no, I'm not dealing with a lunatic again. Last time I let one of you stay here it took a week to get the smell out."
		self.tags.add("specialnpc")
		self.cmdset.add_default(SSInnkeeperCmdSet, permanent=True)
		self.locks.add("get:false()")
	def return_appearance(self, looker):
		if not looker:
			return ""
		desc = str()
		if "Fortunate One" in looker.db.accolades:
			desc = self.db.accoladedesc
		else:
			desc = self.db.desc
		return desc