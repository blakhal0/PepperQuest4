from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random

class playgameoflife(default_cmds.MuxCommand):
	key = "Game of Life"
	aliases = ["game of life", "Game of life", "game of Life", "life", "Life", "game", "Game", "The Game of Life", "the game of life"]
	auto_help = False
	def func(self):
		if "Fortunate One" in self.caller.db.accolades:
			self.caller.msg("|/There is no Game of Life to play.")
			return
		else:
			self.caller.msg("|/|mCasino Host|n says: Ah, hello and welcome to the most exciting game we have at The Golden Parliament Casino! The Game of Life.")
			self.caller.msg("|mCasino Host|n says: No tokens needed for this game, everyone gets one free spin. Win and you receive fantastic prizes. Lose, well, no need to worry about that.")
			answer = yield("|mCasino Host|n says: Well, how about it, are you ready to play the most exciting game of you life?|/|cY|nes, |cN|no")
			if not answer.lower() in ["n", "no"]:
				self.caller.msg("|/|mCasino Host|n says: FANTASTIC! Step on up and spin the wheel!")
				self.caller.msg("You step up and give the wheel a mighty spin...")
				self.caller.msg("*Click-click-clickclickclickclickclickclick-click...click.....click*|/The wheel stops on the grand prize!!!")
				self.caller.msg("|mCasino Host|n says: Well look at that, another big winner! Congratulations! If you'd follow me over here there's some paperwork to fill out.")
				self.caller.msg("You follow the host into a backroom.")
				self.caller.msg("*THUNK*")
				self.caller.msg("Pain, then darkness engulfs you...")
				self.caller.msg("|/An unfamiliar voice chants a spell in the background, a golden coin spins in front of you. You feel tired but at ease, your vision begins to become golden.")
				self.caller.msg("Suddenly your ears fill with a deafening roar, fire courses through your veins, your vision clears, and the fog evaporates from your mind.|/You struggle wildly, but are restrained to a chair in a room filled with gold.")
				self.caller.msg("|mPriest|n shouts: HEY! Someone quick, knock them out!! It's not working, I don't know why!!")
				self.caller.msg("*THUNK*")
				self.caller.msg("As you drift off you can hear the priest talking with someone.")
				self.caller.msg("|mPriest|n says: I've very sorry oh Golden God, the enchantment will not work on this one and I do not know why.")
				self.caller.msg("A voice buzzes from a golden statue.")
				self.caller.msg("|mVoice|n: There is only one reason. Dump them on the other side of the desert, there's no need to trouble ourselves with this one. Let the merciless sands resolve the problem.")
				self.caller.msg("You hear a spell being chanted as you fade, the bright light of a portal is the last thing you glimpse.")
				results = search_object("#3224")
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			else:
				self.caller.msg("|/|mCasino Host|n says: Not a problem, you've got all the time in the world to change your mind. Come back again when you're ready!")
				return

class GameofLifeCmdSet(CmdSet):
	key = "GameofLifeCmdSet"
	def at_cmdset_creation(self):
		self.add(playgameoflife())

class gameoflife(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The Game of Life, for when you've got nothing left to lose."
		self.locks.add("view:not inlist(accolades, Fortunate One)")
		self.cmdset.add_default(GameofLifeCmdSet, permanent=True)
		self.locks.add("get:false()")