from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
from random import randint
import random

class playgorillionaire(default_cmds.MuxCommand):
	key = "Gorillionaire"
	alias = "Gorillionaire Slots"
	auto_help = True
	def func(self):
		target = self.caller.search("Gorillionaire Slots", quiet=True)
		target = target[0]
		price = target.db.cost
		if not "Fortunate One" in self.caller.db.accolades:
			reeloneopts = ["BAR", "-7-", "B2R", "---" "B3R", "---"]
			reeltwoopts = ["ANA", "BAR", "ANA", "---", "---", "ANA", "B7R"]
			reelthreeopts = ["-7-", "S!!", "B2R", "S!!", "---", "B7R"]
		else:
			reeloneopts = ["BAN", "---", "BAR", "-7-", "BAN", "---", "B2R", "BAN", "B3R", "B7R"]
			reeltwoopts = ["---", "BAR", "-7-", "ANA", "B2R", "B3R", "ANA", "B7R"]
			reelthreeopts = ["BAR", "-7-", "---", "S!!", "B2R", "---", "B3R", "B7R"]
		self.caller.msg("|/Money Gorilla welcomes you to Gorillionaire Slots!|/Cost is %d tokens per spin." % (price))
		while 1 > 0:
			spinwin = 0
			answer = yield("|/|cS|npin, |cQ|nuit|/You have %d tokens." % (self.caller.db.tokens))
			if answer.lower() not in ["q", "quit", "s", "spin"]:
				self.caller.msg("|/|rIt appears you may have a gambling problem. Money Gorilla asks that you please seek help.|n")
				break
			if answer.lower() in ["q", "quit"]:
				self.caller.msg("|/Money Gorilla thanks for playing Gorillionaire Slots!!")
				break
			if answer.lower() in ["s", "spin"]:
				if self.caller.db.tokens < price:
					self.caller.msg("|/|rYou do not have enough tokens to play.|/Money Gorilla asks that you please stop being poor.|n")
					break
				self.caller.db.tokens -= price
				self.caller.db.winnings -= price
				reelone = random.choice(reeloneopts)
				reeltwo = random.choice(reeltwoopts)
				reelthree = random.choice(reelthreeopts)
			#BANANAS
				if reelone == "BAN":
					rodis = "|550" + reelone + "|n"
				if reeltwo == "ANA":
					rtdis = "|550" + reeltwo + "|n"
				if reelthree == "S!!":
					rthdis = "|550" + reelthree + "|n"
			#Reel One
				if reelone == "---":
					rodis = "---"
				if reelone == "BAR":
					rodis = "|040" + reelone + "|n"
				if reelone == "B2R":
					rodis = "|005" + reelone + "|n"
				if reelone == "B3R":
					rodis = "|520" + reelone + "|n"
				if reelone == "B7R":
					rodis = "|504" + reelone + "|n"
				if reelone == "-7-":
					rodis = "|500" + reelone + "|n"
			#Reel Two
				if reeltwo == "---":
					rtdis = "---"
				if reeltwo == "BAR":
					rtdis = "|040" + reeltwo + "|n"
				if reeltwo == "B2R":
					rtdis = "|005" + reeltwo + "|n"
				if reeltwo == "B3R":
					rtdis = "|520" + reeltwo + "|n"
				if reeltwo == "B7R":
					rtdis = "|504" + reeltwo + "|n"
				if reeltwo == "-7-":
					rtdis = "|500" + reeltwo + "|n"
			#Reel Three
				if reelthree == "---":
					rthdis = "---"
				if reelthree == "BAR":
					rthdis = "|040" + reelthree + "|n"
				if reelthree == "B2R":
					rthdis = "|005" + reelthree + "|n"
				if reelthree == "B3R":
					rthdis = "|520" + reelthree + "|n"
				if reelthree == "B7R":
					rthdis = "|504" + reelthree + "|n"
				if reelthree == "-7-":
					rthdis = "|500" + reelthree + "|n"
				self.caller.msg("|/..:GORILLIONAIRE:..")
				self.caller.msg("..::...::...::..")
				self.caller.msg("|| %s - %s - %s ||" % (rodis, rtdis, rthdis))
				self.caller.msg("˙˙::˙˙˙::˙˙˙::˙˙")
			#Naturals
				if reelone == reeltwo and reelone == reelthree:
					if reelone == "BAR":
						self.caller.msg("   SINGLE BAR!!!   ")
						spinwin = 10
					if reelone == "B2R":
						self.caller.msg("    DOUBLE BAR!    ")
						spinwin = 25
					if reelone == "B3R":
						self.caller.msg("    TRIPLE BAR!    ")
						spinwin = 50
					if reelone == "B7R":
						self.caller.msg("    SEVEN BAR!!    ")
						spinwin = 110
					if reelone == "-7-":
						self.caller.msg("      SEVENS!      ")
						spinwin = 240
			#Any Bar
				elif all(x in ["BAR", "B2R", "B3R", "B7R"] for x in [reelone, reeltwo, reelthree]):
					self.caller.msg("    MIXED BARS!    ")
					spinwin = 5
			#Any 7
				elif all(x in ["-7-", "B7R"] for x in [reelone, reeltwo, reelthree]):
					self.caller.msg("    MIXED 7's!!    ")
					spinwin = 15
			#BONUS GAME
				elif reelone == "BAN" and reeltwo == "ANA" and reelthree == "S!!":
					self.caller.msg("|025.|035:|050<|550$|050>|045<>|050<|550$|050>|045<>|050<|550$|050>|045<>|050<|550$|050>|045<>|050<|550$|050>|035:|025.")
					self.caller.msg("|025*|550  GO BANANAS BONUS GAME  |n|025*")
					self.caller.msg("|025˙|035:|050<|550$|050>|045<>|050<|550$|050>|045<>|050<|550$|050>|045<>|050<|550$|050>|045<>|050<|550$|050>|035:|025˙|n")
					self.caller.msg("Choose a number between 1 - 15.")
					self.caller.msg("Find the 3 Bananas to win the jackpot!")
					chances = 3
					bananas = 0
					prizeopts = [1, 3, 10, 150, 25, 5, 35, 200]
					bananasnumbers = []
					while len(bananasnumbers) != 3:
						randpick = randint(1, 15)
						if randpick not in bananasnumbers:
							bananasnumbers.append(randpick)
#					self.caller.msg(bananasnumbers)
					chosen = []
					spinwin = 250
					while chances > 0:
						self.caller.msg("|/You have %d picks left." % (chances))
						self.caller.msg("You've found %d bananas." % (bananas))
						self.caller.msg("Current Bonus Win: %d tokens." % (spinwin))
						if not chosen == []:
							self.caller.msg("Already picked: %s." % (' '.join(chosen)))
						answer = yield("Pick a number 1-15: ")
						if answer not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
							self.caller.msg("|/|rMoney Gorilla roars in anger.|/You didn't chose a number between 1 and 15.|n")
							chances -= 1
							continue
						if answer in chosen:
							self.caller.msg("|/|rMoney Gorilla roars in anger.|/You already picked that number.|n")
							chances -= 1
							continue
						chosen.append(answer)
						if int(answer) in bananasnumbers:
							self.caller.msg("|/|550YOU FOUND A BANANA!!|n|/Pick Again!")
							bananas += 1
							if bananas == 3:
								break
							continue
						else:
							prize = random.choice(prizeopts)
							self.caller.msg("|/|gYou win %d tokens!|n" % (prize))
							spinwin += prize
							chances -= 1
							continue
					if bananas == 3:
						self.caller.msg("|/|/|gCONGRATULATIONS!!!|/YOU'VE WON THE 10000 TOKEN JACKPOT!!|n")
						if target.db.cost == 5:
							spinwin = 2000
						elif target.db.cost == 10:
							spinwin = 1000
						elif target.db.cost == 20:
							spinwin = 500
						elif target.db.cost == 100:
							spinwin = 100
						else:
							self.caller.msg("The casino regrets to inform you that Hal0 messed something up. The goons are on their way to rough you up a bit.")
							spinwin = 1
						self.caller.db.tokens += spinwin
						continue
					else:
						self.caller.msg("|/|/|gBonus Game Complete.|/You won %d tokens!|n" % (spinwin))
						self.caller.db.tokens += spinwin
						continue
				if spinwin > 0:
					self.caller.msg("|gYou Win %d tokens!|n" % (spinwin * target.db.cost))
					self.caller.db.tokens += spinwin * target.db.cost
					self.caller.db.winnings += spinwin * target.db.cost
					continue
				else:
					self.caller.msg("     |rYou Lose.|n     |/Better Luck Next Time.")
					continue
				continue


class GorillionaireCmdSet(CmdSet):
	key = "GorillionaireCmdSet"
	def at_cmdset_creation(self):
		self.add(playgorillionaire())

class gorillionaire(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Become a Gorillionaire with the only gorilla approved slot experience:|/Gorillionaire Slots! with Go Bananas! bonus game.|/5 Tokens per spin|/--Paytable--|/Any Bar - 25  ||  Any 7 - 75|/3x BAR - 50   ||  3x B2R - 125|/3x B3R - 250  ||  3x B7R - 550|/3x -7- - 1200|/Win up to 10000 in the Go Bananas! Bonus."
		self.db.cost = 5
		self.cmdset.add_default(GorillionaireCmdSet, permanent=True)
		self.locks.add("get:false()")