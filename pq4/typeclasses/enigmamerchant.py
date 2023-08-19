from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from evennia.prototypes.spawner import spawn

class talkenigmamerchant(default_cmds.MuxCommand):
	key = "Talk Steve"
	aliases = ["talk steve"]
	auto_help = True
	def func(self):
		enigmalist = ["Enigma Armor", "Enigma Weapon", "Enigma Armor"]
		contentslist = []
		for i in self.caller.contents:
			contentslist.append(i.key)
		if "Map to Panahon" in contentslist:
			self.caller.msg("|/|mSteve|n says: Looks like you've already obtained the rarest objects I've ever found or sought. Congratulations, you're quite the adventurer!")
			self.caller.msg("Steve gives you a hardy hand shake and a look of respect.")
			return
		if any(i for i in enigmalist if i in contentslist):
			self.caller.msg("|/|mSteve|n says: Whoa, you've got Enigma Items. Now that's not something you run across every day. I happen to deal in such rare items for the discerning collectors I represent. I've got one of the rarest items ever found right here, a map to Panahon the fabled island of time. You're an adventurer, you obviously recognize the value in a map to a mythical land.")
			answer = yield("|mSteve|n says: So what do you say? I'll trade you this map for the Enigma Items you carry. Deal?|/|cY|nes, |cN|no")
			if answer.lower() in ["y", "yes"]:
				self.caller.msg("|/|mSteve|n says: I love it when a deal comes together!")
				for i in self.caller.contents:
					if i.key in ["Enigma Armor", "Enigma Weapon", "Enigma Armor"]:
						i.delete()
				pm_proto = {
				"key": "Map to Panahon",
				"typeclass": "typeclasses.objects.panahonmap",
				"location": self.caller
				}
				spawn(pm_proto)
				self.caller.msg("You receive a Map to Panahon!")
				self.caller.msg("|mSteve|n says: Done and done! If you happen to find something amazing on your adventure to Panahon stop back! Good luck!!")
				self.caller.msg("Steve gives you a hardy hand shake and a look of respect.")
				return
			else:
				self.caller.msg("|/|mSteve|n says: No deal eh? Well, if you change your mind I'll be here. Just think it over, a mythical land of unknown riches, could be yours for some old junk that's essentially worthless.")
				return
		else:
			self.caller.msg("|/|mSteve|n says: I tend to deal in, mmmm, more exotic items. You don't have anything particularly interesting. Now, if you happen to come across any of those Enigma items, well, I've got a map. A very rare map, said to lead you to the island of time itself. I'd be willing to trade.")
			self.caller.msg("Steve goes back to sorting a small pile of trinkets.")
			return

class TalkEnigmaMerchantCmdSet(CmdSet):
	key = "TalkEnigmaMerchantCmdSet"
	def at_cmdset_creation(self):
		self.add(talkenigmamerchant())

class steve(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "At first glance this appears to be the kind of person you should avoid. A closer inspection shows a well to do merchant under a guise of street urchin, the sense that they're quick with a dagger doesn't fade a bit."
		self.cmdset.add_default(TalkEnigmaMerchantCmdSet, permanent=True)
		self.db.get_err_msg = "|/|mMysterious Merchant|n says: Now now, don't make me turn your hands into a decorative item."
		self.locks.add("get:false()")
		self.tags.add("specialnpc")