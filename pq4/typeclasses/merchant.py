from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import typeclasses.battlespells as magic

class chat(default_cmds.MuxCommand):
	key = "talk merchant"
	aliases = ["Talk Merchant", "Talk merchant", "talk Merchant"]
	auto_help = True
	def func(self):
		battleforsale = []
		healforsale = []
		owforsale = []
		target = self.caller.search("merchant")
		for i in target.db.battlespells:
			if not i in self.caller.db.battlespells:
				name = getattr(magic, i.lower()).name
				battleforsale.append(name)
		for i in target.db.healspells:
			if not i in self.caller.db.battlespells:
				name = getattr(magic, i.lower()).name
				healforsale.append(name)
		for i in target.db.owspells:
			if not i in self.caller.db.overworldspells:
				name = getattr(magic, i.lower()).name
				owforsale.append(name)
		self.caller.msg("|/|mMerchant|n says: Greetings traveler, I am a magic merchant, spells for all your needs. Please, take a look through my wares to see if something might interest you, my prices are more than fair.")
		yield 1
		if battleforsale == [] and healforsale == [] and owforsale == []:
			self.caller.msg("|mMerchant|n says: Oh goodness, it appears you already have everything that I offer.")
			return
		while 1 < 10:
			if battleforsale == [] and healforsale == [] and owforsale == []:
				self.caller.msg("|mMerchant|n says: Oh goodness, it appears you already have everything that I offer.")
				break
			if not battleforsale == []:
				self.caller.msg("|/Some wonderfully dangerous battle spells?")
				for i in battleforsale:
					name = str(i)
					price = int(getattr(magic, i.lower()).price)
					self.caller.msg("%s %d gold." % (name, price))
			if not healforsale == []:
				self.caller.msg("|/Perhaps a nice restorative to keep you alive? Hmmm? Useful in battle and for healing after.")
				for i in healforsale:
					name = str(i)
					price = int(getattr(magic, i.lower()).price)
					self.caller.msg("%s %d gold." % (name, price))
			if not owforsale == []:
				self.caller.msg("|/A little something to use in the day to day, outside of battle?")
				for i in owforsale:
					name = str(i)
					price = int(getattr(magic, i.lower()).price)
					self.caller.msg("%s %d gold." % (name, price))
			answer = yield("|/|mMerchant|n says: Well, how about it, anything catch your eye?|/You have %d gold.|/|gE|nxit to quit." % (self.caller.db.gold))
			if answer.lower() in ["e", "exit", "q", "quit"]:
				self.caller.msg("|/|mMerchant|n says: Come back again!")
				break
			elif not type(answer) == str:
				self.caller.msg("|/|mMerchant|n says: Quit wasting my time with your nonsense jibberish.")
				break
			elif not answer.lower() in (i.lower() for i in battleforsale) and not answer.lower() in (i.lower() for i in healforsale) and not answer.lower() in (i.lower() for i in owforsale):
				self.caller.msg("|/|mMerchant|n says: I'm very sorry, I don't have any %s. Please, take another look." % (answer))
				yield 1
				continue
			elif not self.caller.db.gold >= int(getattr(magic, answer.lower()).price):
				self.caller.msg("|/|mMerchant|n says: It appears you're a bit short on funds, perhaps something ermmm, more economical for you?")
				yield 1
				continue
			else:
				self.caller.msg("|/|mMerchant|n says: Ah yes, a wonderful choice made by an exceedingly savy, and dare I say attractive, person.")
				self.caller.db.gold -= int(getattr(magic, answer.lower()).price)
				if answer.lower() in (i.lower() for i in battleforsale):
					self.caller.db.battlespells.append(answer.lower())
					for i in battleforsale:
						if i.lower() == answer.lower():
							battleforsale.remove(i)
				if answer.lower() in (i.lower() for i in healforsale):
					self.caller.db.battlespells.append(answer.lower())
					self.caller.db.overworldspells.append(answer.lower())
					for i in healforsale:
						if i.lower() == answer.lower():
							healforsale.remove(i)
				if answer.lower() in (i.lower() for i in owforsale):
					self.caller.db.overworldspells.append(answer.lower())
					for i in owforsale:
						if i.lower() == answer.lower():
							owforsale.remove(i)
				self.caller.msg("|/You have learned the %s spell!|/" % (getattr(magic, answer.lower()).name))
				yield 1
		return


class MerchantCmdSet(CmdSet):
	key = "MerchantCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class merchant(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A mysterious looking merchant is hawking their wares."
		self.db.battlespells = ["spark", "zap", "flame", "splash", "gust"]
		self.db.healspells = ["heal", "moreheal"]
		self.db.owspells = []
		self.cmdset.add_default(MerchantCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.tags.add("saleswizard")