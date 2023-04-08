from evennia import default_cmds, CmdSet, search_object, search_tag
from random import randint
from typeclasses.objects import DefaultObject

class playdice(default_cmds.MuxCommand):
	key = "dice"
	aliases = ["Dice"]
	auto_help = True
	def func(self):
		if not self.caller.tags.get("thekingisdead"):
			self.caller.msg("Command is not available. Type 'help' for help.")
			return
		def leave():
			self.caller.msg("|mGuard|n says: See you later.")
			return
		def play():
			self.caller.db.gold -= 10
			self.caller.msg("|/LET'S ROLL!!")
			d_one = randint(1,6)
			d_two = randint(1,6)
			d_three = randint(1,6)
			d_total = d_one + d_two + d_three
			self.caller.msg("You roll a %d, %d, and %d for a total of %d" % (d_one, d_two, d_three, d_total))
			if d_one == 6 and d_two == 6 and d_three == 6:
				self.caller.msg("|gWhat an amazing roll! YOU WIN 20 Gold!!|n")
				self.caller.db.gold += 20
				return
			o_one = randint(1,6)
			o_two = randint(1,6)
			o_three = randint(1,6)
			o_total = o_one + o_two + o_three
			self.caller.msg("Opponent rolls a %d, %d, and %d for a total of %d" % (o_one, o_two, o_three, o_total))
			if o_one == 6 and o_two == 6 and o_three == 6:
				self.caller.msg("|rWhat rotten luck! YOU LOSE 10 Gold!!|n")
				return
			elif o_total < d_total:
				self.caller.msg("|gWhat an amazing roll! YOU WIN 20 Gold!!|n")
				self.caller.db.gold += 20
			elif o_total > d_total:
				self.caller.msg("|rWhat rotten luck! YOU LOSE 10 Gold!!|n")
			else:
				self.caller.msg("Tie game! All money returned.")
				self.caller.db.gold += 10
			return
		def confused():
			self.caller.msg("|mGuard|n says: Did someone hit you on the head? You're not making any sense.")
			return
		if self.caller.db.gold > 10:
			self.caller.msg("|/|mGuard|n says: You look like the type that has some spare gold to dice with. How about it? 10 Gold a roll.")
			answer = yield ("|gP|nlay, |gL|nearn how to play, |gE|nxit.")
			if answer.lower() in ["p", "play"]:
				play()
			elif answer.lower() in ["l", "learn"]:
				self.caller.msg("|/|mGuard|n says: It's not too difficult, 10 gold per roll, all luck really. You roll 3 dice, the opponent rolls 3 dice. Whoever has the higher total wins, roll 3 six's you win automatically. In the unlikely event of a tie, you fight to the death.")
				self.caller.msg("|m%s|n says: ..." % (self.caller.key))
				answertwo = yield("|mGuard|n says: I'm just yanking your chain, ties a tie. So you wanna play or not?|/|gY|nes, |gN|no")
				if answertwo.lower() in ["y", "yes"]:
					play()
				elif answertwo.lower() in ["n", "no"]:
					leave()
				else:
					confused()
			elif answer.lower() in ["e", "exit"]:
				leave()
			else:
				confused()
		else:
			self.caller.msg("|/|mGuard|n says: Beat it ya bum, you don't have enough money to play this game.")
			return

class DiceCmdSet(CmdSet):
	key = "DiceCmdSet"
	def at_cmdset_creation(self):
		self.add(playdice())

class dice(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Several guards are huddled around a table playing an odd game of dice. You contemplate trying your hand at a game of |cDice|n."
		self.cmdset.add_default(DiceCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.locks.add("view:tag(thekingisdead)")
		self.db.get_err_msg = "|/Hey HEY!! None of that now!"