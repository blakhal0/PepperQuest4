from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint
import random

class playspicysevens(default_cmds.MuxCommand):
	key = "Spicy Sevens"
	alias = "Spicy Sevens Slots"
	auto_help = True
	def func(self):
		target = self.caller.search("Spicy Sevens Slots", quiet=True)
		target = target[0]
		price = target.db.cost
		if not "Fortunate One" in self.caller.db.accolades:
			reeloneopts = ["-7-", "---", "B3R", "-7-", "777", "B2R"]
			reeltwoopts = ["BAR", "---", "B3R", "---", "---"]
			reelthreeopts = ["B2R", "---", "-7-", "BAR", "---", "777"]
		else:
			reeloneopts = ["BAR", "-7-", "---", "777", "B2R",  "---", "B3R"]
			reeltwoopts = [ "B3R", "BAR", "-7-", "B2R", "---", "777"]
			reelthreeopts = ["777", "BAR", "---", "-7-", "B2R", "B3R", "---"]
		self.caller.msg("|/Welcome to Spicy Seven Slots!|/Cost is %d tokens per spin." % (target.db.cost))
		while 1 > 0:
			spinwin = 0
			answer = yield("|/|cS|npin, |cQ|nuit|/You have %d tokens." % (self.caller.db.tokens))
			if answer.lower() not in ["q", "quit", "s", "spin"]:
				self.caller.msg("|/|rIt appears you may have a gambling problem. Please seek help.|n")
				break
			if answer.lower() in ["q", "quit"]:
				self.caller.msg("|/Thanks for playing Spicy Sevens Slots!!")
				break
			if answer.lower() in ["s", "spin"]:
				if self.caller.db.tokens < price:
					self.caller.msg("|/|rYou do not have enough tokens to play.|/Please stop being poor.|n")
					break
				self.caller.db.tokens -= price
				self.caller.db.winnings -= price
			#Add to progressive
				target.db.progressive += 1 * target.db.multiplier
			#Get Reels
				reelone = random.choice(reeloneopts)
				reeltwo = random.choice(reeltwoopts)
				reelthree = random.choice(reelthreeopts)
			#Reel One Display
				if reelone == "---":
					rodis = "---"
				if reelone == "BAR":
					rodis = "|c" + reelone + "|n"
				if reelone == "B2R":
					rodis = "|524" + reelone + "|n"
				if reelone == "B3R":
					rodis = "|505" + reelone + "|n"
				if reelone == "-7-":
					rodis = "-|r7|n-"
				if reelone == "777":
					rodis = "|r777|n"
			#Reel Two Display
				if reeltwo == "---":
					rtdis = "---"
				if reeltwo == "BAR":
					rtdis = "|c" + reeltwo + "|n"
				if reeltwo == "B2R":
					rtdis = "|524" + reeltwo + "|n"
				if reeltwo == "B3R":
					rtdis = "|505" + reeltwo + "|n"
				if reeltwo == "-7-":
					rtdis = "-|r7|n-"
				if reeltwo == "777":
					rtdis = "|r777|n"
			#Reel Three Display
				if reelthree == "---":
					rthdis = "---"
				if reelthree == "BAR":
					rthdis = "|c" + reelthree + "|n"
				if reelthree == "B2R":
					rthdis = "|524" + reelthree + "|n"
				if reelthree == "B3R":
					rthdis = "|505" + reelthree + "|n"
				if reelthree == "-7-":
					rthdis = "-|r7|n-"
				if reelthree == "777":
					rthdis = "|r777|n"
				self.caller.msg("|/..:SPICY  SEVENS:..")
				self.caller.msg("||Progressive: %d||" % (target.db.progressive))
				self.caller.msg("..::...::...::..")
				self.caller.msg("|| %s - %s - %s ||" % (rodis, rtdis, rthdis))
				self.caller.msg("˙˙::˙˙˙::˙˙˙::˙˙")
			#Naturals
				if reelone == reeltwo and reelone == reelthree:
					if reelone == "---":
						self.caller.msg("       BLANKS      ")
						spinwin = 2
					if reelone == "BAR":
						self.caller.msg("   SINGLE BAR!!!   ")
						spinwin = 20
					if reelone == "B2R":
						self.caller.msg("    DOUBLE BAR!    ")
						spinwin = 40
					if reelone == "B3R":
						self.caller.msg("    TRIPLE BAR!    ")
						spinwin = 60
					if reelone == "-7-":
						self.caller.msg("      SEVENS!      ")
						spinwin = 300
					if reelone == "777":
						self.caller.msg("  !!PROGRESSIVE!!  ")
						self.caller.msg("    !!JACKPOT!!    ")
						spinwin = target.db.progressive
					#Reset the progressive
						target.db.progressive = 1000
			#Any Bar
				elif all(x in ["BAR", "B2R", "B3R"] for x in [reelone, reeltwo, reelthree]):
					self.caller.msg("    MIXED BARS!    ")
					spinwin = 10
			#Any 7s
				elif all(x in ["-7-", "777"] for x in [reelone, reeltwo, reelthree]):
					self.caller.msg("   MIXED SEVENS!   ")
					spinwin = 200
			#Announce Win/Loss
				if spinwin > 0:
					if reelone == "777" and reeltwo == "777" and reelthree == "777":
						self.caller.msg("|gYou Win %d tokens!|n" % (spinwin))
						self.caller.db.tokens += spinwin
					elif reelone == "---" and reeltwo == "---" and reelthree == "---":
						self.caller.msg("|gYou Win %d tokens!|n" % (spinwin))
						self.caller.db.tokens += spinwin
					else:
						self.caller.msg("|gYou Win %d tokens!|n" % (spinwin * target.db.multiplier))
						self.caller.db.tokens += spinwin * target.db.multiplier
						self.caller.db.winnings += spinwin * target.db.multiplier
					continue
				else:
					self.caller.msg("     |rYou Lose.|n     |/Better Luck Next Time.")
					continue
				continue


class SpicySevensCmdSet(CmdSet):
	key = "SpicySevensCmdSet"
	def at_cmdset_creation(self):
		self.add(playspicysevens())

class spicysevens(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Spicy Sevens With Progressive.|/3 Tokens per spin|/--Paytable--|/3x --- - 2    ||   Any Bar - 10|/3x BAR - 20   ||   3x B2R - 40|/3x B3R - 60   ||   3x Any 7 - 200|/3x -7- - 300  ||   3x 777 - Progressive"
		self.db.cost = 3
		self.db.multiplier = 1
		self.db.progressive = 1000
		self.cmdset.add_default(SpicySevensCmdSet, permanent=True)
		self.locks.add("get:false()")