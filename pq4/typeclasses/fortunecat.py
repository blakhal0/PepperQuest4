from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
import random
from random import randint

class usecatstatue(default_cmds.MuxCommand):
	key = "Cat Statue"
	aliases = ["use statue", "use cat statue"]
	auto_help = True
	def func(self):
		targetcoin = self.caller.search("Coin", candidates=self.caller.contents, quiet=True)
		targetshoe = self.caller.search("Horseshoe", candidates=self.caller.contents, quiet=True)
		if not targetcoin and not targetshoe:
			self.caller.msg("|/Fortune Cat demands an offering! You have nothing to offer the feline wants.")
			return
		answer = yield("|/What would you like to offer the Fortune Cat?")
		if not answer.lower() in ["coin", "horseshoe", "horse shoe"]:
			self.caller.msg("|/Fortune Cat, uninterested in your pedestrian effort, mauls you with razor sharp murder mittens and ferocious nibbles.")
			if self.caller.db.hp < 10:
				self.caller.msg("|/|rWhat tragic fate, you have been murdered by Fortune Cat.|n|/You have brought shame to yourself and your family.")
				self.caller.db.deathcount += 1
				self.caller.db.hp = int(self.caller.db.maxhp * .5)
				self.caller.db.mp = int(self.caller.db.maxmp * .5)
				self.caller.db.gold -= int(self.caller.db.gold * .2)
				results = search_object(self.caller.db.lastcity)
				self.caller.move_to(results[0], quiet=True, move_hooks=False)
				return
			else:
				self.caller.msg("You lose %d hp." % (int(self.caller.db.hp * .10)))
				self.caller.db.hp -= int(self.caller.db.hp * .10)
			return
		if answer.lower() in ["horseshoe", "horse shoe"]:
			if not targetshoe:
				self.caller.msg("|/You don't have a %s to offer." % (answer))
				return
			if targetshoe[0].db.charged == "yes":
				self.caller.msg("|/Fortune Cat is briefly amused with your offering, but ultimately swats the %s onto the ground.|/It seems you're somewhere near the right track, but not quite there." % (answer))
				return
			if targetshoe[0].db.charged == "no":
				self.caller.msg("|/You place the %s on the offering tray.|/Fortune Cat pushes the %s off the tray, unsatisfied with your offering and disinterested in your entire existence." % (answer, answer))
				return
		if answer.lower() == "coin":
			if targetcoin[0].db.charged == "no":
				self.caller.msg("|/You place the coin on the offering tray.|/Fortune Cat pushes the coin off the tray, unsatisfied with your offering and disinterested in your entire existence.")
				return
			if targetcoin[0].db.charged == "yes":
				self.caller.msg("|/You place the coin on the offering tray.|/Fortune Cat is appeased with your offering. Fortune Cat waves its paw in contentment, a secret door opens.")
				self.caller.tags.add("fortunecatappeased")
				self.caller.db.chests.remove(96142620)
				self.caller.db.chests.remove(10482013)
				targetcoin[0].delete()
				targetshoe[0].delete()
				return

class CatStatueCmdSet(CmdSet):
	key = "CatStatueCmdSet"
	def at_cmdset_creation(self):
		self.add(usecatstatue())

class fortunecat(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "A large white |cCat Statue|n sits with one paw raised. At the base of the statue is a small offering tray."
		self.cmdset.add_default(CatStatueCmdSet, permanent=True)
		self.locks.add("get:false()")