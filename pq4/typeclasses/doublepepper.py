from evennia import default_cmds, CmdSet, search_object
from typeclasses.objects import DefaultObject
from random import randint
import random

class playdoublepepper(default_cmds.MuxCommand):
	key = "Double Pepper"
	alias = "Double Pepper Slots"
	auto_help = True
	def func(self):
		target = self.caller.search("Double Pepper Slots", quiet=True)
		target = target[0]
		price = target.db.cost
		if not "Fortunate One" in self.caller.db.accolades:
			reeloneopts = ["-7-", "---", "B3R", "-7-"]
			reeltwoopts = ["BAR", "---", "-7-", "---", "B3R", "---", "2🌂", "---", "🍒"]
			reelthreeopts = ["B2R", "---", "BAR", "---"]
		else:
			reeloneopts = ["BAR", "-7-", "---", "B2R", "B3R", "---", "2🌂", "🍒"]
			reeltwoopts = ["BAR", "-7-", "B2R", "B3R", "---", "2🌂", "🍒"]
			reelthreeopts = ["BAR", "---", "-7-", "B2R", "B3R", "2🌂", "🍒", "---"]
		self.caller.msg("|/Welcome to Double Pepper Slots!|/Cost is %d tokens per spin." % (target.db.cost))
		while 1 > 0:
			spinwin = 0
			answer = yield("|/|cS|npin, |cQ|nuit|/You have %d tokens." % (self.caller.db.tokens))
			if answer.lower() not in ["q", "quit", "s", "spin"]:
				self.caller.msg("|/|rIt appears you may have a gambling problem. Please seek help.|n")
				break
			if answer.lower() in ["q", "quit"]:
				self.caller.msg("|/Thanks for playing Double Pepper Slots!!")
				break
			if answer.lower() in ["s", "spin"]:
				if self.caller.db.tokens < price:
					self.caller.msg("|/|rYou do not have enough tokens to play.|/Please stop being poor.|n")
					break
				self.caller.db.tokens -= price
				self.caller.db.winnings -= price
				reelone = random.choice(reeloneopts)
				reeltwo = random.choice(reeltwoopts)
				reelthree = random.choice(reelthreeopts)
			#Reel One
				if reelone == "---":
					rodis = "---"
				if reelone == "🍒":
					rodis = " |r🍒|n"
				if reelone == "BAR":
					rodis = "|c" + reelone + "|n"
				if reelone == "B2R":
					rodis = "|524" + reelone + "|n"
				if reelone == "B3R":
					rodis = "|505" + reelone + "|n"
				if reelone == "-7-":
					rodis = "|500" + reelone + "|n"
				if reelone == "2🌂":
					rodis = "2|r🌂|n"
			#Reel Two
				if reeltwo == "---":
					rtdis = "---"
				if reeltwo == "🍒":
					rtdis = " |r🍒|n"
				if reeltwo == "BAR":
					rtdis = "|c" + reeltwo + "|n"
				if reeltwo == "B2R":
					rtdis = "|524" + reeltwo + "|n"
				if reeltwo == "B3R":
					rtdis = "|505" + reeltwo + "|n"
				if reeltwo == "-7-":
					rtdis = "|500" + reeltwo + "|n"
				if reeltwo == "2🌂":
					rtdis = "2|r🌂|n"
			#Reel Three
				if reelthree == "---":
					rthdis = "---"
				if reelthree == "🍒":
					rthdis = " |r🍒|n"
				if reelthree == "BAR":
					rthdis = "|c" + reelthree + "|n"
				if reelthree == "B2R":
					rthdis = "|524" + reelthree + "|n"
				if reelthree == "B3R":
					rthdis = "|505" + reelthree + "|n"
				if reelthree == "-7-":
					rthdis = "|500" + reelthree + "|n"
				if reelthree == "2🌂":
					rthdis = "2|r🌂|n"
				self.caller.msg("|/..:DOUBLE PEPPER:..")
				self.caller.msg("..::...::...::..")
				self.caller.msg("|| %s - %s - %s ||" % (rodis, rtdis, rthdis))
				self.caller.msg("˙˙::˙˙˙::˙˙˙::˙˙")
			#Naturals
				if reelone == reeltwo and reelone == reelthree:
					if reelone == "🍒":
						self.caller.msg("     CHERRIES!     ")
						spinwin = 10
					if reelone == "BAR":
						self.caller.msg("   SINGLE BAR!!!   ")
						spinwin = 10
					if reelone == "B2R":
						self.caller.msg("    DOUBLE BAR!    ")
						spinwin = 25
					if reelone == "B3R":
						self.caller.msg("    TRIPLE BAR!    ")
						spinwin = 40
					if reelone == "-7-":
						self.caller.msg("      SEVENS!      ")
						spinwin = 80
					if reelone == "2🌂":
						self.caller.msg("    !!JACKPOT!!    ")
						spinwin = 800
			#Single Cherry
				elif reelone == "🍒" and not "🍒" in [reeltwo, reelthree] and not "2🌂" in [reeltwo, reelthree]:
					self.caller.msg("      CHERRY!      ")
					spinwin = 2
				elif reeltwo == "🍒" and not "🍒" in [reelone, reelthree] and not "2🌂" in [reelone, reelthree]:
					self.caller.msg("      CHERRY!      ")
					spinwin = 2
				elif reelthree == "🍒" and not "🍒" in [reelone, reeltwo] and not "2🌂" in [reelone, reeltwo]:
					self.caller.msg("      CHERRY!      ")
					spinwin = 2
			#Two Cherry
				elif reelone == "🍒" and reeltwo == "🍒" and not reelthree in ["2🌂", "🍒"]:
					self.caller.msg("    TWO CHERRY!    ")
					spinwin = 5
				elif reelone == "🍒" and reelthree == "🍒" and not reeltwo in ["2🌂", "🍒"]:
					self.caller.msg("    TWO CHERRY!    ")
					spinwin = 5
				elif reeltwo == "🍒" and reelthree == "🍒" and not reelone in ["2🌂", "🍒"]:
					self.caller.msg("    TWO CHERRY!    ")
					spinwin = 5
			#Any Bar
				elif all(x in ["BAR", "B2R", "B3R"] for x in [reelone, reeltwo, reelthree]):
					self.caller.msg("    MIXED BARS!    ")
					spinwin = 5
			#2x
				#Any Bar
				elif all(x in ["BAR", "B2R", "B3R"] for x in [reelone, reeltwo]) and "2🌂" == reelthree and not reelone == reeltwo:
					self.caller.msg("    2x ANY BAR!    ")
					spinwin = 10
				elif all(x in ["BAR", "B2R", "B3R"] for x in [reelone, reelthree]) and "2🌂" == reeltwo and not reelone == reelthree:
					self.caller.msg("    2x ANY BAR!    ")
					spinwin = 10
				elif all(x in ["BAR", "B2R", "B3R"] for x in [reelthree, reeltwo]) and "2🌂" == reelone and not reelthree == reeltwo:
					self.caller.msg("    2x ANY BAR!    ")
					spinwin = 10
				#Single Cherries
				elif "🍒" == reelone and reeltwo in ["BAR", "B2R", "B3R", "-7-", "---"] and "2🌂" == reelthree:
					self.caller.msg("    2x CHERRY!!    ")
					spinwin = 10
				elif "🍒" == reelone and reelthree in ["BAR", "B2R", "B3R", "-7-", "---"] and "2🌂" == reeltwo:
					self.caller.msg("    2x CHERRY!!    ")
					spinwin = 10
				elif "🍒" == reeltwo and reelone in ["BAR", "B2R", "B3R", "-7-", "---"] and "2🌂" == reelthree:
					self.caller.msg("    2x CHERRY!!    ")
					spinwin = 10
				elif "🍒" == reeltwo and reelthree in ["BAR", "B2R", "B3R", "-7-", "---"] and "2🌂" == reelone:
					self.caller.msg("    2x CHERRY!!    ")
					spinwin = 10
				elif "🍒" == reelthree and reelone in ["BAR", "B2R", "B3R", "-7-", "---"] and "2🌂" == reeltwo:
					self.caller.msg("    2x CHERRY!!    ")
					spinwin = 10
				elif "🍒" == reelthree and reeltwo in ["BAR", "B2R", "B3R", "-7-", "---"] and "2🌂" == reelone:
					self.caller.msg("    2x CHERRY!!    ")
					spinwin = 10
				#Two Cherries
				elif "🍒" == reelone and "🍒" == reeltwo and "2🌂" == reelthree:
					self.caller.msg("   2x CHERRIES!!   ")
					spinwin = 20
				elif "🍒" == reelone and "🍒" == reelthree and "2🌂" == reeltwo:
					self.caller.msg("   2x CHERRIES!!   ")
					spinwin = 20
				elif "🍒" == reeltwo and "🍒" == reelthree and "2🌂" == reelone:
					self.caller.msg("   2x CHERRIES!!   ")
					spinwin = 20
				#Single Bar
				elif all(x in ["BAR"] for x in [reelone, reeltwo]) and "2🌂" == reelthree:
					self.caller.msg("  2x SINGLE BAR!!  ")
					spinwin = 20
				elif all(x in ["BAR"] for x in [reelone, reelthree]) and "2🌂" == reeltwo:
					self.caller.msg("  2x SINGLE BAR!!  ")
					spinwin = 20
				elif all(x in ["BAR"] for x in [reelthree, reeltwo]) and "2🌂" == reelone:
					self.caller.msg("  2x SINGLE BAR!!  ")
					spinwin = 20
				#Double Bar
				elif all(x in ["B2R"] for x in [reelone, reeltwo]) and "2🌂" == reelthree:
					self.caller.msg("  2x DOUBLE BAR!!  ")
					spinwin = 50
				elif all(x in ["B2R"] for x in [reelone, reelthree]) and "2🌂" == reeltwo:
					self.caller.msg("  2x DOUBLE BAR!!  ")
					spinwin = 50
				elif all(x in ["B2R"] for x in [reelthree, reeltwo]) and "2🌂" == reelone:
					self.caller.msg("  2x DOUBLE BAR!!  ")
					spinwin = 50
				#Triple Bar
				elif all(x in ["B3R"] for x in [reelone, reeltwo]) and "2🌂" == reelthree:
					self.caller.msg("  2x TRIPLE BAR!!  ")
					spinwin = 80
				elif all(x in ["B3R"] for x in [reelone, reelthree]) and "2🌂" == reeltwo:
					self.caller.msg("  2x TRIPLE BAR!!  ")
					spinwin = 80
				elif all(x in ["B3R"] for x in [reelthree, reeltwo]) and "2🌂" == reelone:
					self.caller.msg("  2x TRIPLE BAR!!  ")
					spinwin = 80
				#Sevens
				elif all(x in ["-7-"] for x in [reelone, reeltwo]) and "2🌂" == reelthree:
					self.caller.msg("    2x SEVENS!!    ")
					spinwin = 160
				elif all(x in ["-7-"] for x in [reelone, reelthree]) and "2🌂" == reeltwo:
					self.caller.msg("    2x SEVENS!!    ")
					spinwin = 160
				elif all(x in ["-7-"] for x in [reelthree, reeltwo]) and "2🌂" == reelone:
					self.caller.msg("    2x SEVENS!!    ")
					spinwin = 160
			#Quadruples
				#Cherries
				elif all(x in ["🍒"] for x in [reelone]) and all(x in ["2🌂"] for x in [reeltwo, reelthree]):
					self.caller.msg("   4x CHERRIES!!   ")
					spinwin = 40
				elif all(x in ["🍒"] for x in [reeltwo]) and all(x in ["2🌂"] for x in [reelone, reelthree]):
					self.caller.msg("   4x CHERRIES!!   ")
					spinwin = 40
				elif all(x in ["🍒"] for x in [reelthree]) and all(x in ["2🌂"] for x in [reelone, reeltwo]):
					self.caller.msg("   4x CHERRIES!!   ")
					spinwin = 40
				#Single Bar
				elif all(x in ["BAR"] for x in [reelone]) and all(x in ["2🌂"] for x in [reeltwo, reelthree]):
					self.caller.msg("  4x SINGLE BAR!!  ")
					spinwin = 40
				elif all(x in ["BAR"] for x in [reeltwo]) and all(x in ["2🌂"] for x in [reelone, reelthree]):
					self.caller.msg("  4x SINGLE BAR!!  ")
					spinwin = 40
				elif all(x in ["BAR"] for x in [reelthree]) and all(x in ["2🌂"] for x in [reelone, reeltwo]):
					self.caller.msg("  4x SINGLE BAR!!  ")
					spinwin = 40
				#Double Bar
				elif all(x in ["B2R"] for x in [reelone]) and all(x in ["2🌂"] for x in [reeltwo, reelthree]):
					self.caller.msg("  4x DOUBLE BAR!!  ")
					spinwin = 100
				elif all(x in ["B2R"] for x in [reeltwo]) and all(x in ["2🌂"] for x in [reelone, reelthree]):
					self.caller.msg("  4x DOUBLE BAR!!  ")
					spinwin = 100
				elif all(x in ["B2R"] for x in [reelthree]) and all(x in ["2🌂"] for x in [reelone, reeltwo]):
					self.caller.msg("  4x DOUBLE BAR!!  ")
					spinwin = 100
				#Tripple Bar
				elif all(x in ["B3R"] for x in [reelone]) and all(x in ["2🌂"] for x in [reeltwo, reelthree]):
					self.caller.msg("  4x TRIPLE BAR!!  ")
					spinwin = 160
				elif all(x in ["B3R"] for x in [reeltwo]) and all(x in ["2🌂"] for x in [reelone, reelthree]):
					self.caller.msg("  4x TRIPLE BAR!!  ")
					spinwin = 160
				elif all(x in ["B3R"] for x in [reelthree]) and all(x in ["2🌂"] for x in [reelone, reeltwo]):
					self.caller.msg("  4x TRIPLE BAR!!  ")
					spinwin = 160
				#Sevens
				elif all(x in ["-7-"] for x in [reelone]) and all(x in ["2🌂"] for x in [reeltwo, reelthree]):
					self.caller.msg("    4x SEVENS!!    ")
					spinwin = 320
				elif all(x in ["-7-"] for x in [reeltwo]) and all(x in ["2🌂"] for x in [reelone, reelthree]):
					self.caller.msg("    4x SEVENS!!    ")
					spinwin = 320
				elif all(x in ["-7-"] for x in [reelthree]) and all(x in ["2🌂"] for x in [reelone, reeltwo]):
					self.caller.msg("    4x SEVENS!!    ")
					spinwin = 320
			#Announce Win/Loss
				if spinwin > 0:
					self.caller.msg("|gYou Win %d tokens!|n" % (spinwin * target.db.cost))
					self.caller.db.tokens += spinwin * target.db.cost
					self.caller.db.winnings += spinwin * target.db.cost
					continue
				else:
					self.caller.msg("     |rYou Lose.|n     |/Better Luck Next Time.")
					continue
				continue


class DoublePepperCmdSet(CmdSet):
	key = "DoublePepperCmdSet"
	def at_cmdset_creation(self):
		self.add(playdoublepepper())

class doublepepper(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Double Pepper.|/2 Tokens per spin|/--Paytable--|/|r🍒|n - 4,10,20) ||   Any Bar - 10|/3x BAR - 20   ||   3x B2R - 50|/3x B3R - 80   ||   3x -7- - 800|/3x |r2🌂|n - 1600|/|r2🌂|n on any winning payline doubles win."
		self.db.cost = 2
		self.cmdset.add_default(DoublePepperCmdSet, permanent=True)
		self.locks.add("get:false()")