from evennia import default_cmds, CmdSet, search_object, search_tag
from typeclasses.objects import DefaultObject
import typeclasses.battlespells as magic

class chat(default_cmds.MuxCommand):
	key = "talk wizard"
	aliases = ["Talk Wizard", "Talk wizard", "talk Wizard"]
	auto_help = True
	def func(self):
		battleforsale = []
		healforsale = []
		owforsale = []
		target = search_tag("saleswizard").filter(db_location=self.caller.location)
		for i in target[0].db.battlespells:
			if not i in self.caller.db.battlespells:
				name = getattr(magic, i.lower()).name
				battleforsale.append(name)
		for i in target[0].db.healspells:
			if not i in self.caller.db.overworldspells:
				name = getattr(magic, i.lower()).name
				healforsale.append(name)
		for i in target[0].db.owspells:
			if not i in self.caller.db.overworldspells:
				name = getattr(magic, i.lower()).name
				owforsale.append(name)
		self.caller.msg("|/|m%s|n says: %s" % (target[0].key, target[0].db.welcome))
		yield 1
		if battleforsale == [] and healforsale == [] and owforsale == []:
			self.caller.msg("|m%s|n says: Oh goodness, it appears you already have everything that I offer." % (target[0].key))
			self.caller.msg("|/|m%s|n says: %s" % (target[0].key, target[0].db.goodbye))
			return
		while 1 < 10:
			if battleforsale == [] and healforsale == [] and owforsale == []:
				self.caller.msg("|m%s|n says: Oh goodness, it appears you already have everything that I offer." % (target[0].key))
				self.caller.msg("|/|m%s|n says: %s" % (target[0].key, target[0].db.goodbye))
				break
			if not battleforsale == []:
				self.caller.msg("|/Some wonderfully dangerous battle spells?")
				for i in battleforsale:
					name = str(i)
					price = int(getattr(magic, i.lower()).price)
					self.caller.msg("%s - %d gold." % (name, price))
			if not healforsale == []:
				self.caller.msg("|/Perhaps a nice restorative to keep you alive? Hmmm? Useful in battle and for healing after.")
				for i in healforsale:
					name = str(i)
					price = int(getattr(magic, i.lower()).price)
					self.caller.msg("%s - %d gold." % (name, price))
			if not owforsale == []:
				self.caller.msg("|/A little something to use in the day to day, outside of battle?")
				for i in owforsale:
					name = str(i)
					price = int(getattr(magic, i.lower()).price)
					self.caller.msg("%s - %d gold." % (name, price))
			answer = yield("|/|m%s|n says: Well, how about it, anything catch your eye?|/You have %d gold.|/|gE|nxit to quit." % (target[0].key, self.caller.db.gold))
			if answer.lower() in ["e", "exit", "q", "quit"]:
				self.caller.msg("|/|m%s|n says: %s" % (target[0].key, target[0].db.goodbye))
				break
			elif not type(answer) == str:
				self.caller.msg("|/|m%s|n says: Quit wasting my time with your nonsense jibberish." % (target[0].key))
				break
			elif not answer.lower() in (i.lower() for i in battleforsale) and not answer.lower() in (i.lower() for i in healforsale) and not answer.lower() in (i.lower() for i in owforsale):
				self.caller.msg("|/|m%s|n says: I'm very sorry, I don't have any %s. Please, take another look." % (target[0].key, answer))
				yield 1
				continue
			elif not self.caller.db.gold >= int(getattr(magic, answer.lower()).price):
				self.caller.msg("|/|m%s|n says: It appears you're a bit short on funds, perhaps something ermmm, more economical for you?" % (target[0].key))
				yield 1
				continue
			else:
				self.caller.msg("|/|m%s|n says: Ah yes, a wonderful choice made by an exceedingly savy, and dare I say attractive, person." % (target[0].key))
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
				self.caller.msg("|/|gYou have learned the %s spell!|n|/" % (getattr(magic, answer.lower()).name))
				yield 1
		return


class MagicMerchantCmdSet(CmdSet):
	key = "MagicMerchantCmdSet"
	def at_cmdset_creation(self):
		self.add(chat())

class magicmerchant(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A mysterious looking merchant is hawking their wares."
		self.db.welcome = "WELCOME MESSAGE!"
		self.db.goodbye = "GOODBYE MESSAGE!"
		self.db.battlespells = []
		self.db.healspells = []
		self.db.owspells = []
		self.cmdset.add_default(MagicMerchantCmdSet, permanent=True)
		self.locks.add("get:false()")
		self.tags.add("specialnpc")
		self.tags.add("saleswizard")