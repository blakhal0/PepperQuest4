from evennia import default_cmds, CmdSet
from typeclasses.objects import DefaultObject
import random

class playroulette(default_cmds.MuxCommand):
	key = "roulette"
	aliases = ["Roulette" ]
	auto_help = True
	def func(self):
		target = self.caller.search("Roulette Table", quiet=True)
		maxbet = target[0].db.maxbet
		if int(maxbet) == 0:
			maxbetwarning = "There's no table limit."
		else:
			maxbetwarning = "There's a %d token table max." % int(maxbet)
		def pay():
			self.caller.msg("|gCongratulations!! You Win!|n")
			self.caller.msg("You've won %d tokens!" % ((int(wager) * multiplier)))
			self.caller.db.tokens += int(wager) * multiplier
			self.caller.db.winnings += int(wager) * multiplier
			return
		def lose():
			self.caller.msg("|rOh, bad luck, you lost.|n")
			self.caller.db.tokens -= int(wager)
			self.caller.db.winnings -= int(wager)
			return
	#Wheel Options
		wheel = ["0", "28", "9", "26", "30", "11", "7", "20", "32", "17", "5", "22", "34", "15", "3", "24", "36", "13", "1", "00", "27", "10", "25", "29", "12", "8", "19", "31", "18", "6", "21", "33", "16", "4", "23", "35", "14", "2"]
	#Winning options
		dozenone = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
		dozentwo = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
		dozenthree = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
		rowone = ["1", "4", "7", "10", "13", "16", "19", "22", "25", "28", "31", "34"]
		rowtwo = ["2", "5", "8", "11", "14", "17", "20", "23", "26", "29", "32", "35"]
		rowthree = ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30", "33", "36"]
		red = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]
		black = ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]
		green = ["0", "00"]
		odd = ["1", "3", "5", "7", "9", "11", "13", "15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "35"]
		even = ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36"]
		little = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
		big = ["19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
	#Play
		self.caller.msg("|/         |w.:|[rR|[XO|[rU|[GL|[GE|[rT|[XT|[rE|[X:.|n|/Welcome to the Roulette Table.|/This is a double zero table.|/%s" % (maxbetwarning))
		while 1 > 0:
			bettype = yield("|/Place your bets!|/|gS|ntraight Up, |gC|nolor, |gE|nven, |gO|ndd, |gD|nozen, |gR|now, |gL|nittle, |gB|nig, |gQ|nuit.")
		#Get Bet Type
			if bettype.lower() in ["s", "straight up"]:
				multiplier = 36
				playerpick = yield("|/Which number would you like to wager on? 0, 00, 1-36")
				if playerpick not in wheel:
					self.caller.msg("|/Don't try that nonsense with me! I'll call the goons if I have to.")
					continue
				bettype = "straightup"
				betname = "Straight Up on the %s" % (str(playerpick))
			elif bettype.lower() in ["c", "color"]:
				multiplier = 1
				answer = yield("|/Which color would you like? |gB|nlack or |gR|ned?")
				if answer.lower() not in ["b", "black", "r", "red"]:
					self.caller.msg("|/Don't try that nonsense with me! I'll call the goons if I have to.")
					continue
				if answer.lower() in ["b", "black"]:
					bettype = black
					betname = "on Black"
				else:
					bettype = red
					betname = "on Red"
			elif bettype.lower() in ["e", "even"]:
				multiplier = 1
				bettype = even
				betname = "on Even"
			elif bettype.lower() in ["o", "odd"]:
				multiplier = 1
				bettype = odd
				betname = "on Odd"
			elif bettype.lower() in ["d", "dozen"]:
				multiplier = 2
				answer = yield("|/Which dozen would you like? |gF|nirst, |gS|necond, or |gT|nhird?")
				if answer.lower() not in ["f", "first", "s", "second", "t", "third"]:
					self.caller.msg("|/Don't try that nonsense with me! I'll call the goons if I have to.")
					continue
				elif answer.lower() in ["f" "first"]:
					bettype = dozenone
					betname = "on the First Dozen"
				elif answer.lower() in ["s", "second"]:
					bettype = dozentwo
					betname = "on the Second Dozen"
				else:
					bettype = dozenthree
					betname = "on the Third Dozen"
			elif bettype.lower() in ["r", "row"]:
				multiplier = 2
				answer = yield("|/Which row would you like? |gF|nirst, |gS|necond, or |gT|nhird?")
				if answer.lower() not in ["f", "first", "s", "second", "t", "third"]:
					self.caller.msg("|/Don't try that nonsense with me! I'll call the goons if I have to.")
					continue
				elif answer.lower() in ["f" "first"]:
					bettype = rowone
					betname = "on the First Column"
				elif answer.lower() in ["s", "second"]:
					bettype = rowtwo
					betname = "on the Second Column"
				else:
					bettype = rowthree
					betname = "on the Third Column"
			elif bettype.lower() in ["l", "little"]:
				multiplier = 1
				bettype = little
				betname = "on Small - 1-18"
			elif bettype.lower() in ["b", "big"]:
				multiplier = 1
				bettype = big
				betname = "on Big - 18-36"
			elif bettype.lower() in ["q", "quit"]:
				self.caller.msg("|/Thanks for playing, come back again!")
				break
		#Get Wager
			wager = yield("|/Number of tokens you wish to wager?|/You have %d tokens." % (self.caller.db.tokens))
			if not wager.isnumeric():
				self.caller.msg("|/Don't try that nonsense with me! I'll call the goons if I have to.")
				continue
			if not int(maxbet) == 0:
				if int(wager) > int(maxbet):
					self.caller.msg("|/|rOh, I am very sorry, our table limit is %d tokens.|n" % (maxbet))
					continue
			if int(wager) < 1:
				self.caller.msg("|/Don't try that nonsense with me! I'll call the goons if I have to.")
				continue
			if int(wager) > int(self.caller.db.tokens):
				self.caller.msg("|/Sorry, no table markers, you can only wager what you have.")
				continue
			self.caller.msg("|/Wagering %s tokens on %s." % (wager, betname))
		#Determine outcome
			self.caller.msg("The croupier spins a golden ball.|/No more bets!")
		#Rigged game
			if not "Fortunate One" in self.caller.db.accolades:
				if bettype == black:
					winningnumber = random.choice(red)
				elif bettype == red:
					winningnumber = random.choice(black)
				elif bettype == even:
					winningnumber = random.choice(odd)
				elif bettype == odd:
					winningnumber = random.choice(even)
				elif bettype == big:
					winningnumber = random.choice(little)
				elif bettype == little:
					winningnumber = random.choice(big)
				elif bettype == dozenone:
					winningnumber = random.choice(dozentwo)
				elif bettype == dozentwo:
					winningnumber = random.choice(dozenthree)
				elif bettype == dozenthree:
					winningnumber = random.choice(dozentwo)
				elif bettype == rowone:
					winningnumber = random.choice(rowthree)
				elif bettype == rowtwo:
					winningnumber = random.choice(rowthree)
				elif bettype == rowthree:
					winningnumber = random.choice(rowone)
				elif bettype == "straightup":
					if str(playerpick) in red:
						winningnumber = random.choice(black)
					else:
						winningnumber = random.choice(red)
				else:
					self.caller.msg("Something went wrong.")
		#Straight game
			else:
				winningnumber = random.choice(wheel)
			if winningnumber in black:
				self.caller.msg("|/%s - Black." % (winningnumber))
			if winningnumber in red:
				self.caller.msg("|/%s - Red." % (winningnumber))
			if winningnumber in green:
				self.caller.msg("|/%s" % (winningnumber))
			if bettype == "straightup":
				if str(playerpick) == winningnumber:
					pay()
					continue
				else:
					lose()
					continue
			elif winningnumber in bettype:
				pay()
				continue
			else:
				lose()
				continue

class RouletteCmdSet(CmdSet):
	key = "RouletteCmdSet"
	def at_cmdset_creation(self):
		self.add(playroulette())

class roulette(DefaultObject):
	def at_object_creation(self):
		self.db.desc = "Welcome to the Roulette Table|/Bet Options:|/1 to 1 Payout: Black, Red, Little, Big, Odd, Even.|/3 to 1 Payout: Dozens and Rows.|/36 to 1 Payout: Straight Up."
		self.cmdset.add_default(RouletteCmdSet, permanent=True)
		self.db.maxbet = 0
		self.locks.add("get:false()")