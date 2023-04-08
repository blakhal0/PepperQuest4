from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject

class chatcashier(default_cmds.MuxCommand):
	key = "talk cashier"
	aliases = ["Talk Cashier", "Talk cashier", "talk Cashier" ]
	auto_help = True
	def func(self):
		self.caller.msg("|/|mCashier|n says: Welcome to The Golden Parliament Casino! I hope you're ready to win big!")
		answer = yield("|mCashier|n says: Our games only accept casino tokens, 1 token costs 2 gold. How many tokens would you like?|/|/You have %d gold and %d tokens." % (self.caller.db.gold, self.caller.db.tokens))
		if not answer.isnumeric():
			self.caller.msg("|/|mCashier|n says: Mmm-hmmm, I've run across your kind before. Think you're really funny don't you. Well I'm telling you now, I won't have it. The goons will be along shortly to rough you up.")
			self.caller.msg("A couple of walking mountains appear out of nowhere and beat the crap out of you.")
			self.caller.db.hp = 1
			return
		if int(answer) < 0:
			self.caller.msg("|/|mCashier|n says: Mmm-hmmm, I've run across your kind before. Think you're really funny don't you. Well I'm telling you now, I won't have it. The goons will be along shortly to rough you up.")
			self.caller.msg("A couple of walking mountains appear out of nowhere and beat the crap out of you.")
			self.caller.db.hp = 1
			return
		if int(answer) == 0:
			self.caller.msg("|mCashier|n says: Changed your mind? No worries. Stop back when you're ready!")
			self.caller.msg("|mCashier|n says: Thank you for coming to The Golden Parliament Casino! Good luck!!")
			return
		cost = int(answer) * 2
		if cost > self.caller.db.gold:
			self.caller.msg("|/|mCashier|n says: I'm very sorry, but it appears you're a bit short on funds. The casino does not offer lines of credit at this time. Please either request fewer tokens or earn more gold. Thank you! Please come back to The Golden Parliament Casino again.")
			return
		if "Fortunate One" in self.caller.db.accolades:
			self.caller.db.gold -= int(cost)
			self.caller.db.tokens += int(answer)
			self.caller.msg("The cashier hands you %d tokens" % (int(answer)))
			self.caller.msg("|mCashier|n says: Thank you for coming to The Golden Parliament Casino! Good luck!!")
			return
		else:
			self.caller.db.gold -= int(cost)
			self.caller.db.tokens += int(answer)
			self.caller.msg("The cashier hands you %d tokens" % (int(answer)))
			self.caller.msg("|mCashier|n says: ...and with the convenience fee, currency conversion fee, handling fee, token cleaning fee, verification fee, security fee, gaming tax, local option sales tax, water tax, tax fee, fee tax, sand tax, resort fee, 30 percent gratuity, space time continuum warranty, Emotional Support Badgers for Under Privileged Youth of Upper Kharro donation fund fee, fee tax fee, verification mark fee, and annual llama maintenance fee, that'll be an extra %d gold." % (self.caller.db.gold))
			self.caller.db.winnings -= self.caller.db.gold
			self.caller.db.gold = 0
			self.caller.msg("|m%s|n says: What the actual f-" % (self.caller.key))
			self.caller.msg("A couple of gigantic goons grab you, turn you upside down, shake all the gold out of your pockets, and sweep it up.")
			self.caller.msg("|mCashier|n says: Thank you for coming to The Golden Parliament Casino! Good luck!!")
			return


class CashierCmdSet(CmdSet):
	key = "CashierCmdSet"
	def at_cmdset_creation(self):
		self.add(chatcashier())

class cashier(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "The cashier welcomes you with a very pleasant and warm smile."
		self.tags.add("specialnpc")
		self.cmdset.add_default(CashierCmdSet, permanent=True)
		self.locks.add("get:false()")