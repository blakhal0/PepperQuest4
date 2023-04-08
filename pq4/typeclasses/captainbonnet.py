from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class chatcaptainbonnet(default_cmds.MuxCommand):
	key = "Talk Captain Bonnet"
	aliases = ["talk captain bonnet"]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("kingofthieves"):
			self.caller.msg("There's no one by that name to talk to.")
			return
		self.caller.msg("|/|mCaptain Bonnet|n says: Well hello, welcome to our humble abode. I know it's not much, but we've tried to make the place as pleasant as possible.")
		answer = yield("|mCaptain Bonnet|n says: So, how about it? Would you like to go for a sail on The Revenge? We don't go many places due to the Valaharran ships in the Bay of Blood, but I know a lovely port in Kharro.|/|cY|nes, |cN|no")
		if answer.lower() in ["y", "yes"]:
			self.caller.msg("|/Captain Bonnet's face lights up with joy.")
			self.caller.msg("|mCaptain Bonnet|n says: Oh wonderful. I do so love taking the ship out. I'm sure you'll have a fantastic voyage.")
			self.caller.msg("|mCaptain Bonnet|n shouts: Listen up crew, %s has agreed to let us take them for a ride on the ship, prepare the longboats and get ready to set sail!" % (self.caller.key))
			self.caller.msg("|/You board the ship and set to sea, destined for Kharro. The ship glides across the Bay of Blood, up the coast of the Dogudaki Ocean, past the Red Cliffs of Kharro, and into the Dekheila Bay where you once again take to the longboat as the crew rows you ashore.")
			self.caller.msg("|mCaptain Bonnet|n says: I do hope you enjoyed the trip, please stop back again if you find yourself in Tormey, it was very exciting to meet such an intriguing adventurer.")
			results = search_object("#2998")
			self.caller.move_to(results[0], quiet=True, move_hooks=False)
			return
		elif answer.lower() in ["n", "no"]:
			self.caller.msg("|/|mCaptain Bonnet|n says: I suppose sailing isn't for everyone. Please enjoy your time in Booty Port. If you change your mind, it really is a lovely ship. I think you'd very much enjoy it.")
			return
		else:
			self.caller.msg("|/|mCaptain Bonnet|n says: I'm terribly sorry, I didn't understand that. Lucius is a terrific translator if you don't speak the local language.")
			return

class CaptainBonnetCmdSet(CmdSet):
	key = "CaptainBonnetCmdSet"
	def at_cmdset_creation(self):
		self.add(chatcaptainbonnet())

class captainbonnet(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "He's fancy"
		self.cmdset.add_default(CaptainBonnetCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:tag(kingofthieves)")
		self.tags.add("specialnpc")